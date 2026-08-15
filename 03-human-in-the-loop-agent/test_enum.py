import state

print("State file:", state.__file__)

print("WorkflowState class id:", id(state.WorkflowState))

s = state.LoanApprovalState()

print("\nCurrent state:", s.current_state)
print("Current repr:", repr(s.current_state))
print("Current type:", type(s.current_state))
print("Current type id:", id(type(s.current_state)))

print("\nExpected:", state.WorkflowState.INIT)
print("Expected repr:", repr(state.WorkflowState.INIT))
print("Expected type:", type(state.WorkflowState.INIT))
print("Expected type id:", id(type(state.WorkflowState.INIT)))

print("\n== :", s.current_state == state.WorkflowState.INIT)
print("is :", s.current_state is state.WorkflowState.INIT)
print("value:", s.current_state.value)