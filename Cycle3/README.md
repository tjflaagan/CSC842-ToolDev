# Auto Grader Script
## General Information
* Author: Tyler Flaagan
* Date: 10/23/16
* Script Name: osinter.py
* Description: This script takes a list of subnets as input and is capable of performing multiple functions with those subnets. 


## Use Case and Background Info

While in the early phases of assessing a network some manual footwork has to be done especially during OSINT. This first set of utilities are things that I used to help get off the ground a step quicker.ying the code. If other grades show up, additional review is recommended. 

## Installation
The installation instructions assume the following dependencies are met:
* The machine running the script has the correct version of Python running.
* The user has permissions to execute the script
* Must have dependencies installed such as Censys

`> pip3 install censys`

## Usage

1. Copy the script to the machine that has dependencies met.
2. Launch the grade.py script with the following Python command:

`> python3 osinter.py <arguments>`


* I plan to add more features to this as I come across functionality that I think will fit well with the tool.
* Shodan was another consideration that I had but for my test cases it did not turn up any results. This will vary depending on your target.