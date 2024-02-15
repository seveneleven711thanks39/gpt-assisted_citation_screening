#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import os

#Load data from an Excel file using Pandas
MYDIR = "Your directory"
filename = os.path.join(MYDIR, 'file name')

df = pd.read_excel(filename,
                   sheet_name="Sheet1",
                  engine='openpyxl',)
