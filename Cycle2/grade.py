#!/usr/bin/python3

import sys
import os
import re
import json
import argparse
import itertools
from os.path import isfile, join

# Importing languages
import langs.c
import langs.cpp
import langs.py

# Outputs to json file and standard output
def outputFunc(grade, user, js, P):
    # print(js["Student"])
    js["Student"].append({"Correct": grade[0], "Total": grade[1], "User": user})
        
    assign = P.split('_')[1].split('.')[0] + '.json'
    with open(join("Assigns", assign), 'w') as f:
        js = json.dump(js, f)


# Compares answer to correct answer
def grader(user, output, js, Perf):
    total = 0
    correct = 0
    output = output.decode(encoding='UTF-8')
    
    if(Perf):
        if(js["IO"]["Output"] == output):
            return (1, 1)
        else:
            return (0, 1)
    else:
        gradeable = re.findall(r"[\w']+|[.,;]", output)
        answer = re.findall(r"[\w']+|[.,;]", js["IO"]["Output"])

        for g, a in itertools.zip_longest(gradeable, answer):
            total += 1
            if(g == a):
                correct += 1

        return (correct, total)



# Determines language and fires the grading and output functions
def langSwitch(Path,Perf):
    files = [ F for F in os.listdir(Path) if isfile(join(Path,F))]
    output = ''
    for P in files:
        lang = P.split('.')[1]
        user = P.split('_')[0]
        assign = P.split('_')[1].split('.')[0] + '.json'

        with open(join("Assigns", assign), 'r') as f:
            js = json.load(f)
        
        if(lang == 'c'):
            output = langs.c.execute(join(Path,P), Path, js)
        elif(lang =='cpp'):
            output = langs.cpp.execute(join(Path,P), Path, js)
        # elif(lang == 'py'):
        #     output = langs.py.execute(join(Path,P), Path, js)

        grade = grader(user, output, js, Perf)
        outputFunc(grade, user, js, P)


def main():
    parser = argparse.ArgumentParser(prog="Auto-Grader", description='Auto Grader')
    parser.add_argument('--file', '-f', type=str, help='Directory containing programs', required=False)
    parser.add_argument('--perfect', '-p', type=bool, help='Use perfect graded (1 or 0)', required=False)
    
    args = parser.parse_args()
    Path = args.file
    Perf = args.perfect

    langSwitch(Path, Perf)

if __name__ == '__main__':
    main()