#!/usr/bin/python


# Parse a plist file that contains info about baselines of different testMethods, different .csv files are generated that corresponds to each testMethod 
# Each .csv file contains baselines of each metric a test measures
import os
import plistlib
import csv
import pandas as pd
import time
from openpyxl.workbook import Workbook

def main():

   plistFileId = '7270C6BB-FC92-4790-AB38-E977E8599516'
   fileName=os.path.expanduser(f'/Users/runner/work/1/s/./Mobile/IOSDefendersPoC/KannupriyaInternDemo/findRecipe/*.xcodeproj/xcshareddata/xcbaselines/C34F493E27C47808003202A3.xcbaseline/{plistFileId}.plist')
   
   if os.path.exists(fileName):
      pl=plistlib.readPlist(fileName)
      if 'classNames' in pl:
         #each 'keys' in pl['classNames'] corresponds to each UnitTestClass Name
         for keys in pl['classNames']:
            currentTestBundleOfAClass = keys

            #each testMethodName in pl['classNames'][currentTestBundleOfAClass] corresponds to names of testMethods present in a UnitTestClass
            for testMethodName in pl['classNames'][currentTestBundleOfAClass]:
               metricsArrayofThisTest = pl['classNames'][currentTestBundleOfAClass][testMethodName]

               #here 'keys' corresponds to different metrics we are measuring for a particular testMethod
               keys = metricsArrayofThisTest.keys()
#               csvFileName = f'{testMethodName}.csv'

#               with open(csvFileName,'w',newline='') as fp:
#                  a = csv.writer(fp, delimiter=',')
#                  a.writerow(['metric','value'])
               for key in keys:
                  #put all metrics along with their baseline values in the csv file, each csv file corresponds to each testMethod
                  data = [key,metricsArrayofThisTest[key]['baselineAverage']]
                  print(data)
#                     a.writerow(data)

               #converting each .csv file into .xlsx file      
#               readFile = pd.read_csv(f'/Users/administrator/Desktop/{testMethodName}.csv')
#               readFile.to_excel(f'/Users/administrator/Desktop/{testMethodName}.xlsx',index=None, header=True)
      else:
         print('None of the tests has a measureBlock\n')


   else:
      print('No such plist file exists !')

   

if __name__ == '__main__':
   main()

# # similarly store correspoding values of metrics for each test case 
