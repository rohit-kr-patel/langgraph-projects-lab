from dataclasses import dataclass, field
from typing import Any, List, Optional
from uuid import uuid4


@dataclass
class AgentState:
    """
    Shared state for the Observable & Supervised Agent.

    This state is the single source of truth and flows through
    supervisor, worker, and router nodes.
    """

    # ─────────────────────────────────────────────
    # Task identity
    # ─────────────────────────────────────────────
    task: str
    execution_id: str = field(default_factory=lambda: str(uuid4()))
    decision: str | None = None
    # ─────────────────────────────────────────────
    # Execution progress
    # ─────────────────────────────────────────────
    current_step: str = "initialized"
    status: str = "running"  # running | success | failed

    # ─────────────────────────────────────────────
    # Worker results
    # ─────────────────────────────────────────────
    worker_output: Optional[Any] = None
    confidence_score: Optional[float] = None

    # ─────────────────────────────────────────────
    # Control & safety
    # ─────────────────────────────────────────────
    retry_count: int = 0
    max_retries: int = 3

    # ─────────────────────────────────────────────
    # Observability
    # ─────────────────────────────────────────────
    events: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    # ─────────────────────────────────────────────
    # Helper methods (optional but useful)
    # ─────────────────────────────────────────────
    def add_event(self, event: str) -> None:
        """Append an observability event."""
        self.events.append(event)

    def add_error(self, error: str) -> None:
        """Append an error record."""
        self.errors.append(error)

    def increment_retry(self) -> None:
        """Increment retry count safely."""
        self.retry_count += 1
