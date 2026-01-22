from datetime import datetime
from typing import Optional, Dict, Any


def log_event(  event_name: str,  state,metadata: Optional[Dict[str, Any]] = None,
) -> None:
    """
    Emit a structured observability event.

    This function has no side effects other than logging.
    It must not modify state or influence control flow.
    """

    log_record = {
        "event": event_name,
        "execution_id": state.execution_id,
        "current_step": state.current_step,
        "retry_count": state.retry_count,
        "timestamp": datetime.utcnow().isoformat(),
        "metadata": metadata or {},
    }

    print(log_record)
