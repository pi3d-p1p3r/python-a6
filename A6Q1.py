import math

# Given data
interest_rate = 0.0433  # 4.33% annual interest rate
investment_A = [225, 215, 250, 225, 205]  # Cash flows for years 1-5
investment_B = [220, 225, 250, 250, 210]  # Cash flows for years 1-5
years = [1, 2, 3, 4, 5]

def calculate_npv_continuous(cash_flows, rate, time_periods):
    """
    Calculate NPV using continuous compounding formula: PV = FV * e^(-rt)
    """
    npv = 0
    for i, cash_flow in enumerate(cash_flows):
        t = time_periods[i]
        present_value = cash_flow * math.exp(-rate * t)
        npv += present_value
        print(f"Year {t}: Cash Flow = ${cash_flow:,.2f}, PV = ${present_value:,.2f}")
    return npv

# Calculate NPV for Investment A
print("Investment A Analysis:")
print("-" * 40)
npv_a = calculate_npv_continuous(investment_A, interest_rate, years)
print(f"Total NPV for Investment A: ${npv_a:,.2f}")

print("\n" + "="*50 + "\n")

# Calculate NPV for Investment B
print("Investment B Analysis:")
print("-" * 40)
npv_b = calculate_npv_continuous(investment_B, interest_rate, years)
print(f"Total NPV for Investment B: ${npv_b:,.2f}")

print("\n" + "="*50 + "\n")

# Compare investments
print("Investment Comparison:")
print("-" * 30)
print(f"Investment A NPV: ${npv_a:,.2f}")
print(f"Investment B NPV: ${npv_b:,.2f}")
print(f"Difference (B - A): ${npv_b - npv_a:,.2f}")

if npv_a > npv_b:
    print(f"\n**Investment A is preferable** by ${npv_a - npv_b:,.2f}")
elif npv_b > npv_a:
    print(f"\n**Investment B is preferable** by ${npv_b - npv_a:,.2f}")
else:
    print(f"\nBoth investments have equal NPV")

# Calculate the present value factors for reference
print(f"\nPresent Value Factors (e^(-rt)) for each year:")
for year in years:
    pv_factor = math.exp(-interest_rate * year)
    print(f"Year {year}: {pv_factor:.6f}")
