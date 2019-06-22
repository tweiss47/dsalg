#!/usr/bin/env python
# coding: utf-8

# # Coin Change
# 
# You are given coins of different denominations and a total amount of money. Write a function to compute the fewest coins needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.
# 
# As an example:
# * Input: `coins = [1, 2, 3]`, `amount = 6`
# * Output: `2`
# * Explanation: The output is `2` because we can use `2` coins with value `3`. That is, `6 = 3 + 3`. We could also use `3` coins with value `2` (that is, `6 = 2 + 2 + 2`), but this would use more coins—and the problem specifies we should use the smallest number of coins possible.
# 
# There's test code below that you can use to check your solution. And at the bottom of the notebook, you'll find two different possible solutions.

# In[1]:


# this is assuming that the coins are in descending order - so if not then we would need to sort them
# this acutally kind of seems better than the dynamic options

def coin_change(coins, amount):
    # This should return one value: the fewest coins needed to make up the given amount
    coins.sort()
    coin_count = 0
    coin_index = len(coins) - 1
    while amount > 0 and coin_index >= 0:
        if coins[coin_index] <= amount:
            amount -= coins[coin_index]
            coin_count += 1
        else:
            coin_index -= 1
    return coin_count if amount == 0 else -1


# In[83]:


# if the coins are not sorted and we don't want to sort them, then we need to consider all
# the possibilities

def coin_change(coins, amount):
    # keep track of intermediate results
    lookup = {}

    # recursively compute the number of coins needed
    def coin_change(left):
        # base cases use inf to indicate an uncalculable result so min will work
        if left < 0: return float("inf")
        if left == 0: return 0

        # if result not calulated already, calculate for each of the possible choices
        if left not in lookup:
            lookup[left] = min(coin_change(left - coin) + 1 for coin in coins)
        return lookup[left]
    
    count = coin_change(amount)
    return count if count != float("inf") else -1


# In[84]:


def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# In[85]:


arr = [1,2,5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)


# In[86]:


arr = [4,5,6]
amount = 23
solution = 4
test_case = [arr, amount, solution]
test_function(test_case)


# In[87]:


arr = [5,7,8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)


# ## Solutions
# 
# Let's look at two different solutions. Here's one way to do it...
# 
# <span class="graffiti-highlight graffiti-id_jjdrdzm-id_fpk926y"><i></i><button>Show Solution One</button></span>

# And here's another possibility:
# 
# <span class="graffiti-highlight graffiti-id_bmrwntc-id_9z3z0e0"><i></i><button>Show Solution Two</button></span>
