from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_aws import ChatBedrock

from app.core.config import settings
from app.models.llm_provider_model import LLMProvider

def get_llm_chat_model():
    """
    Factory to create an OpenAI Chat Model using app settings.
    """
    match settings.llm_provider:
        case LLMProvider.OPENAI:
            return ChatOpenAI(
                api_key=settings.openai_api_key,
                model= settings.openai_model,
                temperature=0
            )
        case LLMProvider.GEMINI:
            return ChatGoogleGenerativeAI(
                google_api_key= settings.gemini_api_key,
                model=settings.gemini_model,
                temperature=0
            )
        case LLMProvider.BEDROCK:
            return ChatBedrock(
                region=settings.bedrock_region,
                model=settings.bedrock_model_id,
                temperature=0
            )
        case _:
            raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")
