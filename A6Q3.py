import numpy as np
import pandas as pd
r=4.5/100
n=4
t=np.array([1,2,3,4,5,6])
FV=np.array([460,235,640,370,330,250])
df=(1+(r/n))**(-n*t)
PV=np.zeros_like(FV)
PV=df*FV

data={
    'time(years)':t,
    'Discount Factor':df,
    'Cashflows ':FV,
    'Present value of the Cashflows':PV
}
df=pd.DataFrame(data)
print(df)
print(f'The present value of the investment : {PV.sum():0.4f}')
