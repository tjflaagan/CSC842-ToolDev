#!/usr/bin/python3

from pymongo import MongoClient
import json
import pprint


client = MongoClient()
db = client['grader']


r = db.assigns.find({},{"_id": 0,"assign": 1, "prof": 1, "due": 1})

for i in r:
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(i)


