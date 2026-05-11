import os
from dotenv import load_dotenv
from src.prompt import buildSystemPrompt
from langchain.agents import create_agent

from pydantic import BaseModel
from langchain.agents.structured_output import ToolStrategy
from langchain_mistralai import ChatMistralAI


load_dotenv()

class ResponseStructure(BaseModel):
    response: str

MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")
if not MISTRAL_API_KEY:
    raise ValueError("Missing MISTRAL_API_KEY environment variable.")

model = ChatMistralAI(
    model="mistral-medium-latest",
    temperature=0,
    max_retries=2,
    api_key=MISTRAL_API_KEY,
)


def handleAgentResponse(question: str, country: str) -> str:
    """
    Handles the AI agent response.
    """
    agent = create_agent(
        model,
        system_prompt=buildSystemPrompt(country=country),
        response_format=ToolStrategy(ResponseStructure)
    )

    result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
    )

    return result["structured_response"].response
