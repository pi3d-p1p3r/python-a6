import math

# Parameters
S0, K, r, q, sigma, T, n = 484, 480, 0.10, 0.03, 0.25, 2/12, 4

# Binomial parameters
dt = T / n
u = math.exp(sigma * math.sqrt(dt))
d = 1 / u
p = (math.exp((r - q) * dt) - d) / (u - d)
discount = math.exp(-r * dt)

print(f"Binomial Tree: u={u:.4f}, d={d:.4f}, p={p:.4f}")

# Build stock price tree
S = {}
for i in range(n + 1):
    for j in range(i + 1):
        S[(i,j)] = S0 * (u**(i-j)) * (d**j)

# Option values at maturity (put payoff)
P = {}
for j in range(n + 1):
    P[(n,j)] = max(0, K - S[(n,j)])

print(f"Stock prices at maturity: {[f'{S[(n,j)]:.2f}' for j in range(n+1)]}")
print(f"Put payoffs at maturity: {[f'{P[(n,j)]:.2f}' for j in range(n+1)]}")

# Backward induction with early exercise
early_exercise_optimal = False
for i in range(n-1, -1, -1):
    for j in range(i + 1):
        continuation = discount * (p * P[(i+1,j)] + (1-p) * P[(i+1,j+1)])
        exercise = max(0, K - S[(i,j)])
        P[(i,j)] = max(continuation, exercise)
        
        if exercise > continuation:
            early_exercise_optimal = True

# Calculate European put for comparison
P_euro = dict(P)  # Copy final payoffs
for i in range(n-1, -1, -1):
    for j in range(i + 1):
        P_euro[(i,j)] = discount * (p * P_euro[(i+1,j)] + (1-p) * P_euro[(i+1,j+1)])

print(f"\nAmerican Put Value: ${P[(0,0)]:.4f}")
print(f"European Put Value: ${P_euro[(0,0)]:.4f}")
print(f"Early Exercise Premium: ${P[(0,0)] - P_euro[(0,0)]:.4f}")
print(f"Early exercise optimal: {early_exercise_optimal}")
