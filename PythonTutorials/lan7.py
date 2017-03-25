# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 23:33:18 2017

@author: lankuohsing
"""

import os
for i in os.listdir('.'):
    if os.path.isdir(i):
        print (i)