import os
from dotenv import load_dotenv
from src.prompt import buildSystemPrompt
# from langchain.agents import create_agent
# from langchain.chat_models import init_chat_model
from pydantic import BaseModel
# from langchain.agents.structured_output import ToolStrategy
# from langchain_deepseek import ChatDeepSeek
from mistralai import Mistral


load_dotenv()

class ResponseStructure(BaseModel):
    response: str

MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")
if not MISTRAL_API_KEY:
    raise ValueError("Missing MISTRAL_API_KEY environment variable.")

client = Mistral(api_key=MISTRAL_API_KEY)


def handleAgentResponse(question: str, country: str) -> str:
    """
    Handles the AI agent response.
    """
    def query_mistral(prompt: str):
        response = client.chat.complete(
            model="mistral-medium-latest",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message

    questionPrompt = buildSystemPrompt(country=country, question=question)

    result = query_mistral(questionPrompt)
    return result
