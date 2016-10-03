#!/usr/bin/python3

import sys
import os
import re
import json
import pprint
import shutil
import subprocess
import argparse
import itertools
from os.path import isfile, join
from pymongo import MongoClient


# Importing languages
import langs.c
import langs.cpp
import langs.py



# Example python3 grade.py --file Test
def main():
    parser = argparse.ArgumentParser(prog="Auto-Grader", description='Auto Grader')
    parser.add_argument('--file', '-f', type=str, help='Directory containing programs', required=False)
    parser.add_argument('--perfect', '-p', help='Use perfect graded (1 or 0)', required=False, default=False, action='store_true')
    parser.add_argument('--moss', '-m', help='Run moss on the files', required=False, default=False, action='store_true')

    args = parser.parse_args()
    Path = args.file
    Perf = args.perfect
    Moss = args.moss
    
    moss_run = True
    moss_return = ''

    client = MongoClient()
    db = client['grader']


    # Determines language and fires the grading and output functions
    # Note: Langs now return a tuple with (Output, runtime)
    files = [ F for F in os.listdir(Path) if isfile(join(Path,F))]
    
    for P in files:
        lang = P.split('.')[1]
        user = P.split('_')[0]
        if(lang != 'pl'):
            assign = P.split('_')[1].split('.')[0]
        else:
            continue

        output = ''
        assign_data = db.assigns.find_one({"assign":assign})

        if(lang == 'c'):
            output = langs.c.execute(join(Path,P), Path, assign_data)
            if Moss == True and moss_run == True:
                p = subprocess.Popen(["./"+Path+"/moss.pl " + Path + "/*.c"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
                moss_return = p.communicate()[0]
                print(moss_return.decode('ascii').split('\n')[-2])
        elif(lang =='cpp'):
            output = langs.cpp.execute(join(Path,P), Path, assign_data)
            if Moss == True and moss_run == True:
                p = subprocess.Popen(["./"+Path+"/moss.pl *.cpp"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
                moss_return = p.communicate()[0]
                print(moss_return.decode('ascii').split('\n')[-2])
        elif(lang == 'py'):
            output = langs.py.execute(join(Path,P), Path, assign_data)
            if Moss == True and moss_run == True:
                p = subprocess.Popen(["./"+Path+"/moss.pl *.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
                moss_return = p.communicate()[0]
                print(moss_return.decode('ascii').split('\n')[-2])

        moss_run = False
        Moss = False
        

        total = 0
        correct = 0
        output = output[0].decode(encoding='UTF-8')
    
        if(Perf):
            if(assign_data["io"]["output"] == output[0]):
                return (1, 1)
            else:
                return (0, 1)
        else:
            gradeable = re.findall(r"[\w']+|[.,;]", output[0])
            answer = re.findall(r"[\w']+|[.,;]", assign_data["io"]["output"])

            for g, a in itertools.zip_longest(gradeable, answer):
                total += 1
                if(g == a):
                    correct += 1

        grade = (correct, total)

        s = db.grades.insert_one({
            "student": user,
            "correct": grade[0],
            "total": grade[1],
            "runtime": output[1],
            "assign": assign_data["_id"],
            "file_type": lang
        }) 

        shutil.move(join(Path, P), join(Path, "Complete", P))

        

if __name__ == '__main__':
    main()

























