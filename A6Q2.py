import math

# Given data
face_value = 100  # Assuming $100 face value (standard)
coupon_rate = 0.08  # 8% annual coupon
yield_rate = 0.11  # 11% continuously compounded yield
maturity = 5  # 5 years
annual_coupon = coupon_rate * face_value  # $8 per year

def bond_price_continuous(coupon, face_value, yield_rate, maturity):
    """Calculate bond price with continuous compounding"""
    price = 0
    
    # Present value of coupon payments (years 1-4)
    for t in range(1, maturity):
        pv_coupon = coupon * math.exp(-yield_rate * t)
        price += pv_coupon
    
    # Present value of final payment (coupon + principal at year 5)
    final_payment = coupon + face_value
    pv_final = final_payment * math.exp(-yield_rate * maturity)
    price += pv_final
    
    return price

def bond_duration_continuous(coupon, face_value, yield_rate, maturity, bond_price):
    """Calculate modified duration with continuous compounding"""
    weighted_time = 0
    
    # Weighted time for coupon payments (years 1-4)
    for t in range(1, maturity):
        pv_coupon = coupon * math.exp(-yield_rate * t)
        weighted_time += t * pv_coupon
    
    # Weighted time for final payment
    final_payment = coupon + face_value
    pv_final = final_payment * math.exp(-yield_rate * maturity)
    weighted_time += maturity * pv_final
    
    duration = weighted_time / bond_price
    return duration

# Part (a): Calculate bond price
print("=" * 60)
print("BOND PRICING ANALYSIS")
print("=" * 60)

bond_price = bond_price_continuous(annual_coupon, face_value, yield_rate, maturity)
print(f"\n(a) Bond Price Calculation:")
print(f"    Face Value: ${face_value}")
print(f"    Annual Coupon: ${annual_coupon} ({coupon_rate*100}%)")
print(f"    Yield: {yield_rate*100}% (continuously compounded)")
print(f"    Maturity: {maturity} years")

# Show detailed cash flow analysis
print(f"\n    Cash Flow Analysis:")
total_pv = 0
for t in range(1, maturity):
    pv = annual_coupon * math.exp(-yield_rate * t)
    total_pv += pv
    print(f"    Year {t}: Coupon ${annual_coupon} → PV = ${pv:.4f}")

# Final payment (coupon + principal)
final_pv = (annual_coupon + face_value) * math.exp(-yield_rate * maturity)
total_pv += final_pv
print(f"    Year {maturity}: Coupon + Principal ${annual_coupon + face_value} → PV = ${final_pv:.4f}")
print(f"\n    **Bond Price: ${bond_price:.4f}**")

# Part (b): Calculate duration
print(f"\n(b) Duration Calculation:")
duration = bond_duration_continuous(annual_coupon, face_value, yield_rate, maturity, bond_price)
print(f"    **Duration: {duration:.4f} years**")

# Part (c): Effect of 0.2% yield decrease
print(f"\n(c) Effect of 0.2% Yield Decrease:")
yield_change = -0.002  # -0.2%
price_change_approx = -duration * yield_change * bond_price
new_price_approx = bond_price + price_change_approx

print(f"    Original Yield: {yield_rate*100}%")
print(f"    New Yield: {(yield_rate + yield_change)*100}%")
print(f"    Duration-based price change: ${price_change_approx:.4f}")
print(f"    **Approximate new price: ${new_price_approx:.4f}**")

# Part (d): Recalculate with 10.8% yield
print(f"\n(d) Verification with 10.8% Yield:")
new_yield = 0.108  # 10.8%
new_bond_price = bond_price_continuous(annual_coupon, face_value, new_yield, maturity)
actual_price_change = new_bond_price - bond_price

print(f"    Recalculated bond price at {new_yield*100}% yield: ${new_bond_price:.4f}")
print(f"    Actual price change: ${actual_price_change:.4f}")
print(f"    Duration-predicted change: ${price_change_approx:.4f}")
print(f"    Difference: ${abs(actual_price_change - price_change_approx):.4f}")

# Verification
percent_error = abs(actual_price_change - price_change_approx) / abs(actual_price_change) * 100
print(f"    **Accuracy of duration approximation: {100-percent_error:.2f}%**")

# Summary table
print(f"\n" + "="*60)
print("SUMMARY")
print("="*60)
print(f"Bond Price (11% yield):        ${bond_price:.4f}")
print(f"Duration:                      {duration:.4f} years")
print(f"New Price (10.8% yield):       ${new_bond_price:.4f}")
print(f"Actual Price Change:           ${actual_price_change:.4f}")
print(f"Duration-Predicted Change:     ${price_change_approx:.4f}")
