from app.db.repairmen_loader import load_repairmen
from app.core.config import settings
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA


class ChatbotService:
    def __init__(self):
        docs = load_repairmen()
        embeddings = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)
        self.vectorstore = FAISS.from_documents(docs, embeddings)
        self.chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(temperature=0, openai_api_key=settings.openai_api_key),
            retriever=self.vectorstore.as_retriever(),
        )

    def get_reply(self, message: str) -> str:
        return self.chain.run(message)
