#!/usr/bin/python3

# generates reference ID for an xctestresult file

import json
import sys

input = sys.argv
currentTestFileName=input[1]
# print(currentTestFileName)
# currentTestFileName = 'CurrentTest.json'
with open(currentTestFileName,'r') as json_file:
   json_load=json.load(json_file)			#It will store the JSON as python dictionary  => json_load is now a dictionary
testRefId=json_load['actions']['_values'][0]['actionResult']['testsRef']['id']['_value']	#gives the testsRef.id => which 
sys.exit(testRefId) 

# def return_testRefID(currentTestFileName):
#    with open(currentTestFileName,'r') as json_file:
#       json_load=json.load(json_file)         #It will store the JSON as python dictionary  => json_load is now a dictionary
#       testRefId=json_load['actions']['_values'][0]['actionResult']['testsRef']['id']['_value']  #gives the testsRef.id => which 
#       return testRefId


# if __name__ == '__main__':
#    input=sys.argv
#    return_testRefID(input[1])


