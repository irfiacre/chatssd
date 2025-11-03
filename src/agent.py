import os
from dotenv import load_dotenv
from src.prompt import buildSystemPrompt
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from pydantic import BaseModel
from langchain.agents.structured_output import ToolStrategy


load_dotenv()

class ResponseStructure(BaseModel):
    response: str

def handleAgentResponse(question: str, country: str) -> str:
    """
    Handles the AI agent response.
    """
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    
    if not GOOGLE_API_KEY:
        raise ValueError("Missing GOOGLE_API_KEY environment variable.")
    
    model = init_chat_model(
        model="google_genai:gemini-2.5-flash-lite",
        temperature=0.7,
        timeout=30,
        max_tokens=1000,
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
