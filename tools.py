# tools.py

import os
from dotenv import load_dotenv
from crewai.tools import BaseTool
from langchain_community.document_loaders import PyPDFLoader

load_dotenv()


# -----------------------------
# Financial Document Reader Tool
# -----------------------------
class FinancialDocumentTool(BaseTool):
    name: str = "Financial Document Reader"
    description: str = (
        "Reads and extracts text content from a provided financial PDF document."
    )

    def _run(self, file_path: str) -> str:
        """
        Reads the uploaded financial PDF file and returns extracted text.
        """

        if not os.path.exists(file_path):
            return "Error: File not found."

        loader = PyPDFLoader(file_path)
        documents = loader.load()

        full_text = ""

        for doc in documents:
            content = doc.page_content
            full_text += content.strip() + "\n"

        return full_text