import numpy as np
import pandas as pd
from scipy.stats import norm
import math

# Given parameters
S = 32      # Current stock price
sigma = 0.30 # Volatility (30%)
r = 0.05    # Risk-free rate (5% per annum)

def black_scholes_call(S, K, T, r, sigma):
    """Calculate European call option price using Black-Scholes formula"""
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    call_price = S*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
    return call_price

def black_scholes_put(S, K, T, r, sigma):
    """Calculate European put option price using Black-Scholes formula"""
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    put_price = K*np.exp(-r*T)*norm.cdf(-d2) - S*norm.cdf(-d1)
    return put_price

# Stock price range for profit calculations
stock_range = np.arange(15, 50, 1)

print("=" * 80)
print("EUROPEAN OPTIONS STRATEGIES - COSTS AND PROFIT ANALYSIS")
print("=" * 80)
print(f"Stock Price: ${S}, Volatility: {sigma*100}%, Risk-free Rate: {r*100}%")
print("=" * 80)

# (a) Bull Spread using European call options (K=$25, $30, T=6 months)
print("\n(a) BULL SPREAD USING CALLS (K=$25, $30, T=6 months)")
print("-" * 60)
T_6m = 6/12  # 6 months = 0.5 years

call_25_6m = black_scholes_call(S, 25, T_6m, r, sigma)
call_30_6m = black_scholes_call(S, 30, T_6m, r, sigma)

bull_spread_cost = call_25_6m - call_30_6m  # Long $25 call, Short $30 call
print(f"Call option (K=$25): ${call_25_6m:.4f}")
print(f"Call option (K=$30): ${call_30_6m:.4f}")
print(f"**Bull Spread Cost: ${bull_spread_cost:.4f}**")

# Bull spread profit calculation
def bull_spread_profit(S_T, K1, K2, net_cost):
    return np.maximum(np.minimum(S_T - K1, K2 - K1), 0) - net_cost

bull_profits = bull_spread_profit(stock_range, 25, 30, bull_spread_cost)

# (b) Bear Spread using European put options (K=$25, $30, T=6 months)
print("\n(b) BEAR SPREAD USING PUTS (K=$25, $30, T=6 months)")
print("-" * 60)

put_25_6m = black_scholes_put(S, 25, T_6m, r, sigma)
put_30_6m = black_scholes_put(S, 30, T_6m, r, sigma)

bear_spread_cost = put_30_6m - put_25_6m  # Long $30 put, Short $25 put
print(f"Put option (K=$25): ${put_25_6m:.4f}")
print(f"Put option (K=$30): ${put_30_6m:.4f}")
print(f"**Bear Spread Cost: ${bear_spread_cost:.4f}**")

# Bear spread profit calculation
def bear_spread_profit(S_T, K1, K2, net_cost):
    return np.maximum(np.minimum(K2 - S_T, K2 - K1), 0) - net_cost

bear_profits = bear_spread_profit(stock_range, 25, 30, bear_spread_cost)

# (c) Butterfly Spread using European call options (K=$25, $30, $35, T=1 year)
print("\n(c) BUTTERFLY SPREAD USING CALLS (K=$25, $30, $35, T=1 year)")
print("-" * 60)
T_1y = 1.0  # 1 year

call_25_1y = black_scholes_call(S, 25, T_1y, r, sigma)
call_30_1y = black_scholes_call(S, 30, T_1y, r, sigma)
call_35_1y = black_scholes_call(S, 35, T_1y, r, sigma)

butterfly_call_cost = call_25_1y + call_35_1y - 2*call_30_1y
print(f"Call option (K=$25): ${call_25_1y:.4f}")
print(f"Call option (K=$30): ${call_30_1y:.4f}")
print(f"Call option (K=$35): ${call_35_1y:.4f}")
print(f"**Butterfly Call Cost: ${butterfly_call_cost:.4f}**")

# Butterfly spread profit calculation
def butterfly_profit(S_T, K1, K2, K3, net_cost):
    profit = np.where(S_T <= K1, -net_cost,
                     np.where(S_T <= K2, S_T - K1 - net_cost,
                             np.where(S_T <= K3, K3 - S_T - net_cost, -net_cost)))
    return profit

butterfly_call_profits = butterfly_profit(stock_range, 25, 30, 35, butterfly_call_cost)

# (d) Butterfly Spread using European put options (K=$25, $30, $35, T=1 year)
print("\n(d) BUTTERFLY SPREAD USING PUTS (K=$25, $30, $35, T=1 year)")
print("-" * 60)

