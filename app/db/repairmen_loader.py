import pandas as pd
from langchain.docstore.document import Document
from pathlib import Path
from typing import Optional


def load_repairmen(csv_path: Optional[Path] = None) -> list[Document]:
    if csv_path is None:
        base_dir = Path(__file__).resolve().parent.parent
        csv_path = base_dir / "data" / "repairmen.csv"

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
