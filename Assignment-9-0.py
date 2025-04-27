from pulp import LpMinimize, LpProblem, LpVariable, lpSum # type: ignore

# Create the problem
model = LpProblem("Apollo_Ad_Campaign", LpMinimize)

# Decision variables
x = LpVariable("Real_Estate_Ads", lowBound=0, cat="Integer")
y = LpVariable("Travel_Ads", lowBound=0, cat="Integer")

# Objective function: Minimize cost
model += 18500 * x + 29500 * y, "Total_Cost"

# Constraints
model += 15 * x + 2 * y >= 17, "Women_Reach"
model += 8 * x + 12 * y >= 20, "Men_Reach"

# Solve the problem
model.solve()

# Print results
print("Status:", model.status)
print("Real Estate Ads (x):", x.varValue)
print("Travel Ads (y):", y.varValue)
print("Total Cost: $", model.objective.value())