#Computation in AI code

#Import packages
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Read data.
data = pd.read_csv(r'supercomputer-power-flops.csv')
x = np.array(data['Year'][9:28:2])
y = np.array(data['Floating-Point Operations per Second'][9:28:2])

#Plot computation from 2002 to 2020
plot1 = plt.plot(x,y,'o-')
plt.xlim(2002,2020)
plt.xlabel('Years')
plt.yscale('log')
plt.ylabel('FLOPS')
plt.title('Computational Power from 2002-2020')
plt.show()

#Coefficients for exponential regression
[a,b] = np.polyfit(x,np.log10(y),1)

#Plot regression upto 2050. Note that seaborn uses bootstrapping to 
#calculate confidence intervals. The 90% CI is represented by the blue shading
fig, trend = plt.subplots()
trend.set_xlim([2002,2050])
yticks=[10**i for i in range(12,27,2)]  #for yaxis to show actual value rather than logs 
yvalues=[np.format_float_scientific(i) for i in yticks]  #compress to scientific notation
sns.regplot(data=data,x=x,y=np.log10(y),truncate=False,ci=90,ax=trend)
trend.set(title='Computation estimate over the years')
trend.set(yticklabels=yvalues)
trend.set(xlabel='2002-2050')
trend.set(ylabel='FLOPS')

