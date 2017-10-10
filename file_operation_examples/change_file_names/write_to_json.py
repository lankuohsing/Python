# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:42:08 2017

@author: languoxing
"""

import json
import time



def store(data):
    with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(data))

def load():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return data



if __name__ == "__main__":

    data = {}
    data["last"]=time.strftime("%Y%m%d")
    store(data)

    data = load()
    print(data["last"])