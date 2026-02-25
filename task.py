# task.py

from crewai import Task
from agents import financial_analyst


analyze_financial_document = Task(
    description=(
        "You are given the FULL extracted financial document below:\n\n"
        "{file_content}\n\n"

        "Using ONLY the above content, extract and analyze:\n"
        "- Revenue\n"
        "- Net Income\n"
        "- Operating Margin\n"
        "- Debt Levels\n"
        "- Cash Flow\n"
        "- Business Risks\n\n"

        "User Query: {query}\n\n"

        "STRICT RULES:\n"
        "- Do NOT fabricate numbers\n"
        "- Do NOT invent trends\n"
        "- Do NOT use external websites\n"
        "- If data is missing, write 'Not mentioned in document'\n"
    ),
    expected_output=(
        "Return structured analysis:\n\n"
        "1. Company Overview\n"
        "2. Key Financial Metrics (with actual numbers)\n"
        "3. Growth Trends\n"
        "4. Risk Factors\n"
        "5. Investment Outlook (Bullish / Neutral / Bearish with justification)\n"
    ),
    agent=financial_analyst,
    async_execution=False,
)