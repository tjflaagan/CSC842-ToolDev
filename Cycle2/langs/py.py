#!/usr/bin/python3

import os
import sys
import time
import subprocess
from os.path import isfile, join

def execute(file, path, js):
    output = ''
    args = ''
    Input = js["IO"]["Input"]
    try:
        start = time.time()
        p = subprocess.Popen(["python3", file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout_val = p.communicate(Input.encode(encoding='UTF-8'))[0]
        end = time.time()
        subprocess.call(['rm', join(path,'a.out')])
        return stdout_val
    except: 
        print("Error -", file)