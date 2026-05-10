import os
from dotenv import load_dotenv
from src.prompt import buildSystemPrompt
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from pydantic import BaseModel
from langchain.agents.structured_output import ToolStrategy
from langchain_deepseek import ChatDeepSeek
from mistralai import Mistral


load_dotenv()

class ResponseStructure(BaseModel):
    response: str

def handleAgentResponse(question: str, country: str) -> str:
    """
    Handles the AI agent response.
    """
    MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

    if not MISTRAL_API_KEY:
        raise ValueError("Missing MISTRAL_API_KEY environment variable.")

    model = Mistral(
        model="ministral-3b-latest",
        temperature=0,
        max_tokens=None,
        api_key=MISTRAL_API_KEY
    )
    agent = create_agent(
        model,
        system_prompt=buildSystemPrompt(country=country),
        response_format=ToolStrategy(ResponseStructure)
    )

    result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
    )

    return result["structured_response"].response
