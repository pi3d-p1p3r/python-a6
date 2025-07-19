import numpy as np
import matplotlib.pyplot as plt

# Parameters
K = 150  # Strike price
premium = 5  # Option premium
S = np.arange(100, 200, 1)  # Stock price range

# Profit functions
def long_call_profit(S, K, premium):
    return np.maximum(S - K, 0) - premium

def short_call_profit(S, K, premium):
    return -np.maximum(S - K, 0) + premium

def long_put_profit(S, K, premium):
    return np.maximum(K - S, 0) - premium

def short_put_profit(S, K, premium):
    return -np.maximum(K - S, 0) + premium

# Calculate profits
long_call = long_call_profit(S, K, premium)
short_call = short_call_profit(S, K, premium)
long_put = long_put_profit(S, K, premium)
short_put = short_put_profit(S, K, premium)

# Create plots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle(f'Options Profit Diagrams (K=${K}, Premium=${premium})', fontweight='bold')

# Plot each option
plots = [
    (ax1, long_call, 'Long Call', 'blue'),
    (ax2, short_call, 'Short Call', 'red'),
    (ax3, long_put, 'Long Put', 'green'),
    (ax4, short_put, 'Short Put', 'purple')
]

for ax, profit, title, color in plots:
    ax.plot(S, profit, color=color, linewidth=2)
    ax.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    ax.axvline(x=K, color='gray', linestyle='--', alpha=0.5)
    ax.set_title(title)
    ax.set_xlabel('Stock Price ($)')
    ax.set_ylabel('Profit ($)')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Summary
print("Options Analysis Summary:")
print(f"Strike Price: ${K}, Premium: ${premium}")
print("\nBreakeven Points:")
print(f"Long Call:  ${K + premium}")
print(f"Short Call: ${K + premium}")
print(f"Long Put:   ${K - premium}")
print(f"Short Put:  ${K - premium}")

print(f"\nMax Profit/Loss:")
print(f"Long Call:  Max Loss = ${premium}, Max Profit = Unlimited")
print(f"Short Call: Max Profit = ${premium}, Max Loss = Unlimited")
print(f"Long Put:   Max Loss = ${premium}, Max Profit = ${K - premium}")
print(f"Short Put:  Max Profit = ${premium}, Max Loss = ${K - premium}")
