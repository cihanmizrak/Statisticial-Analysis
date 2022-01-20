import numpy as np
import scipy.stats as ss
data = [128,118,144,133,132,111,148,139,136,
        126,127,115,142,140,131,132,122,119,129,128]

s = np.std(data,ddof = 1) 

mu = 120 #mean of the population 
alpha = 0.05 #significant level
x = np.mean(data) #mean of the sample
n = len(data) 


Th = (x-mu)/(s/np.sqrt(n)) 


table = ss.t.ppf(1-alpha,n-1)

if Th>table :
    print(f"{Th} > {table}, you can reject the null hypothesis.")
else:
    print(f"{Th} < {table}, you fail to reject the null hypothesis.")

#Output
# 4.53462 > 1.72913, you can reject the null hypothesis.

