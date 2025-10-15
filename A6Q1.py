import numpy as np
import pandas as pd

FV_A=np.array([225,215,250,225,205])
FV_B=np.array([220,225,250,250,210])
t=np.array([1,2,3,4,5])
r=4.33/100

def PV(FV,t):
    df=np.exp(-r*t);
    pv=np.zeros_like(FV)
    for i in range(len(FV)):
        pv[i]=FV[i]*df[i]
    return df,pv

df_A,PV_A=PV(FV_A,t)
df_B,PV_B=PV(FV_B,t)

data={
    'Time (yrs)':t,
    'Discount Factor':df_A,
    'Future Cashflow (A)':FV_A,
    'Future Cashflow (B)':FV_B,
    'Present Value (A)':PV_A,
    'Present Value (B)':PV_B,
}
df=pd.DataFrame(data)
print(df)

print(f"The present value of the investment A is :",PV_A.sum())
print(f"The present value of the investment B is :",PV_B.sum())

if PV_A.sum()<PV_B.sum():    
    print(f"The investment B is better than A")
elif PV_B.sum()<PV_A.sum():
    print(f"The investment A is better than B")
else:
    print(f"The investment A is as benificial as B")
