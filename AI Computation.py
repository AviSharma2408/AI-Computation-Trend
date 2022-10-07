# Computation in AI code

# Import packages
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Read the data and select relevant data points
data = pd.read_csv(r'C:\Users\sharm\Desktop\supercomputer-power-flops.csv')
x = np.array(data['Year'][0:28:3])
y = np.array(data['Floating-Point Operations per Second'][0:28:3])

# Plot computation from 2002 to 2020
plot1 = plt.plot(x, y, 'o-')
plt.xlim(1993,2020)
plt.xlabel('Years')
plt.yscale('log')
plt.ylabel('FLOPS')
plt.title('Computational Capacity from 1993-2020')
plt.show()

#Coefficients for the regression equation
[a, b] = np.polyfit(x, np.log10(y), 1)


# Function that estimates compute given the year as input
def comp_est(x):
    est = 10**(a*x+b)
    est = "{:e}".format(est)
    return est

# Plot regression upto 2030. Note that seaborn uses bootstrapping to
# calculate confidence intervals. The 90% CI is represented by the blue shading
fig, trend = plt.subplots()
trend.set_xlim([1993, 2030])
yticks=[10**i for i in range(10,22,2)]  #for yaxis to show actual value rather than logs
yvalues=[np.format_float_scientific(i) for i in yticks]  #compress to scientific notation
sns.regplot(data=data, x=x, y=np.log10(y), truncate=False, ci=90, ax=trend)
trend.set(title='Computational Capacity Prediction ')
trend.set(yticklabels=yvalues)
trend.set(xlabel='1993-2030')
trend.set(ylabel='FLOPS')


