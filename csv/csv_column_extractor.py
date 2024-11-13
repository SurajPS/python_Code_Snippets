# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 12:57:02 2018

@author: Z637257

To take only certain columns from a csv file and write it in a new csv file
"""

import csv

import pandas as pd
from numpy import genfromtxt

def extract_columns(file_name, out_file="output.csv", columns=[0,1,2]):
    print ("Read Start")
    csvdata=genfromtxt(file_name, delimiter=' ')
    data=csvdata[:,columns]
    firstline=True
    print ("Read Finish")
    with open(out_file,'wb') as csvtarget:
        print ("Write Start")
        filewriter=csv.writer(csvtarget,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for dat in data:
            if(firstline):
                firstline=False
                continue
            filewriter.writerow(dat)
    

