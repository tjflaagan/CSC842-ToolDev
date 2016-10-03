#!/usr/bin/python3

from pymongo import MongoClient
from datetime import datetime
import json


client = MongoClient()
db = client['grader']


prof_name = str(input("Enter your name: "))
prof_email = str(input("Enter your email: "))
assign = str(input("Enter your assign ID (This is what your students will have in the second part of their file name): "))
due_date = str(input("Date (format) Y, M, D: "))
input1 = str(input("Program input: "))
output = str(input("Correct Program output: "))
libs = str(input("Other libs to link. Include the dash  ex. -lm (Only works for C): "))


try:
    due_date = datetime.strptime(due_date, '%Y, %m, %d')
except ValueError:
    print("Incorrect format")


r = db.assigns.insert_one(
    {
        "assign": assign,
        "prof": {
            "name": prof_name,
            "email": prof_email
        },
        "io": {
            "input": input1,
            "output": output,
            "libs": libs
            

        },
        "due": due_date,
    }
)


