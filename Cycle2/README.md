# Auto Grader Script Edition 2 
## General Information
* Author: Tyler Flaagan
* Date: 10/02/16
* Script Name: grade.py
* Description: This script takes input created by an instructor or professor and input from the student. Once the student that gives the specified input and proper output from 

## Edition 2 Additions

* Code base refactoring.
* Implemented local Mongodb for storage instead of flat files.
* Fixed problems with Python lang. 
* Added running time info.
* HTML output for given assignment.
* Fixed argument issue pointed out by @Spirotot.
* Added script to help instructors build assignments.
* Moss perl script integration.
* Script to show currently available assignments.
* Script to show students results for a given assignment.

## Use Case and Background Info

Often times while teaching a class the most burdoning task is grading. For some it is the least liked portion of teaching a class. It can take hours on end to manually compile, execute, and review code. This script will attempt to shorten that time greatly for any that use it. 

This script is designed similarly to ACM style grading except it has the capability to give more detailed output and different style of output rather than the 0 or 1 style checking from ACM. While this is created to move away from the 0 or 1 style, it is best to stick to programs that output data in a fashion that has good deliminators. While the ACM site specifies programs that can be used, this tool allows instructors to create their own assignments to be graded.

This script is not meant to be a complete grading solution yet. If the answer in the JSON file is correct and the student receives 100% on the assignment, the grader may want to skip manually verifying the code. If other grades show up, additional review is recommended. 

## Installation
The installation instructions assume the following dependencies are met:
* The machine running the script has the correct version of Python running.
* The user has permissions to execute the script
* Program must be submitted using the following naming convention: `lastname_programID.extension`
* The machine must have mongo running

To set up and run the script, perform the following:

1. Copy the script to the machine that has dependencies met.
2. Launch the grade.py script with the following Python command:

`> python3 grade.py <arguments>`


Extra:

To launch the assign builder

`> python3 assignBuilder.py`

To launch assign finder

`> python3 assignFinder.py`

## Possible Future Work

* Create cron job/script that watches all assignments due dates and runs the grading script on the due date.
	* This would allow for emailing results to instructor or professor or even possibly uploading scores without professor or instructor intervention. Full automation from submission to published grade in D2L.
* Added code to kill infinite looping code.
* Integrate @Spirotot's utility to automatically upload score and feedback to D2L.
* Different styles of grading could be added. (Still haven't come up with any)
* Better error checking in assign builder script. Input and if there is already an assign by that name.
* Better file storage/handling for assignments.
* Add hours/minutes to date time selection for specific due times.
* Error handling for when assignment is not found
* Added checks for programs that don't compile in C and C++.
* With the way this has been developing, I want to incorporate all of it into a django site. Since I haven't worked with django before and that is a much steeper learning curve. Not sure if I'll get around to that. This would solve a few problems that are going to come up soon I think. 

## Resources

https://docs.mongodb.com/getting-started/python/client/

## Other stuff

What's needed for local Mongo:


Install the OSX version of mongo

Install the Python mongo driver

    pip install pymongo
