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
        avg = dataset[attribute].iloc[:i].mean()        #Could use Dynamic Programming here for optimization.
        mean.append(avg)
    return mean

mean = moving_average(dataset = sbin,moving_limit = 52, attribute = "Close")
print(mean)



def rolling_window(dataset, size, limit):
"""
displays data for all n consecutive entries in the dataset(where n = size), up untill the size(window size) is increased to a limit  
"""
    while size <= limit:
        end = size
        i = 0
        while end <= len(dataset.index):
            print(dataset.iloc[i:end])
            end+=1
            i+=1
        size+=1


rolling_window(sbin, 10, 75)


