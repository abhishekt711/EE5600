import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import binom
import seaborn as sns
import pandas as pd
sample_size=500
event_two_head=105
event_one_head=275
event_no_head=120
prob2=event_two_head/sample_size
prob1=event_one_head/sample_size
prob0=event_no_head/sample_size

data_binom = binom.rvs(n=2,p=0.5,size=500)


#Calculating the number of favourable outcomes
err_ind0 = np.nonzero(data_binom == 0)
#calculating the probability
err_n0 = np.size(err_ind0)/sample_size
#Calculating the number of favourable outcomes
err_ind1 = np.nonzero(data_binom == 1)
#calculating the probability
err_n1 = np.size(err_ind1)/sample_size
#Calculating the number of favourable outcomes
err_ind2 = np.nonzero(data_binom == 2)
#calculating the probability
err_n2 = np.size(err_ind2)/sample_size
#Theory vs simulation
print("Probability of Two Heads =",prob2,"\n","Probability of One Head =",prob1,"\n","Probability of No Head =", prob0)
print("Two Heads in random binomial distribution  =",np.size(err_ind2),"\n", "One Head in random binomial distribution  =",np.size(err_ind1),"\n","No Head in random binomial distribution =", np.size(err_ind0) )


print("Probability of Two Heads in random binomial distribution  =",err_n2,"\n", "Probability of One Head in random binomial distribution  =",err_n1,"\n","Probability of No Head in random binomial distribution =", err_n0)





sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(4.5,3)})
ax= sns.distplot(data_binom,
                 kde=False,
                 color="red",
                 hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial', ylabel='Frequency')
plt.show()
