from graph import graph
from state import LoanApprovalState
from langgraph.types import Command

config = {
    "configurable": {
        "thread_id": "loan-001"
    }
}

initial_state = LoanApprovalState(
    customer_name="Sohail verma",
    loan_amount=500000,
    credit_score=720,
)

# Start the workflow
result = graph.invoke(
    initial_state,
    config=config,
)

# Check if graph paused for human review
if "__interrupt__" in result:

    review = result["__interrupt__"][0].value

    print("\n========== HUMAN REVIEW ==========")
    print(f"Customer      : {review['customer_name']}")
    print(f"Loan Amount   : ₹{review['loan_amount']}")
    print(f"Credit Score  : {review['credit_score']}")
    print(f"Risk Level    : {review['risk_level']}")
    print(f"Confidence    : {review['confidence_score']}")
    print("==================================")

    print("\n1. Approve")
    print("2. Reject")
    print("3. Edit Credit Score")

    choice = input("\nEnter choice: ")

    if choice == "1":

        resume_data = {
            "human_decision": "APPROVED"
        }

    elif choice == "2":

        resume_data = {
            "human_decision": "REJECTED"
        }

    elif choice == "3":

        new_score = int(input("Enter new credit score: "))

        resume_data = {
            "human_decision": "APPROVED",
            "credit_score": new_score
        }

    else:

        print("Invalid choice. Rejecting by default.")

        resume_data = {
            "human_decision": "REJECTED"
        }

    # Resume workflow
    result = graph.invoke(
        Command(resume=resume_data),
        config=config,
    )

print("\n========== FINAL RESULT ==========")
print(result)