from app.db.repairmen_loader import load_repairmen
from app.core.config import settings
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from app.models.chat_model import LangChainResult
from typing import Any
import os


class ChatbotService:
    def __init__(self):
        os.environ["OPENAI_API_KEY"] = settings.openai_api_key  # ✅ cần có dòng này

        docs = load_repairmen()
        embeddings = OpenAIEmbeddings()
        self.vectorstore = FAISS.from_documents(docs, embeddings)

        self.chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(
                temperature=0
            ),  # ❌ không cần truyền openai_api_key thủ công
            retriever=self.vectorstore.as_retriever(),
        )

    def get_reply(self, message: str) -> LangChainResult:
        raw_result: dict[str, Any] = self.chain.invoke(message)
        return LangChainResult(**raw_result)
