import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#remove rows with null values
loansData.dropna(inplace=True)

#generate box plot of loan amounts
loansData.boxplot(column=['Amount.Funded.By.Investors' , 'Amount.Requested'])
plt.savefig('lendingclub-boxplot.pdf', format='pdf')

The box plot shows that the investors funded about $10000 on average

#generate histogram for loan amounts
loansData.hist(column=['Amount.Funded.By.Investors', 'Amount.Requested'], layout=(2,1))
plt.savefig('lendingclub-hist.pdf', format='pdf')

The histogram shows the distribution of funding.

plt.figure()
plt.subplot(211)
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.subplot(212)
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig('lendingclub-qq.pdf', format='pdf')

plt.show()

#the data shows abnormal distribution and is more concentrated on the tail end
#Comparing the Amount Requested and Amount Funded by the Investors shows:
# - The box plot shows the average for both quantities are the same.  Plus the amount funded at the third quartile is smaller.
# - The histogram shows that the two data sets have the same distribution. However, there is a slight decrease in the frequencies.
# - The QQ plot shows that the distributions are similar, there is no preference by investors for smaller or higher deals.
