#!/usr/bin/python3

import os
import sys
import time
import subprocess
from os.path import isfile, join

def execute(file, path, js):
    output = ''
    args = ''
    Input = js["io"]["input"]
    try:
        subprocess.check_output(["gcc", file], shell=False)
        start = time.time()
        subprocess.call(['mv', 'a.out', path])
        p = subprocess.Popen(["./"+path+"/a.out"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        stdout_val = p.communicate(Input.encode(encoding='UTF-8'))[0]
        end = time.time()
        subprocess.call(['rm', join(path,'a.out')])
        t = end - start
        return (stdout_val, t)
    except: 
        print("Error -", file)