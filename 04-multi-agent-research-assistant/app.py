from llm import invoke_llm
from state import ResearchState
from nodes import research_agent


state = ResearchState(
    query="What is LangGraph?"
)

result = research_agent(state)

print(result.research_notes)