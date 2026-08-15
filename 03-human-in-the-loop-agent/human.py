from langgraph.types import interrupt

def human_review_node(state):

    decision = interrupt(
        {
            "customer_name": state.customer_name,
            "loan_amount": state.loan_amount,
            "credit_score": state.credit_score,
            "risk_level": state.risk_level,
            "confidence_score": state.confidence_score,
        }
    )

    if decision:
        for key, value in decision.items():
            setattr(state, key, value)

    return state