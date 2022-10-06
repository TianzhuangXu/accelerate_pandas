#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 08:53:12 2022

@author: xutianzhuang
"""

import sys
import pandas as pd
from datetime import datetime
import os

# input file directory
wkdr = '/Users/xutianzhuang/Desktop/accelerate_pandas/data/'
# output file directory
opdr = '/Users/xutianzhuang/Desktop/accelerate_pandas/output/'
filename = os.listdir(wkdr)
filename.remove('.DS_Store')
# sys.argv[1]) get parameter from shell
# shell loop can be adjusted, i represents the sequence of input data
# to multitask, run run.sh& together with different setup of i
file = pd.read_json(wkdr + filename[int(sys.argv[1])], lines = True)
sample = file[file['data'].apply(lambda x: (x['state'] == 'successful' or x['state'] == 'failed')
                                    and x['country'] == 'US' and x['currency'] == 'USD'
                                    and (x['category']['slug'].split('/')[0] == 'technology'
                                     or x['category']['slug'].split('/')[0] == 'games'
                                     or x['category']['slug'].split('/')[0] == 'design'))]
sample.to_json(opdr + filename[int(sys.argv[1])])
