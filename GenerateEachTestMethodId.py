#!/usr/bin/python3


#generates ID of each of those tests which have a measureBlock, because then only it is comparable in terms of metrics

import json
import sys
import csv

input = sys.argv
currentTestsReferencetFileName=input[1]
with open(currentTestsReferencetFileName,'r') as json_file:
   json_load=json.load(json_file)			#It will store the JSON as python dictionary  => json_load is now a dictionary



csvFilePath='/Users/runner/work/1/s/./Mobile/IOSDefendersPoC/KannupriyaInternDemo/JSONFromXcresulttool/testMethodIds.csv'
with open(csvFilePath,'w',newline='') as fp:
   a = csv.writer(fp, delimiter=',')
   a.writerow(['methodname','id'])
   # last two -values are iterable
   for i in range(0,len(json_load['summaries']['_values'][0]['testableSummaries']['_values'][0]['tests']['_values'][0]['subtests']['_values'][0]['subtests']['_values'])):            # No. of testClasses
      for j in range (0,len(json_load['summaries']['_values'][0]['testableSummaries']['_values'][0]['tests']['_values'][0]['subtests']['_values'][0]['subtests']['_values'][i]['subtests']['_values'])):        # No. of test methods in each class
         testName=json_load['summaries']['_values'][0]['testableSummaries']['_values'][0]['tests']['_values'][0]['subtests']['_values'][0]['subtests']['_values'][i]['subtests']['_values'][j]['name']['_value']
         testStatus = json_load['summaries']['_values'][0]['testableSummaries']['_values'][0]['tests']['_values'][0]['subtests']['_values'][0]['subtests']['_values'][i]['subtests']['_values'][j]['testStatus']['_value']
         currentTest = json_load['summaries']['_values'][0]['testableSummaries']['_values'][0]['tests']['_values'][0]['subtests']['_values'][0]['subtests']['_values'][i]['subtests']['_values'][j]


         # printing only those tests which have a measure
         if 'summaryRef' in currentTest:
            print(testName)
            print(testStatus)
            testId=print(currentTest['summaryRef']['id']['_value'])
            print('--------------------------------------------')
            data = [testName,testId]
            a.writerow(data)
