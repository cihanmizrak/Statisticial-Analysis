import numpy as np
import scipy.stats as ss

#Paried Sample T-test is a statistical prodecure for examining or comparing the means of two samples.



#We want to compare or measure the amount of sleep, got by patients before and after taking soporific drugs to help them sleep.

#The null hypothesis
#Ho:(µ1 = µ2) Soporific, drug has no effect on the sleep duration of the patients.

#The alternative hypothesis
#H1:(µ1 ≠ µ2) Soporific, drug has effect on the sleep duration of the patients.


control = [8.0,7.1,6.5,6.7,7.2,5.4,4.7,8.1,6.3,4.8]
treatment = [9.9,7.9,7.6,6.8,7.1,9.9,10.5,9.7,10.9,8.2]

n = len(control)


#Where d is the avarage difference between the paried samples.
#The degrees of freedom is n-1.

d = []

for i in range(n):
    d.append(control[i]-treatment[i])

#standart error
s = np.std(d)
 
Th = np.abs(np.mean(d)/(s/(np.sqrt(n))))
table = np.abs(ss.t.ppf(0.025, n-1))


if Th>table :
    print(f"{Th} > {table}, we can reject the null hypothesis.")
    print("\n We can say there is a statistically significant difference in sleep duration caused by the soporific drug")
else:
    print(f"{Th} < {table}, we fail to reject the null hypothesis.")
    
    
    
#3.82054369738174 > 2.262157162740992, we can reject the null hypothesis.

 #We can say there is a statistically significant difference in sleep duration caused by the soporific drug