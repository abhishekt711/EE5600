import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import binom
import seaborn as sns
sample_size=500
event_two_head=105
event_one_head=275
event_no_head=120
prob2=event_two_head/sample_size
prob1=event_one_head/sample_size
prob0=event_no_head/sample_size

data_binom = binom.rvs(n=2,p=0.5,size=500)




#Theory vs simulation
print("Probability of Two Heads =",prob2,"\n","Probability of One Head =",prob1,"\n","Probability of No Head =", prob0)

sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize':(4.5,3)})
ax= sns.distplot(data_binom,
                 kde=False,
                 color="red",
                 hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial', ylabel='Frequency')
plt.show()
