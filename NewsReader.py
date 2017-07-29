# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:30:12 2017

@author: Sarvaswa
"""
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
        
    ## Detect Platform
    platform = os.sys.platform.lower()
    
    ## Obtain News-API Key
    if not os.path.isfile('key.csv'):
        print('No Keys Found. Run setup_system.py first to add new key.')
    else:
        api_key = read_key()
        
        ## Run News Reader based on Plaform
        if platform[:3]=='win':
            print('Windows Detected')
            if (not os.path.isfile('commands.bat')):
                print('No Commands File Found. Run setup_system.py first to generate commands.')
            else:
                p = Popen('commands.bat', stdin=PIPE, stdout=PIPE,
                          stderr=PIPE, shell=True)
                stdout, stderr = p.communicate()
                print(stdout.decode('cp1252', errors='replace'))
        elif platform == 'darwin':
            print('Mac OSX Detected')
            os.system('python newsUpdate.py ' + api_key)