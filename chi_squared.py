import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections

#load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#drop null values
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

k = 0
for i in freq:
	k = k+1

print "The number of unique elements in freq is", k

print "The most frequent number of open credit lines is", freq.most_common(1)[0][0]

plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show()

# do a Chi-Squared test:
chi, p = stats.chisquare(freq.values())

print "Data shows a chi-squared and a p-value of", chi, p
