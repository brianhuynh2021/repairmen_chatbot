from enum import Enum


class LLMProvider(str, Enum):
    OPENAI = 'openai'
    GEMINI = 'gemini'
    BEDROCK = 'bedrock'
