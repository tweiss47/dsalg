#!/usr/bin/env python
# coding: utf-8

# # Stock Prices

# You are given access to yesterday's stock prices for a single stock. The data is in the form of an array with the stock price in 30 minute intervals from 9:30 a.m EST opening to 4:00 p.m EST closing time. With this data, write a function that returns the maximum profit obtainable. You will need to buy before you can sell.
# 
# For example, suppose you have the following prices:
# 
# `prices = [3, 4, 7, 8, 6]`
# 
# >Note: This is a shortened array, just for the sake of example—a full set of prices for the day would have 13 elements (one price for each 30 minute interval betwen 9:30 and 4:00), as seen in the test cases further down in this notebook.
# 
# In order to get the maximum profit in this example, you would want to buy at a price of 3 and sell at a price of 8 to yield a maximum profit of 5. In other words, you are looking for the greatest possible difference between two numbers in the array.
# 
# Fill out the function below and run it against the test cases. Take into consideration the time complexity of your solution. 

# In[6]:


def max_returns(prices):
    """
    Calculate maxiumum possible return
    
    Args:
       prices(array): array of prices
    Returns:
       int: The maximum profit possible
    """
    if len(prices) < 2: return 0
    start = 0
    max_profit = prices[1] - prices[0]
    for i in range(2, len(prices)):
        profit = prices[i] - prices[start]
        if profit > max_profit:
            max_profit = profit
        elif profit < 0:
            start = i
    return max_profit


# <span class="graffiti-highlight graffiti-id_uc722im-id_o4cterg"><i></i><button>Show Solution</button></span>

# In[7]:


# Test Cases
def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# In[8]:


prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
test_case = [prices, solution]
test_function(test_case)


# In[9]:


prices = [54, 18, 37, 9, 11, 48, 23, 1, 7, 34, 2, 45, 67]
solution = 66
test_case = [prices, solution]
test_function(test_case)


# In[10]:


prices = [78, 54, 45, 37, 34, 23, 18, 12, 9, 9, 7, 2, 2]
solution = 0
test_case = [prices, solution]
test_function(test_case)


# In[ ]:




