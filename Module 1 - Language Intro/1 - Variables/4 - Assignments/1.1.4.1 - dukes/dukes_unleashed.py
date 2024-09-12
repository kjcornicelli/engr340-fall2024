"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

in_state_cost = 30792
out_state_cost = 47882

interest = 0.05

in_state_gift = in_state_cost/interest

out_state_gift = out_state_cost/interest

print("In state gift needed to return total yearly cost of tuition is", in_state_gift)
print("Out of state gift needed to return total yearly cost of tuirion is", out_state_gift)