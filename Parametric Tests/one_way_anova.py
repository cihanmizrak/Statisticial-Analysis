import numpy as np
import scipy.stats as ss
from tabulate import tabulate


def one_way_anova(x):
    N = []
    k = len(x)
    sums = []
    sumsq = []
    means = []
    group_bwl = 0 #between
    group_whl = 0 #within 
    if len(x)<3:
        print("At least three different groups required")
    else:
        for i in range(k):
            N.append(len(x[i]))     # N[n1,n2,n3,...,nn]
            sums.append(np.sum(x[i]))  
            sumsq.append((np.sum(x[i]))**2)
            means.append(np.mean(x[i]))
            group_whl += np.var(x[i])*k
        n = np.sum(N)
    
        totalmean = np.sum(sums) / n 
        
            
        for i in range(k):
            group_bwl += N[i]*((means[i]-totalmean)**2)
        
        group_bw = group_bwl/(k-1)
        group_wh = group_whl/(n-k)
        
        df1,df2 = k-1,n-k
        F = group_bw / group_wh
        t = [(group_bwl+group_whl),((k-1)+(n-k))]
        
        print(tabulate([['Between Groups', group_bwl,(k-1),group_bw,F], 
                        ['Wihtin Groups', group_whl,(n-k),group_wh,""],
                        ['Total',t[0],t[1],"",""]],  
                       headers=['','Sum of Squares', 'df','Mean Squares','F']))
        
        Ft = np.round(ss.f.ppf(0.05, df1, df2),4) #Ftable value
        
        if F>Ft:
            print(f"\n\nF test = {np.round(F,4)}\nF table = {Ft} \nWe can reject the null hypothesis.")
        else:
            print(f"\n\nF test = {np.round(F,4)}\nF table = {Ft} \nWe fail to reject the null hypothesis.")
            
#sample             
treat_times = [[47,32,63,54],[51,74,70],[68,46,49,53],[63,85,80,95,82]]
one_way_anova(treat_times)


#Output

#                  Sum of Squares    df  Mean Squares        F
#--------------  ----------------  ----  ------------------  -----------------
#Between Groups           2739        3  913.0               6.708850424559112
#Wihtin Groups            1633.07    12  136.08888888888887
#Total                    4372.07    15


#F test = 6.7089
#F table = 0.1144 
#You can reject the null hypothesis.
