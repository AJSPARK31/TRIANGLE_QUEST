#!/usr/bin/env python
# coding: utf-8

# In[ ]:



# You are given a positive integer . Print a numerical triangle of height  like the one below:

# 1
# 22
# 333
# 4444
# 55555
# ......
# Can you do it using only arithmetic operations, a single for loop and print statement?

# triangle quest


n=int(input())
for i in range(1,n): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int(i*10**i/9))
    


# In[2]:





# In[ ]:




