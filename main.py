# main.py

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document
from langchain_community.document_loaders import PyPDFLoader

app = FastAPI(title="Financial Document Analyzer API")


# --------------------------------------------------
# Crew Runner
# --------------------------------------------------
def run_crew(query: str, file_content: str):
    try:
        crew = Crew(
            agents=[financial_analyst],
            tasks=[analyze_financial_document],
            process=Process.sequential,
        )

        result = crew.kickoff(
            inputs={
                "query": query,
                "file_content": file_content
            }
        )

        return str(result)

    except Exception as e:
        raise Exception(f"Crew execution failed: {str(e)}")


# --------------------------------------------------
# Health Check
# --------------------------------------------------
@app.get("/")
async def root():
    return {"status": "API running successfully"}


# --------------------------------------------------
# Analyze Endpoint
# --------------------------------------------------
@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    query: str = Form("Analyze this financial document for investment insights")
):
    file_id = str(uuid.uuid4())
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", f"{file_id}.pdf")

    try:
        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Extract PDF content
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        document_text = ""
        for doc in documents:
            document_text += doc.page_content + "\n"

        # 🔥 IMPORTANT: Limit document size to avoid token overflow
        MAX_CHARS = 8000   # Safe for Groq free tier
        document_text = document_text[:MAX_CHARS]

        if not query or query.strip() == "":
            query = "Analyze this financial document for investment insights"

        # Run Crew with extracted (limited) content
        analysis = run_crew(
            query=query.strip(),
            file_content=document_text
        )

        return {
            "status": "success",
            "file_name": file.filename,
            "analysis": analysis
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing document: {str(e)}"
        )

    finally:
        # Cleanup temporary file
        if os.path.exists(file_path):
            os.remove(file_path)


# --------------------------------------------------
# Run Server
# --------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)