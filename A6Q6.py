import numpy as np
import matplotlib.pyplot as plt

# Given parameters
call_strike = 45  # Call strike price
put_strike = 40   # Put strike price
call_premium = 3  # Call option cost
put_premium = 4   # Put option cost
total_premium = call_premium + put_premium  # Total cost

# Create stock price range
stock_prices = np.arange(20, 70, 1)

def long_strangle_profit(S, call_strike, put_strike, call_premium, put_premium):
    """Calculate profit for long strangle strategy"""
    call_profit = np.maximum(S - call_strike, 0) - call_premium
    put_profit = np.maximum(put_strike - S, 0) - put_premium
    total_profit = call_profit + put_profit
    return total_profit, call_profit, put_profit

# Calculate profits
total_profit, call_profit, put_profit = long_strangle_profit(
    stock_prices, call_strike, put_strike, call_premium, put_premium
)

# Create the plot
plt.figure(figsize=(12, 8))

# Plot individual option profits
plt.subplot(2, 1, 1)
plt.plot(stock_prices, call_profit, 'b--', linewidth=2, label=f'Long Call (K=${call_strike})')
plt.plot(stock_prices, put_profit, 'r--', linewidth=2, label=f'Long Put (K=${put_strike})')
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
plt.axvline(x=call_strike, color='blue', linestyle=':', alpha=0.5)
plt.axvline(x=put_strike, color='red', linestyle=':', alpha=0.5)
plt.title('Individual Option Profits', fontweight='bold')
plt.xlabel('Stock Price ($)')
plt.ylabel('Profit ($)')
plt.legend()
plt.grid(True, alpha=0.3)

# Plot combined strategy profit
plt.subplot(2, 1, 2)
plt.plot(stock_prices, total_profit, 'g-', linewidth=3, label='Long Strangle Strategy')
plt.axhline(y=0, color='black', linestyle='-', alpha=0.5)
plt.axvline(x=call_strike, color='blue', linestyle=':', alpha=0.5, label=f'Call Strike ${call_strike}')
plt.axvline(x=put_strike, color='red', linestyle=':', alpha=0.5, label=f'Put Strike ${put_strike}')

# Mark breakeven points
lower_breakeven = put_strike - total_premium
upper_breakeven = call_strike + total_premium
plt.axvline(x=lower_breakeven, color='orange', linestyle='--', alpha=0.7, label=f'Breakeven ${lower_breakeven}')
plt.axvline(x=upper_breakeven, color='orange', linestyle='--', alpha=0.7, label=f'Breakeven ${upper_breakeven}')

# Mark maximum loss
plt.axhline(y=-total_premium, color='purple', linestyle=':', alpha=0.7, label=f'Max Loss -${total_premium}')

plt.title('Long Strangle Strategy - Total Profit', fontweight='bold', fontsize=14)
plt.xlabel('Stock Price ($)')
plt.ylabel('Profit ($)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Analysis and key points
print("=" * 60)
print("LONG STRANGLE STRATEGY ANALYSIS")
print("=" * 60)
print(f"Call Option: Strike = ${call_strike}, Premium = ${call_premium}")
print(f"Put Option:  Strike = ${put_strike}, Premium = ${put_premium}")
print(f"Total Premium Paid: ${total_premium}")

print("\n" + "-" * 60)
print("PROFIT ZONES:")
print("-" * 60)

print(f"\n1. Stock Price ≤ ${put_strike}:")
print(f"   - Put exercised, Call expires worthless")
print(f"   - Profit = (${put_strike} - S) - ${total_premium} = ${put_strike - total_premium} - S")

print(f"\n2. ${put_strike} < Stock Price < ${call_strike}:")
print(f"   - Both options expire worthless")
print(f"   - Profit = -${total_premium} (Maximum Loss)")

print(f"\n3. Stock Price ≥ ${call_strike}:")
print(f"   - Call exercised, Put expires worthless") 
print(f"   - Profit = (S - ${call_strike}) - ${total_premium} = S - ${call_strike + total_premium}")

print("\n" + "-" * 60)
print("KEY METRICS:")
print("-" * 60)
print(f"Lower Breakeven Point: ${lower_breakeven}")
print(f"Upper Breakeven Point: ${upper_breakeven}")
print(f"Maximum Loss: ${total_premium} (when ${put_strike} < S < ${call_strike})")
print(f"Maximum Profit: Unlimited (when S → 0 or S → ∞)")

# Verify breakeven calculations
sample_prices = [lower_breakeven, upper_breakeven]
for price in sample_prices:
    profit, _, _ = long_strangle_profit(price, call_strike, put_strike, call_premium, put_premium)
    print(f"Profit at S=${price}: ${profit:.2f}")

print("\n" + "=" * 60)
print("STRATEGY SUMMARY:")
print("This is a LONG STRANGLE - profitable when stock moves significantly")
print("in either direction beyond the breakeven points.")
print("=" * 60)
