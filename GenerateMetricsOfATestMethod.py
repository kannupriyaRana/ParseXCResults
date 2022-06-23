#!/usr/bin/python3

# Extract metrics of a partciular test

import json
import sys
import csv

input = sys.argv
currentTestReferenceFilePath = input[1]
currentTestName = input[2]
with open(currentTestReferenceFilePath,'r') as json_file:
   json_load=json.load(json_file)         #It will store the JSON as python dictionary  => json_load is now a dictionary

testStatus = json_load['testStatus']['_value']
print(testStatus)

csvFilePath='/Users/runner/work/1/s/./Mobile/IOSDefendersPoC/KannupriyaInternDemo/JSONFromXcresulttool/{currentTestName}.csv'
with open(csvFilePath,'w',newline='') as fp:
   a = csv.writer(fp, delimiter=',')

   for i in range (0, len(json_load['performanceMetrics']['_values'])):
      print(json_load['performanceMetrics']['_values'][i]['displayName']['_value'])
      print(json_load['performanceMetrics']['_values'][i]['identifier']['_value'])
      print(json_load['performanceMetrics']['_values'][i]['maxPercentRegression']['_value'])
      print(json_load['performanceMetrics']['_values'][i]['maxPercentRelativeStandardDeviation']['_value'])
      print(json_load['performanceMetrics']['_values'][i]['maxRegression']['_value'])
      print(json_load['performanceMetrics']['_values'][i]['maxStandardDeviation']['_value'])
      print(json_load['performanceMetrics']['_values'][i]['unitOfMeasurement']['_value'])

      for j in range (0,len(json_load['performanceMetrics']['_values'][i]['measurements']['_values'])):
         print(json_load['performanceMetrics']['_values'][i]['measurements']['_values'][j]['_value']),

      print('----------------------------------------')

