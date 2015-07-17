import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Remove the '%' symbols from the Interest.Rate column.
loansData['Interest.Rate'] = map(lambda x: float(x.rstrip('%')), loansData['Interest.Rate'])

#Remove the word 'months' from the Loan.Length column.
loansData['Loan.Length'] = map(lambda x: int(x.rstrip('months')), loansData['Loan.Length'])

#Convert FICO scores into a numerical value, and save it in a new column called FICO.Score. Since the ranges are small, we're going to go ahead and pick the first number to represent the range.
loansData['FICO.Score'] = loansData['FICO.Range'].astype('string')

loansData['FICO.Score'] = map(lambda x: int(x.split("-")[0]), loansData['FICO.Score']) 

import matplotlib.pyplot as plt

plt.figure()
p = loansData['FICO.Score'].hist()

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
#plt.show()

#NOTE: a Gaussian distribution (also called a normal distribution, a Gaussian distribution is the classic symmetric "bell curve

import numpy as np
import statsmodels.api as sm

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()


print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared


loansData.to_csv('loansData_clean.csv', header=True, index=False)
