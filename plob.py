import collections
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from matplotlib.backends.backend_pdf import PdfPages

#Data list
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(x)
print c

# calculate number instances in list
count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

#boxplot results 
p1 = plt.figure(1)
plt.boxplot(x)
plt.title('BoxPlot')
p1.savefig('prob-boxplot.pdf', format='pdf')

#Historgram results
p2 = plt.figure(2)
plt.hist(x)
plt.title('Historgram')
p2.savefig('prob-hist.pdf', format='pdf')

#QQ Plot results
p3 = plt.figure(3)
stats.probplot(x, dist="norm", plot=plt)
p3.savefig('prob-qq.pdf', format='pdf')

# display results
plt.show()


