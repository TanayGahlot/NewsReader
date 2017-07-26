# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:30:12 2017

@author: Sarvaswa
"""

## Key: 9f055cb1404449f79aca035f832b32f9

## Script to run updateNews.py

## Import required packages
import os
import csv
from subprocess import Popen, PIPE

## Function to read key from file
def read_key():
    
    with open('key.csv', 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            key = ''.join(r)
    return key

if __name__ == '__main__':
    
    exit_flag = 0
    
    ## Obtain News-API Key
    if not os.path.isfile('key.csv'):
        print('No Keys Found. Run setup_system.py first to add new key.')
        exit_flag = 1
    else:
        api_key = read_key()
    
    ## Generate Commands
    if (not os.path.isfile('commands.bat')) and (exit_flag == 0):
        print('No Commands File Found. Run setup_system.py first to generate commands.')
    
    ## Run Commands
    if not exit_flag:
        p = Popen('commands.bat', stdin=PIPE, stdout=PIPE,
                  stderr=PIPE, shell=True)
        stdout, stderr = p.communicate()
        print(stdout)
        print(stderr)