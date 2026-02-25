import os
from dotenv import load_dotenv
from crewai import Agent
from crewai.llm import LLM
from tools import FinancialDocumentTool

load_dotenv()

# -----------------------------
# Load Groq LLM
# -----------------------------
llm = LLM(
    model="llama-3.3-70b-versatile",  # Free Groq model
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    temperature=0.7
)

# -----------------------------
# Financial Analyst Agent
# -----------------------------
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial documents and provide structured, data-driven investment insights.",
    backstory=(
        "You are an experienced financial analyst specializing in corporate earnings, "
        "financial statements, risk analysis, and investment evaluation. "
        "You strictly analyze the provided document and avoid speculation."
    ),
    verbose=True,
    memory=True,
    tools=[FinancialDocumentTool()],
    llm=llm,
    max_iter=2,
    allow_delegation=False
)

# -----------------------------
# Risk Assessment Agent
# -----------------------------
risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Identify financial risks and market uncertainties based on the financial document.",
    backstory=(
        "You specialize in identifying liquidity risk, leverage risk, "
        "market volatility, macroeconomic risk, and operational risks."
    ),
    verbose=True,
    llm=llm,
    max_iter=1,
    allow_delegation=False
)

# -----------------------------
# Investment Strategy Advisor
# -----------------------------
investment_advisor = Agent(
    role="Investment Strategy Advisor",
    goal="Provide responsible, evidence-based investment recommendations.",
    backstory=(
        "You focus on long-term portfolio growth, diversification, "
        "risk-adjusted returns, and sustainable financial strategies."
    ),
    verbose=True,
    llm=llm,
    max_iter=1,
    allow_delegation=False
)