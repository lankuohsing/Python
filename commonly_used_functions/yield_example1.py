# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 10:45:24 2018

@author: lankuohsing
"""

# In[]


# In[]
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1
# In[]
for n in fab(5):
    print(n)