import math

# Given parameters
S = 19      # Current stock price
K = 20      # Strike price
C = 1       # Call option price
r = 0.03    # Risk-free rate (3% per annum)
T = 4/12    # Time to maturity (4 months = 1/3 year)

def european_put_call_parity(call_price, strike, stock_price, risk_free_rate, time_to_maturity):
    """
    Calculate European put option price using put-call parity
    
    Put-Call Parity: C + K*e^(-r*T) = P + S
    Solving for P: P = C + K*e^(-r*T) - S
    
    Parameters:
    - call_price: Price of call option
    - strike: Strike price
    - stock_price: Current stock price
    - risk_free_rate: Risk-free interest rate
    - time_to_maturity: Time to expiration in years
    """
    
    # Calculate present value of strike price
    pv_strike = strike * math.exp(-risk_free_rate * time_to_maturity)
    
    # Apply put-call parity formula
    put_price = call_price + pv_strike - stock_price
    
    return put_price, pv_strike

# Calculate the put option price
put_price, pv_strike = european_put_call_parity(C, K, S, r, T)

# Display detailed calculation
print("=" * 60)
print("EUROPEAN PUT OPTION PRICING")
print("=" * 60)
print(f"Given Information:")
print(f"  Current Stock Price (S): ${S}")
print(f"  Strike Price (K): ${K}")
print(f"  Call Option Price (C): ${C}")
print(f"  Risk-free Rate (r): {r*100}% per annum")
print(f"  Time to Maturity (T): {T:.4f} years ({T*12:.0f} months)")

print("\n" + "-" * 60)
print("PUT-CALL PARITY CALCULATION:")
print("-" * 60)
print(f"Formula: C + K×e^(-r×T) = P + S")
print(f"Solving for P: P = C + K×e^(-r×T) - S")

print(f"\nStep-by-step calculation:")
print(f"1. Present Value of Strike Price:")
print(f"   K×e^(-r×T) = ${K} × e^(-{r} × {T:.4f})")
print(f"   K×e^(-r×T) = ${K} × e^(-{r*T:.4f})")
print(f"   K×e^(-r×T) = ${K} × {math.exp(-r*T):.6f}")
print(f"   K×e^(-r×T) = ${pv_strike:.4f}")

print(f"\n2. Put Option Price:")
print(f"   P = C + K×e^(-r×T) - S")
print(f"   P = ${C} + ${pv_strike:.4f} - ${S}")
print(f"   P = ${put_price:.4f}")

print("\n" + "=" * 60)
print("RESULT:")
print("=" * 60)
print(f"**The 4-month European put option price is ${put_price:.2f}**")

# Verification - check put-call parity holds
print(f"\nVerification (Put-Call Parity Check):")
left_side = C + pv_strike
right_side = put_price + S
print(f"Left side (C + K×e^(-r×T)): ${left_side:.4f}")
print(f"Right side (P + S): ${right_side:.4f}")
print(f"Difference: ${abs(left_side - right_side):.6f}")

# Additional analysis
print(f"\n" + "-" * 60)
print("ANALYSIS:")
print("-" * 60)
print(f"• The put option is **in-the-money** (S < K: ${S} < ${K})")
print(f"• Intrinsic value of put: max(K-S, 0) = max(${K}-${S}, 0) = ${max(K-S, 0)}")
print(f"• Time value of put: ${put_price:.4f} - ${max(K-S, 0)} = ${put_price - max(K-S, 0):.4f}")
print(f"• The put is priced above intrinsic value due to time value")

# Compare with intrinsic values
call_intrinsic = max(S - K, 0)
put_intrinsic = max(K - S, 0)
print(f"\nIntrinsic Values:")
print(f"• Call intrinsic value: max(S-K, 0) = ${call_intrinsic}")
print(f"• Put intrinsic value: max(K-S, 0) = ${put_intrinsic}")
print(f"• Call time value: ${C} - ${call_intrinsic} = ${C - call_intrinsic}")
print(f"• Put time value: ${put_price:.4f} - ${put_intrinsic} = ${put_price - put_intrinsic:.4f}")
