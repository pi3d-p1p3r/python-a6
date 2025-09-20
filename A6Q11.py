import math
import matplotlib.pyplot as plt

S0, K, r, q, sg, T, n = 484, 480, 0.10, 0.03, 0.25, 2/12, 4
dt = T/n 
u, d = math.exp(sg*(dt)**0.5), math.exp(-sg*(dt)**0.5)
p, disc = (math.exp((r-q)*dt)-d)/(u-d), math.exp(-r*dt)

print(f"u={u:.3f}, d={d:.3f}, p={p:.3f}")

# Tree: S = Stock price, P = Put option price
S = {(i,j): S0*u**(i-j)*d**j for i in range(n+1) for j in range(i+1)}
P = {(n,j): max(0, K-S[n,j]) for j in range(n+1)}

# Backward induction
for i in range(n-1, -1, -1):
    for j in range(i+1):
        cont = disc * (p*P[i+1,j] + (1-p)*P[i+1,j+1])
        exercise = max(0, K-S[i,j])
        P[i,j] = max(cont, exercise)

print(f"American Put: ${P[0,0]:.3f}")

# Plotting
plt.figure(figsize=(10,6))
for i in range(n+1):
    for j in range(i+1):
        x, y = i, i-2*j
        if i<n: 
            plt.plot([x,x+1], [y,y+1], 'k-', alpha=0.2)
            plt.plot([x,x+1], [y,y-1], 'k-', alpha=0.2)
        
        color = 'lightgreen' if j==0 else 'lightcoral' if j==i else 'lightyellow'
        plt.scatter(x, y, s=300, c=color, edgecolors='black')
        
        # Stock price: above
        plt.text(x, y+0.3, f'S={S[i,j]:.0f}', ha='center', fontweight='bold', fontsize=9)
        # Put value: below  
        plt.text(x, y-0.4, f'P={P[i,j]:.1f}', ha='center', fontsize=8)

plt.title('American Put Option Tree')
plt.xlabel('Time Step')
plt.grid(alpha=0.3)
plt.ylim(-(n+2), n+2)  # Extended y-limits for external text
plt.tight_layout()
plt.show()
