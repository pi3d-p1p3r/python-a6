import pandas as pd

# Given data
payments = [460, 235, 640, 370, 330, 250]  # Payments for years 1-6
years = [1, 2, 3, 4, 5, 6]  # Payment years
nominal_rate = 0.045  # 4.5% annual interest rate
compounding_frequency = 4  # Quarterly compounding

def calculate_effective_annual_rate(nominal_rate, frequency):
    """Calculate effective annual rate from nominal rate and compounding frequency"""
    return (1 + nominal_rate/frequency)**frequency - 1

def calculate_present_value(cash_flows, years, effective_rate):
    """Calculate present value of cash flows"""
    pv_list = []
    total_pv = 0
    
    print("Present Value Calculation Details:")
    print("=" * 60)
    print(f"{'Year':<6} {'Payment':<10} {'PV Factor':<12} {'Present Value':<15}")
    print("-" * 60)
    
    for i, (payment, year) in enumerate(zip(cash_flows, years)):
        pv_factor = 1 / (1 + effective_rate)**year
        present_value = payment * pv_factor
        pv_list.append(present_value)
        total_pv += present_value
        
        print(f"{year:<6} ${payment:<9} {pv_factor:<11.6f} ${present_value:<14.2f}")
    
    return total_pv, pv_list

# Calculate effective annual rate
effective_annual_rate = calculate_effective_annual_rate(nominal_rate, compounding_frequency)

print("PRESENT VALUE ANALYSIS")
print("=" * 60)
print(f"Nominal Interest Rate: {nominal_rate*100}% per annum")
print(f"Compounding Frequency: {compounding_frequency} times per year (quarterly)")
print(f"Effective Annual Rate: {effective_annual_rate:.6f} ({effective_annual_rate*100:.4f}%)")
print()

# Calculate present value
total_pv, individual_pvs = calculate_present_value(payments, years, effective_annual_rate)

print("=" * 60)
print(f"**TOTAL PRESENT VALUE: ${total_pv:.2f}**")
print("=" * 60)

# Create summary DataFrame
summary_df = pd.DataFrame({
    'Year': years,
    'Payment': payments,
    'Present Value': individual_pvs
})

print("\nSUMMARY TABLE:")
print(summary_df.round(2).to_string(index=False))

# Additional analysis
print(f"\nADDITION ANALYSIS:")
print(f"• Total future payments: ${sum(payments):,.2f}")
print(f"• Total present value: ${total_pv:,.2f}")
print(f"• Discount amount: ${sum(payments) - total_pv:,.2f}")
print(f"• Present value as % of future payments: {total_pv/sum(payments)*100:.2f}%")

# Verification calculation showing the quarterly compounding effect
quarterly_rate = nominal_rate / compounding_frequency
print(f"\nQUARTERLY COMPOUNDING VERIFICATION:")
print(f"• Quarterly rate: {quarterly_rate:.4f} ({quarterly_rate*100:.3f}%)")
print(f"• (1 + quarterly_rate)^4 = (1 + {quarterly_rate:.4f})^4 = {(1 + quarterly_rate)**4:.6f}")
print(f"• Effective annual rate = {(1 + quarterly_rate)**4:.6f} - 1 = {effective_annual_rate:.6f}")

# Show calculation formula
print(f"\nFORMULA USED:")
print(f"PV = Σ [Payment_t / (1 + r_eff)^t]")
print(f"where r_eff = (1 + {nominal_rate}/{compounding_frequency})^{compounding_frequency} - 1")
print(f"r_eff = {effective_annual_rate:.6f}")
