from scipy.optimize import linprog 

c = [57,13,20] # cost function coefficients

A = [[25, 0, 10], 
     [40, 30, 15] #coefficents of inequality constraints 
     
     ]

b = [0.20, 0.30] # RHS

# Bounds for variables (x1, x2, x3) - 
# they are all greater than or equal to 0

x_bounds = [(0, None), (0, None), (0, None)]

result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

#extract optimal solution and objective value
x_optimal = result.x
optimal_cost = result.fun

print("Optimal Solution:")
print("x1 =", x_optimal[0])
print("x2 =", x_optimal[1])
print("x3 =", x_optimal[2])
print("Optimal Cost Function Value:", optimal_cost)