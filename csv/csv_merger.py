# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 09:18:35 2018

@author: root
"""

import csv
import math
import os




folder="csv/trajectory_"
out_file="output.csv"
file_num=8


def merge_csv(folder_path,out_file):
    file_list = os.listdir(folder_path)
    with open(out_file,'wb') as csvtarget:
        filewriter=csv.writer(csvtarget,delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for filename in file_list:
            if(filename.endswith('.csv')):
                csvdata=csv.reader(open(filename, 'r'))
                for data in csvdata:
                    rowvals=data
                    filewriter.writerow(rowvals)
    return 0


#merge_csv(file_num, out_file)