put_25_1y = black_scholes_put(S, 25, T_1y, r, sigma)
put_30_1y = black_scholes_put(S, 30, T_1y, r, sigma)
put_35_1y = black_scholes_put(S, 35, T_1y, r, sigma)

butterfly_put_cost = put_25_1y + put_35_1y - 2*put_30_1y
print(f"Put option (K=$25): ${put_25_1y:.4f}")
print(f"Put option (K=$30): ${put_30_1y:.4f}")
print(f"Put option (K=$35): ${put_35_1y:.4f}")
print(f"**Butterfly Put Cost: ${butterfly_put_cost:.4f}**")

butterfly_put_profits = butterfly_profit(stock_range, 25, 30, 35, butterfly_put_cost)

# (e) Straddle using options (K=$30, T=6 months)
print("\n(e) STRADDLE (K=$30, T=6 months)")
print("-" * 60)

straddle_cost = call_30_6m + put_30_6m
print(f"Call option (K=$30): ${call_30_6m:.4f}")
print(f"Put option (K=$30): ${put_30_6m:.4f}")
print(f"**Straddle Cost: ${straddle_cost:.4f}**")

# Straddle profit calculation
def straddle_profit(S_T, K, net_cost):
    return np.maximum(S_T - K, 0) + np.maximum(K - S_T, 0) - net_cost

straddle_profits = straddle_profit(stock_range, 30, straddle_cost)

# (f) Strangle using options (K=$25, $35, T=6 months)
print("\n(f) STRANGLE (K=$25, $35, T=6 months)")
print("-" * 60)

call_35_6m = black_scholes_call(S, 35, T_6m, r, sigma)
strangle_cost = call_35_6m + put_25_6m
print(f"Call option (K=$35): ${call_35_6m:.4f}")
print(f"Put option (K=$25): ${put_25_6m:.4f}")
print(f"**Strangle Cost: ${strangle_cost:.4f}**")

# Strangle profit calculation
def strangle_profit(S_T, K1, K2, net_cost):
    return np.maximum(S_T - K2, 0) + np.maximum(K1 - S_T, 0) - net_cost

strangle_profits = strangle_profit(stock_range, 25, 35, strangle_cost)

# Create comprehensive profit tables
print("\n" + "=" * 80)
print("PROFIT TABLES FOR ALL STRATEGIES")
print("=" * 80)

# Create DataFrame with all profits
profit_df = pd.DataFrame({
    'Stock_Price': stock_range,
    'Bull_Spread': bull_profits,
    'Bear_Spread': bear_profits,
    'Butterfly_Call': butterfly_call_profits,
    'Butterfly_Put': butterfly_put_profits,
    'Straddle': straddle_profits,
    'Strangle': strangle_profits
})

# Display selected rows
selected_prices = [20, 25, 27, 30, 32, 35, 40, 45]
display_df = profit_df[profit_df['Stock_Price'].isin(selected_prices)]

print("\nProfit Analysis at Key Stock Prices:")
print(display_df.round(4).to_string(index=False))

# Summary of strategy costs
print("\n" + "=" * 80)
print("STRATEGY COST SUMMARY")
print("=" * 80)
summary_data = {
    'Strategy': ['Bull Spread (Calls)', 'Bear Spread (Puts)', 'Butterfly (Calls)', 
                 'Butterfly (Puts)', 'Straddle', 'Strangle'],
    'Cost': [bull_spread_cost, bear_spread_cost, butterfly_call_cost, 
             butterfly_put_cost, straddle_cost, strangle_cost],
    'Max_Profit': [5 - bull_spread_cost, 5 - bear_spread_cost, 
                   5 - butterfly_call_cost, 5 - butterfly_put_cost,
                   'Unlimited', 'Unlimited'],
    'Max_Loss': [bull_spread_cost, bear_spread_cost, butterfly_call_cost,
                 butterfly_put_cost, straddle_cost, strangle_cost]
}

summary_df = pd.DataFrame(summary_data)
print(summary_df.round(4).to_string(index=False))

# Additional analysis
print("\n" + "=" * 80)
print("KEY OBSERVATIONS")
print("=" * 80)
print(f"• Current stock price (${S}) is close to middle strikes")
print(f"• Bull and bear spreads have limited risk/reward profiles")
print(f"• Butterfly spreads profit when stock stays near ${30}")
print(f"• Straddle and strangle profit from high volatility")
print(f"• All costs calculated using Black-Scholes with σ={sigma*100}%, r={r*100}%")
