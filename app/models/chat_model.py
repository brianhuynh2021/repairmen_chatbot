from pydantic import BaseModel


class LangChainResult(BaseModel):
    query: str
    result: str