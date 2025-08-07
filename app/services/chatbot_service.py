from app.db.repairmen_loader import load_repairmen
from app.core.config import settings
from app.llm.llm_client_factory import get_llm_chat_model
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from app.models.chat_model import LangChainResult
from typing import Any



class ChatbotService:
    def __init__(self):
        docs = load_repairmen()
        embeddings = OpenAIEmbeddings(api_key=settings.openai_api_key)
        self.vectorstore = FAISS.from_documents(docs, embeddings)
        
        llm = get_llm_chat_model()
        

        self.chain = RetrievalQA.from_chain_type(
            llm=llm,  # ❌ không cần truyền openai_api_key thủ công
            retriever=self.vectorstore.as_retriever(),
        )

    def get_reply(self, message: str) -> LangChainResult:
        raw_result: dict[str, Any] = self.chain.invoke(message)
        return LangChainResult(**raw_result)
