# Linear Programming for Coal Purchasing Optimization
import numpy  as np                # type: ignore
import pandas as pd                # type: ignore
from scipy.optimize import linprog # type: ignore
# Supplier data
# Suppliers: Ashley, Bedford, Consol, Dunby, Earlam, Florence, Gaston, Hopt
# Prices: Cost per ton
# Union mines: 1 = Yes, 0 = No
# Transport modes: Rail or Truck
# Volatility: Percent volatility of each supplier
# Capacity: Max tons each supplier can deliver
# Data
suppliers      = ["Ashley", 
                  "Bedford", 
                  "Consol", 
                  "Dunby", 
                  "Earlam", 
                  "Florence", 
                  "Gaston", 
                  "Hopt"]
price          = [49.5, 50.0, 
                  61.0, 63.5, 
                  66.5, 71.0, 
                  72.5, 80.0]  # Cost per ton
is_union       = [1, 1, 0, 1, 0, 1, 0, 0]                          # Union mine: 1 = Yes, 0 = No
transport_mode = ["Rail", "Truck", 
                  "Rail", "Truck", 
                  "Truck", "Truck", 
                  "Rail", "Rail"]
volatility     = [15, 16, 18, 20, 21, 22, 23, 25]                  # Volatility percent
capacity       = [300, 600, 510, 655, 575, 680, 450, 490]          # Max tons each supplier can deliver
#
# Objective function coefficients (minimize cost)
# Coefficients for the objective function (cost per ton)
# We want to minimize the total cost of purchasing coal
#
c = price
# Constraints
# Equality constraint: total coal must equal 1225 mtons
# We need to purchase exactly 1225 mtons of coal
# Equality constraints (A_eq x = b_eq)
# Coefficients for the equality constraint
A_eq = [[1] * 8]
b_eq = [1225]
# Inequality constraints
# Inequality constraints (A_ub x <= b_ub)
A_ub = []
b_ub = []
#
# Volatility constraint: weighted volatility >= 19% => -volatility*x <= -232.75
# We want the weighted volatility to be less than or equal to 19%
# This is calculated as the sum of (volatility * purchased amount) / total purchased amount
# The total purchased amount is 1225 mtons, so we need to ensure that
# sum(volatility * purchased amount) <= 19% * 1225
# Rearranging gives us the inequality:
# sum(volatility * purchased amount) <= 232.75
# We can express this as:
#
A_ub.append([-v for v in volatility])
b_ub.append(-232.75)
#
# Union constraint: at least 50% from union mines => -union*x <= -612.5
# We want at least 50% of the total purchased amount to come from union mines
#
A_ub.append([-u for u in is_union])
b_ub.append(-612.5)
#
# Rail capacity constraint: x_rail <= 650
# We need to ensure that the amount purchased by rail does not exceed 650 mtons
#
A_ub.append([1 if m == "Rail" else 0 for m in transport_mode])
b_ub.append(650)
#
# Truck capacity constraint: x_truck <= 720
# We need to ensure that the amount purchased by truck does not exceed 720 mtons
#
A_ub.append([1 if m == "Truck" else 0 for m in transport_mode])
b_ub.append(720)
#
# Bounds for each supplier (0 <= x_i <= capacity_i)
# We need to ensure that the amount purchased from each supplier 
# is between 0 and their capacity
#
bounds = [(0, cap) for cap in capacity]
#
# Solve using linear programming
#
print("Running optimization...")
result = linprog(c=c, A_ub=A_ub, 
                      b_ub=b_ub, 
                      A_eq=A_eq, 
                      b_eq=b_eq,
                      bounds=bounds, 
                      method='highs')
#
# Process results
#
if result.success:
    purchased    = result.x
    total_cost   = np.dot(purchased, price)
    average_cost = total_cost / 1225
    df = pd.DataFrame({
        "Supplier": suppliers,
        "Price": price,
        "Purchased (mtons)": purchased,
        "Cost": [p * x for p, x in zip(price, purchased)]
    })
    print("\nOptimal Purchase Plan:")
    print(df.round(2).to_string(index=False))
    print(f"\nTotal Cost: ${total_cost:,.2f}")
    print(f"Average Cost per Ton: ${average_cost:.2f}")
else:
    print("Optimization failed:", result.message)