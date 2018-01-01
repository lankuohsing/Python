# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 21:22:39 2017

@author: lankuohsing
"""

# In[]
import pandas as pd
import os
# In[]
xlsx_file1=pd.read_excel("excel_sample1.xlsx",sheetname=1,header=None)
# In[]
print(os.path.abspath(os.curdir))
