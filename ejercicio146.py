# Exercise 146
"""
The present value - pv and the investment period - n are given below:
pv = 1000
n = 10
Depending on the interest rates given below, calculate the future value fv of
your investment:
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
Round the result to the full cent and print the result to the console.
Expected result:
[1104.62, 1218.99, 1343.92, 1480.24, 1628.89, 1790.85, 1967.15]
"""
PV = 1000
N = 10
rate = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07]
FVS = [round(PV * (1 + r) ** N, 2) for r in rate]
print(FVS)
