import numpy as np
import math

# Parameters
F0, K, r, sigma, T, n = 60, 60, 0.08, 0.30, 0.5, 2

# Binomial parameters
dt = T / n
u = math.exp(sigma * math.sqrt(dt))
d = 1 / u
p = (1 - d) / (u - d)
discount = math.exp(-r * dt)

print(f"Binomial Tree: u={u:.4f}, d={d:.4f}, p={p:.4f}")

# Build futures price tree
F = {}
for i in range(n + 1):
    for j in range(i + 1):
        F[(i,j)] = F0 * (u**(i-j)) * (d**j)

# Option values at maturity
C = {}
for j in range(n + 1):
    C[(n,j)] = max(0, F[(n,j)] - K)

print(f"\nFutures prices at maturity: {[F[(n,j)] for j in range(n+1)]}")
print(f"Option payoffs at maturity: {[C[(n,j)] for j in range(n+1)]}")

# Backward induction
for i in range(n-1, -1, -1):
    for j in range(i + 1):
        C[(i,j)] = discount * (p * C[(i+1,j)] + (1-p) * C[(i+1,j+1)])

# Check early exercise optimality
early_exercise_optimal = False
for i in range(n):
    for j in range(i + 1):
        exercise_value = max(0, F[(i,j)] - K)
        if exercise_value > C[(i,j)]:
            early_exercise_optimal = True
            break

print(f"\nEuropean Call Value: ${C[(0,0)]:.4f}")
print(f"American Call Value: ${C[(0,0)]:.4f}")
print(f"Early exercise optimal: {early_exercise_optimal}")
