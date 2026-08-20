from state import ResearchState
from llm import invoke_llm


def research_agent(
    state: ResearchState,
) -> ResearchState:

    prompt = f"""
You are a research assistant.

Research the following topic:

{state.query}

Provide:
1. A brief overview
2. Key points
3. Important facts

Keep the response concise.
"""

    response = invoke_llm(prompt)

    state.research_notes = response

    state.history.append(
        f"Research Agent completed for query: {state.query}"
    )

    return state