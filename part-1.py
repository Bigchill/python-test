from nsepy import *
from datetime import *
from requests import *
from numpy import *
from pandas import *
from scipy import *
from lxml import *
 
sbin = get_history(symbol='SBIN',start=date(2018,1,1),end=date(2019,2,22))  #sample stock
print(sbin)
print(sbin["Close"])

def moving_average(dataset, moving_limit, attribute):
  """
  calculates moving averages for an attribute(closing price) for each stock and index. moving limit is set for how many weeks do we want to
  work on.
  """
    mean=[]
    for i in range(4, moving_limit+1, 12):
        avg = dataset[attribute].iloc[:i].mean()
        mean.append(avg)
    return mean

mean = moving_average(sbin, 52, "Close")
print(mean)


