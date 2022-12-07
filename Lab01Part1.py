#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 22:38:21 2022

@author: Ho Hang Cheng SID: 210058323
"""
#Part 1
#1.
import csv


f = open('TB_burden_countries_2014-09-29.csv')
i = 0
for row in csv.reader(f):
   i=i+1
print("The number of rows is "+str(i))
#
# =============================================================================
# 
# =============================================================================
#2.
#row count variable = 0, sum variable 0
import csv

row_sum = 0
row_count=0
f = open('TB_burden_countries_2014-09-29.csv')

    
for row in csv.reader(f) :  
      
  try:
    
     val = float(row[11])
     row_sum += val
     row_count += 1    
  except ValueError:
      pass
  
if row_count > 0:
    colavg = row_sum / row_count
    print('The average is '+str(colavg))

    
    
#3.

import csv

row_sum = 0
row_count=0
f = open('TB_burden_countries_2014-09-29.csv')

    
for row in csv.reader(f) :  
      
  try:
    if row[5] == '1990':
     val = float(row[11])
     row_sum += val
     row_count += 1    
  except ValueError:
      pass
  
if row_count > 0:
    colavg = row_sum / row_count
    print('The average for 1990 is '+str(colavg))
    
# =============================================================================
  
# =============================================================================
import csv

row_sum = 0
row_count=0
f = open('TB_burden_countries_2014-09-29.csv')

    
for row in csv.reader(f) :  
      
  try:
    if row[5] == '2011':
     val = float(row[11])
     row_sum += val
     row_count += 1    
  except ValueError:
      pass
  
if row_count > 0:
    colavg = row_sum / row_count
    print('The average for 2011 is '+str(colavg))

# ===========================$$$==================================================

    

#try:
    
#except:
    #ValueError
    


        
#use if 
# two variables for each year, total in four


#Part2: change number of bins
#np.sqrt 
    

