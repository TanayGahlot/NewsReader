# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 20:18:52 2017

@author: Sarvaswa
"""

## Setup File

## Import required packages
import os
import csv

## Function to generate commands file
def gen_commands(key):
    
    commands = ['chcp 65001',
                'python3 newsUpdate.py ' + key]
    numCommands = len(commands)
    
    with open('commands.bat', 'w') as f:
        for i,command in enumerate(commands,1):
            if i == numCommands:
                f.write(command)
            else:
                f.write(command + '\n')

## Function to store key to file
def add_key():
    
    key = input('Enter News-API key: ')
    with open('key.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(key)
    
    print('New Key Added')
    gen_commands(key)
    return key

## Function to read key from file
def read_key():
    
    with open('key.csv', 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            key = ''.join(r)
    return key

if __name__ == '__main__':
    
    ## Obtain News-API Key
    if not os.path.isfile('key.csv'):
        api_key = add_key()
    else:
        api_key = read_key()
    
    ## Generate Commands File for Windows
    platform = os.sys.platform.lower()
    if (not os.path.isfile('commands.bat')) and (platform[:3] == 'win'):
        gen_commands(api_key)
    
    print('All Set. Run NewsReader.py to listen to latest news updates!')