#!/usr/bin/python3

from pymongo import MongoClient
import json
import pprint


client = MongoClient()
db = client['grader']


r = db.grades.find({})
f = open('grades.html','w')

table_data = [
        ['Assignment',   'Name',   'Correct', 'Total', 'Type'],

    ]
message = "<html><head></head><body><table><tr><th>Assign</th><th>Student</th><th>Correct</th><th>Total</th><th>File Type</th></tr>"


for i in r:
    message += "<tr>"
    message += "<td>"+str(i['student'])+"</td>"
    message += "<td>"+str(i['correct'])+"</td>"
    message += "<td>"+str(i['total'])+"</td>"
    message += "<td>"+str(i['file_type'])+"</td>"
    message += "</tr>"


message += "</table></body></html>"

f.write(message)
f.close()
