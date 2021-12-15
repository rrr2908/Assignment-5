#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Write a Python class to implement pow(x, n)
class oops:
    def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x
        elif x == -1:
            if n%2 == 0:
                return 1
            elif n%2 == 1:
                return -1
        elif n ==0:
            return 1
        elif n<0:
            return 1/self.pow(x,-n)
        value = self.pow(x,n//2)
        if n%2 == 0:
            return value*value
        return value*value*x
x = int(input("Enter the value of x:"))
n = int(input("Enter the value of n:"))
print(oops().pow(x,n))


# In[ ]:




