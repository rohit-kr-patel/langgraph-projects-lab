from graph import graph
from state import ResearchState


initial_state = ResearchState(
    query="What is LangGraph?"
)

result = graph.invoke(initial_state)


print("\n========== RESEARCH NOTES ==========")
print(result["research_notes"])


print("\n========== VERIFIED NOTES ==========")
print(result["verified_notes"])


print("\n========== FINAL ANSWER ==========")
print(result["final_answer"])


print("\n========== HISTORY ==========")

for item in result["history"]:
    print("-", item)