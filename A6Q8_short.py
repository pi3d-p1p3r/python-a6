import numpy as np
import pandas as pd
from scipy.stats import norm

# Parameters
S, sigma, r = 32, 0.30, 0.05
T_6m, T_1y = 0.5, 1.0
stock_range = np.arange(15, 50, 1)

def bs_call(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)

def bs_put(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)

# Calculate option prices
calls_6m = {K: bs_call(S, K, T_6m, r, sigma) for K in [25, 30, 35]}
puts_6m = {K: bs_put(S, K, T_6m, r, sigma) for K in [25, 30]}
calls_1y = {K: bs_call(S, K, T_1y, r, sigma) for K in [25, 30, 35]}
puts_1y = {K: bs_put(S, K, T_1y, r, sigma) for K in [25, 30, 35]}

# Strategy costs
strategies = {
    'Bull_Spread': calls_6m[25] - calls_6m[30],
    'Bear_Spread': puts_6m[30] - puts_6m[25],
    'Butterfly_Call': calls_1y[25] + calls_1y[35] - 2*calls_1y[30],
    'Butterfly_Put': puts_1y[25] + puts_1y[35] - 2*puts_1y[30],
    'Straddle': calls_6m[30] + puts_6m[30],
    'Strangle': calls_6m[35] + puts_6m[25]
}

# Profit calculations
def calc_profits(S_T):
    return {
        'Bull_Spread': np.maximum(np.minimum(S_T - 25, 5), 0) - strategies['Bull_Spread'],
        'Bear_Spread': np.maximum(np.minimum(30 - S_T, 5), 0) - strategies['Bear_Spread'],
        'Butterfly_Call': np.where(S_T <= 25, -strategies['Butterfly_Call'],
                                 np.where(S_T <= 30, S_T - 25 - strategies['Butterfly_Call'],
                                         np.where(S_T <= 35, 35 - S_T - strategies['Butterfly_Call'], 
                                                 -strategies['Butterfly_Call']))),
        'Butterfly_Put': np.where(S_T <= 25, -strategies['Butterfly_Put'],
                                np.where(S_T <= 30, S_T - 25 - strategies['Butterfly_Put'],
                                        np.where(S_T <= 35, 35 - S_T - strategies['Butterfly_Put'], 
                                                -strategies['Butterfly_Put']))),
        'Straddle': np.abs(S_T - 30) - strategies['Straddle'],
        'Strangle': np.maximum(S_T - 35, 0) + np.maximum(25 - S_T, 0) - strategies['Strangle']
    }

# Generate results
profits = calc_profits(stock_range)
profit_df = pd.DataFrame({'Stock_Price': stock_range, **profits})

# Display results
print(f"Stock: ${S}, σ: {sigma*100}%, r: {r*100}%\n")

print("Strategy Costs:")
for name, cost in strategies.items():
    print(f"{name}: ${cost:.4f}")

print(f"\nProfit at Key Prices:")
selected = profit_df[profit_df['Stock_Price'].isin([20, 25, 30, 35, 40])]
print(selected.round(4).to_string(index=False))
