t=5; y=11/100; r=8/100; FV=1000;    #Face Value
t_c=np.array([1,2,3,4,5])
coupon=1000*r*np.ones_like(t_c)
PV_coupon=coupon*np.exp(-y*t_c)
PV_FV=np.exp(-y*t)*FV
bond_value=PV_coupon.sum()+PV_FV
print(f"The bond value is : {bond_value:.3f}")

#Bond's Duration
bond_duration=(np.dot(PV_coupon,t_c)+PV_FV*t)/bond_value
print(f"The bond duration is : {bond_duration:.4f} years")

#Estimated price change 
dy=-0.2/100
dP=-bond_duration*bond_value*dy
bond_pred=dP+bond_value
print(f"Effect of Bond's price on a 0.2% decease in the Bond yield is {dP:0.4f}")
print(f"Hence the predicted bond's price becomes {bond_pred:0.3f}")

# Verification of estimation
y1=10.8/100
coupon1=1000*r*np.ones_like(t_c)
PV_coupon1=coupon1*np.exp(-y1*t_c)
bond_value1=PV_coupon1.sum()+np.exp(-y1*t)*FV
print(f"The bond value is after yield rate increased to 10.8% (actual) : {bond_value1:.3f}")
print(f"Comment : Since the differenve between predicted and actual bond value is ~{bond_pred-bond_value1:0.3f}, which is not too large, our approximation is valid")
