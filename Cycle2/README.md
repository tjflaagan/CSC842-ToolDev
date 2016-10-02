# Auto Grader Script Edition 2 
## General Information
* Author: Tyler Flaagan
* Date: 10/02/16
* Script Name: grade.py
* Description: This script takes input created by an instructor or professor and input from the student. Once the student that gives the specified input and proper output from 

## Use Case and Background Info

Often times while teaching a class the most burdoning task is grading. For some it is the least liked portion of teaching a class. It can take hours on end to manually compile, execute, and review code. This script will attempt to shorten that time greatly for any that use it. 

This script is designed similarly to ACM style grading except it has the capability to give more detailed output and different style of output rather than the 0 or 1 style checking from ACM. While this is created to move away from the 0 or 1 style, it is best to stick to programs that output data in a fashion that has good deliminators. While the ACM site specifies programs that can be used, this tool allows instructors to create their own assignments to be graded.

This script is not meant to be a complete grading solution yet. If the answer in the JSON file is correct and the student receives 100% on the assignment, the grader may want to skip manually verifying the code. If other grades show up, additional review is recommended. 

## Installation
The installation instructions assume the following dependencies are met:
* The machine running the script has the correct version of Python running.
* The user has permissions to execute the script
* Program must be submitted using the following naming convention: `lastname_programID.extension`

To set up and run the script, perform the following:

1. Copy the script to the machine that has dependencies met.
2. Launch the grade.py script with the following Python command:

`> python3 grade.py <arguments>`


## Possible Future Work
* Add in more output options (CSV, HTML, XML).
* Integrate @Spirotot's utility to automatically upload score and feedback to D2L.
* Create cron job/script that watches all assignments due dates and runs the grading script on the due date.
	* This would allow for emailing results to instructor or professor or even possibly uploading scores without professor or instructor intervention. Full automation from sumbission to published grade in D2L.
* Integrate MOSS, this may be slightly more difficult since there isn't a Python version of the software.
	* <https://theory.stanford.edu/~aiken/moss/>
* Create web front end to handle assignment creation/grade reporting and student assignment submission.
* Add support for linking other libraries such as linking math library in C.
* Add support for more languages.
* Possibly move away from static JSON files to a type of DB.
* Different styles of grading could be added (Not sure what those would be at this point)
* Allow for both versions of Python for all of you who have not updated... :(

* I kept changing the overall flow of the script throughout writing so a refactoring is necessary at this point.