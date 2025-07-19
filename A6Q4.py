import math

# Given parameters
S0 = 40      # Initial stock price
r = 0.10     # Risk-free rate (10% per annum, continuously compounded)
T = 1.0      # Time to maturity (1 year)

print("=" * 70)
print("FORWARD CONTRACT ANALYSIS - NON-DIVIDEND-PAYING STOCK")
print("=" * 70)
print(f"Initial Stock Price (S₀): ${S0}")
print(f"Risk-free Rate (r): {r*100}% per annum (continuous compounding)")
print(f"Contract Maturity (T): {T} year")

# Part (a): Initial forward price and value
print(f"\n(a) AT CONTRACT INCEPTION (t = 0)")
print("-" * 50)

def forward_price_continuous(stock_price, risk_free_rate, time_to_maturity):
    """Calculate forward price with continuous compounding"""
    return stock_price * math.exp(risk_free_rate * time_to_maturity)

def forward_contract_value(current_stock_price, agreed_forward_price, risk_free_rate, time_remaining):
    """Calculate value of existing forward contract"""
    return current_stock_price - agreed_forward_price * math.exp(-risk_free_rate * time_remaining)

# Calculate initial forward price
F0 = forward_price_continuous(S0, r, T)
initial_value = 0  # Forward contract value at inception is always zero

print(f"Forward Price Calculation:")
print(f"F₀ = S₀ × e^(r×T)")
print(f"F₀ = ${S0} × e^({r} × {T})")
print(f"F₀ = ${S0} × e^{r*T:.4f}")
print(f"F₀ = ${S0} × {math.exp(r*T):.6f}")
print(f"**Forward Price (F₀): ${F0:.4f}**")

print(f"\nInitial Contract Value:")
print(f"**Initial Value: ${initial_value}** (always zero at inception)")

# Part (b): 6 months later
print(f"\n(b) SIX MONTHS LATER (t = 0.5)")
print("-" * 50)

t = 0.5      # Current time (6 months = 0.5 years)
S1 = 45      # Stock price after 6 months
T_remaining = T - t  # Remaining time to maturity

print(f"Current Stock Price (S₁): ${S1}")
print(f"Time Elapsed: {t} years")
print(f"Remaining Time to Maturity: {T_remaining} years")
print(f"Risk-free Rate: {r*100}% (unchanged)")

# New forward price for a contract starting now with 6 months to maturity
F1 = forward_price_continuous(S1, r, T_remaining)

print(f"\nNew Forward Price (for 6-month contract starting now):")
print(f"F₁ = S₁ × e^(r×T_remaining)")
print(f"F₁ = ${S1} × e^({r} × {T_remaining})")
print(f"F₁ = ${S1} × e^{r*T_remaining:.4f}")
print(f"F₁ = ${S1} × {math.exp(r*T_remaining):.6f}")
print(f"**New Forward Price: ${F1:.4f}**")

# Value of existing forward contract
contract_value = forward_contract_value(S1, F0, r, T_remaining)

print(f"\nValue of Existing Forward Contract:")
print(f"V = S₁ - K × e^(-r×T_remaining)")
print(f"V = ${S1} - ${F0:.4f} × e^(-{r} × {T_remaining})")
print(f"V = ${S1} - ${F0:.4f} × e^{-r*T_remaining:.4f}")
print(f"V = ${S1} - ${F0:.4f} × {math.exp(-r*T_remaining):.6f}")
print(f"V = ${S1} - ${F0 * math.exp(-r*T_remaining):.4f}")
print(f"**Contract Value: ${contract_value:.4f}**")

# Summary and interpretation
print(f"\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"(a) At Contract Inception:")
print(f"    Forward Price: ${F0:.2f}")
print(f"    Contract Value: ${initial_value:.2f}")

print(f"\n(b) After 6 Months:")
print(f"    New Forward Price (6-month contract): ${F1:.2f}")
print(f"    Existing Contract Value: ${contract_value:.2f}")

print(f"\n" + "=" * 70)
print("INTERPRETATION")
print("=" * 70)

if contract_value > 0:
    print(f"• The existing forward contract has a **positive value** of ${contract_value:.2f}")
    print(f"• This represents a **gain** for the long position holder")
    print(f"• The stock price increased from ${S0} to ${S1}, benefiting the long position")
elif contract_value < 0:
    print(f"• The existing forward contract has a **negative value** of ${abs(contract_value):.2f}")
    print(f"• This represents a **loss** for the long position holder")
    print(f"• The stock price movement was unfavorable for the long position")
else:
    print(f"• The existing forward contract has **zero value**")
    print(f"• No gain or loss for the long position holder")

print(f"\n• **Forward price difference**: ${F1:.2f} - ${F0:.2f} = ${F1 - F0:.2f}")
print(f"• The new 6-month forward price is higher due to the increased stock price")

# Verification
print(f"\n" + "=" * 70)
print("VERIFICATION")
print("=" * 70)
print(f"Discount factor for 6 months: e^(-r×0.5) = e^(-{r*T_remaining:.4f}) = {math.exp(-r*T_remaining):.6f}")
print(f"Present value of original forward price: ${F0:.4f} × {math.exp(-r*T_remaining):.6f} = ${F0 * math.exp(-r*T_remaining):.4f}")
print(f"Contract value = Current stock - PV of forward = ${S1} - ${F0 * math.exp(-r*T_remaining):.4f} = ${contract_value:.4f}")
