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






def fact_checker_agent(
    state: ResearchState,
) -> ResearchState:

    prompt = f"""
You are a fact-checking assistant.

Review the research notes below.

Research Notes:
{state.research_notes}

Tasks:
1. Verify factual accuracy.
2. Correct any mistakes.
3. Remove unsupported claims.
4. Produce a cleaned and verified version.

Return only the verified notes.
"""

    response = invoke_llm(prompt)

    state.verified_notes = response

    state.history.append(
    f"Fact Checker completed for query: {state.query}"
)

    return state



def summarizer_agent(
    state: ResearchState,
) -> ResearchState:

    prompt = f"""
You are a summarization assistant.

Using the verified notes below, create a concise and easy-to-read answer.

Verified Notes:
{state.verified_notes}

Requirements:
- Keep it clear and factual
- Use bullet points if helpful
- Focus on the most important information
- Maximum 80 words
"""

    response = invoke_llm(prompt)

    state.final_answer = response

    state.history.append(
        "Summarizer Agent completed"
    )

    return state


def supervisor_agent(
    state: ResearchState,
) -> ResearchState:

    if not state.research_notes:
        state.next_agent = "research"

    elif not state.verified_notes:
        state.next_agent = "fact_checker"

    elif not state.final_answer:
        state.next_agent = "summarizer"

    else:
        state.next_agent = "end"

    print(
        f"[SUPERVISOR] Routing -> {state.next_agent}"
    )

    state.history.append(
        f"Supervisor routed to {state.next_agent}"
    )

    return state