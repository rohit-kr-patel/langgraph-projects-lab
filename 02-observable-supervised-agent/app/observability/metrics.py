from typing import Dict


# Global in-memory metrics store
_METRICS: Dict[str, object] = {
    "total_executions": 0,
    "successful_executions": 0,
    "failed_executions": 0,
    "total_retries": 0,
    "failure_reasons": {},  # reason -> count
}


def increment(metric_name: str, value: int = 1) -> None:
    """
    Increment a numeric metric counter.
    """
    if metric_name not in _METRICS:
        return

    if isinstance(_METRICS[metric_name], int):
        _METRICS[metric_name] += value


def increment_failure(reason: str) -> None:
    """
    Increment failure counters and track failure reasons.
    """
    _METRICS["failed_executions"] += 1

    reasons = _METRICS["failure_reasons"]
    reasons[reason] = reasons.get(reason, 0) + 1


def increment_retry() -> None:
    """
    Increment retry counter.
    """
    _METRICS["total_retries"] += 1


def mark_success() -> None:
    """
    Mark a successful execution.
    """
    _METRICS["successful_executions"] += 1


def get_metrics() -> Dict[str, object]:
    """
    Return a snapshot of all metrics.
    """
    return _METRICS.copy()
