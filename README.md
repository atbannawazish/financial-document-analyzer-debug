# Financial Document Analyzer (CrewAI Debug Challenge Submission)

## Overview

This project is a debugged and optimized version of the original CrewAI-based Financial Document Analyzer system.

The original repository contained:
- Deterministic execution bugs
- Inefficient and hallucination-prone prompts
- Improper file handling
- Token overflow issues
- Poor repository hygiene

All issues have been identified, fixed, and improved.

---

## Issues Identified & Fixes

### 1. Deterministic Bugs Fixed
- File path was not passed correctly to Crew tasks
- FinancialDocumentTool used a static path instead of dynamic upload path
- Crew kickoff inputs were incomplete
- Groq token limit errors due to excessive prompt size
- Missing structured output formatting
- Unsafe repository (tracked local files like PDFs and .env)

### 2. Prompt Optimization
- Removed hallucination instructions
- Enforced strict document-only financial analysis
- Prevented fabricated URLs and market trends
- Structured deterministic financial output format

---

## Tech Stack

- Python
- FastAPI
- CrewAI
- LangChain
- Groq LLM
- SQLAlchemy (if database integration implemented)

---

## How to Run

### 1. Clone Repository
```bash
git clone https://github.com/atbannawazish/financial-document-analyzer-debug.git
cd financial-document-analyzer-debug