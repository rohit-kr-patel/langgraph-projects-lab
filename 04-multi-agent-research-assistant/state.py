
from dataclasses import dataclass, field
from typing import List

@dataclass
class ResearchState:
    query: str

    research_notes: str = ""

    verified_notes: str = ""

    final_answer: str = ""

    next_agent: str = ""

    status: str = "STARTED"

    history: list[str] = field(default_factory=list)