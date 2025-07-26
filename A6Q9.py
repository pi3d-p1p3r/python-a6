import numpy as np
from scipy.stats import norm
import math

# Given parameters
S0 = 30      # Current stock price
K = 29       # Exercise price
r = 0.05     # Risk-free interest rate (5%)
sigma = 0.25 # Volatility (25% per annum)
T = 4/12     # Time to maturity (4 months = 1/3 year)

print("Option Pricing Problem")
print("=" * 50)
print(f"Stock Price (S₀): ${S0}")
print(f"Exercise Price (K): ${K}")
print(f"Risk-free Rate (r): {r*100}%")
print(f"Volatility (σ): {sigma*100}%")
print(f"Time to Maturity (T): {T:.4f} years ({4} months)")
print()

# Calculate d1 and d2
d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
d2 = d1 - sigma*np.sqrt(T)

print("Intermediate calculations:")
print(f"d₁ = {d1:.4f}")
print(f"d₂ = {d2:.4f}")
print(f"N(d₁) = {norm.cdf(d1):.4f}")
print(f"N(d₂) = {norm.cdf(d2):.4f}")
print(f"N(-d₁) = {norm.cdf(-d1):.4f}")
print(f"N(-d₂) = {norm.cdf(-d2):.4f}")
print()

# (a) European Call Option Price
call_price = S0 * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
print("(a) European Call Option Price:")
print(f"C = S₀×N(d₁) - K×e^(-rT)×N(d₂)")
print(f"C = {S0}×{norm.cdf(d1):.4f} - {K}×{np.exp(-r*T):.4f}×{norm.cdf(d2):.4f}")
print(f"C = ${call_price:.4f}")
print()

# (b) American Call Option Price
# For non-dividend-paying stocks, American call = European call
american_call_price = call_price
print("(b) American Call Option Price:")
print("For non-dividend-paying stocks, American call = European call")
print(f"American Call Price = ${american_call_price:.4f}")
print()

# (c) European Put Option Price
put_price = K * np.exp(-r*T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
print("(c) European Put Option Price:")
print(f"P = K×e^(-rT)×N(-d₂) - S₀×N(-d₁)")
print(f"P = {K}×{np.exp(-r*T):.4f}×{norm.cdf(-d2):.4f} - {S0}×{norm.cdf(-d1):.4f}")
print(f"P = ${put_price:.4f}")
print()

# (d) Verify Put-Call Parity
print("(d) Put-Call Parity Verification:")
print("Put-Call Parity: C + K×e^(-rT) = P + S₀")
print()

left_side = call_price + K * np.exp(-r*T)
right_side = put_price + S0

print(f"Left side:  C + K×e^(-rT) = {call_price:.4f} + {K}×{np.exp(-r*T):.4f}")
print(f"           = {call_price:.4f} + {K * np.exp(-r*T):.4f}")
print(f"           = ${left_side:.4f}")
print()

print(f"Right side: P + S₀ = {put_price:.4f} + {S0}")
print(f"           = ${right_side:.4f}")
print()

print(f"Difference: |Left - Right| = |{left_side:.4f} - {right_side:.4f}| = {abs(left_side - right_side):.6f}")

if abs(left_side - right_side) < 1e-10:
    print("✓ Put-Call Parity HOLDS (difference is negligible)")
else:
    print("✗ Put-Call Parity does NOT hold")

print("\n" + "=" * 50)
print("SUMMARY:")
print(f"European Call Price: ${call_price:.4f}")
print(f"American Call Price: ${american_call_price:.4f}")
print(f"European Put Price:  ${put_price:.4f}")
print(f"Put-Call Parity:     ✓ Verified")
