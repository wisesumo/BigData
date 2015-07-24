import pandas as pd
import statsmodels.api as sm
import numpy as np
import requests, zipfile, StringIO

r = requests.get('https://resources.lendingclub.com/LoanStats3c.csv.zip')
z = zipfile.ZipFile(StringIO.StringIO(r.content))
loansData = pd.read_csv(z.open('LoanStats3c.csv'), nrows = 1000, skiprows=1)

subdata = pd.DataFrame(columns=['Interest.Rate', 'Annual.Income', 'Home'])
subdata['Interest.Rate'] = loansData.int_rate
subdata['Annual.Income'] = loansData.annual_inc.astype(float)
subdata['Home'] = loansData.home_ownership


#add the Statsmodels intercept column to the dataframe.
subdata['Intercept'] = float(1.0)

subdata.dropna(inplace=True)
subdata['Interest.Rate'] = map(lambda x: float(x.rstrip('%')), subdata['Interest.Rate'])



#monthly income model

print " Monthly Income Model "

model1 = sm.OLS(subdata['Interest.Rate'], subdata[['Intercept', 'Annual.Income']])
res1 = model1.fit()

print res1.summary()

subdata['Home'] = map(lambda x: 1*(x == "RENT") + 2*(x == "OWN"), subdata['Home'])



#monthly income and home ownership model

print " Monthly income and Home Ownership Model "

model2 = sm.OLS(subdata['Interest.Rate'], subdata[['Intercept', 'Annual.Income', 'Home']])
res2 = model2.fit()

print res2.summary()

subdata['Interaction'] = subdata['Annual.Income']*subdata['Home']




#model of the monthly income and home ownership and interaction

print " Model with monthly income, Home Ownership, and Interaction "

model3 = sm.OLS(subdata['Interest.Rate'], subdata[['Intercept', 'Annual.Income', 'Home', 'Interaction']])

res3 = model3.fit()

print res3.summary()
