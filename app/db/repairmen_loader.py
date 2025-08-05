import pandas as pd
from langchain.docstore.document import Document

def load_repairmen(csv_path: str = "../data/repairmen.csv") -> list[Document]:
    df = pd.read_csv(csv_path)

    documents = []
    for _, row in df.iterrows():
        content = f"""
        Tên: {row['name']}
        Loại dịch vụ: {row['type']}
        SĐT: {row['phone']}
        Khu vực: {row['area']}
        """
        documents.append(Document(page_content=content))

    return documents