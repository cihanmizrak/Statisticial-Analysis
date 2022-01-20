import numpy as np
import scipy.stats as ss

#"We want to compare the blood pressure of male consultant doctors with the junior resident female doctors we explored above.

#The null hypothesis 
#Ho : There is no significant between the blood pressures of male consultant doctors and junior resident female doctors.

#The alternative hypothesis
#H1 : There is a statistically significant between the blood pressures of male consultant doctors and junior resident female doctors.


female_doctor_bps = [128, 127, 118, 115, 144, 142, 133, 140, 132, 131,
                     111, 132, 149, 122, 139, 119, 136, 129, 126, 128]

male_consultant_bps = [118, 115, 112, 120, 24, 130, 123, 110, 120, 121,
                       123, 125, 129, 130, 112, 117, 119, 120, 123, 128]

#t test 

#female doctor's mean
x_1 = np.mean(female_doctor_bps)

#male consultant's mean
x_2 = np.mean(male_consultant_bps)

#female doctor's standart deviation 
s_1 = np.std(female_doctor_bps)

#male consultant's standart deviation
s_2 = np.std(male_consultant_bps)

#lenght female doctor's bps
n1 = len(female_doctor_bps)

#lenght male consultant's bps
n2 = len(male_consultant_bps)

s2 = (((n1-1)*(s_1)**2)+(n2-1)*((s_2)**2))/(n1+n2-2)

ttest = (x_1-x_2)/np.sqrt((s2)*((1/n1)+(1/n2)))

table = ss.t.ppf(0.05,n1+n2-2)
print(f"Critical value = {table}\nTest statistics = {ttest}")
if ttest>table :
    print(f"{ttest} > {table}, you can reject the null hypothesis.")
else:
    print(f"{ttest} < {table}, you fail to reject the null hypothesis.")

#Critical value = -1.6859544576438146
#Test statistics = 2.6367925362322158
#2.6367925362322158 > -1.6859544576438146, you can reject the null hypothesis.