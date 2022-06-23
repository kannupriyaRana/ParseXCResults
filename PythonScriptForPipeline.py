#!/usr/bin/python3

import json
import sys
import os
import plistlib
import csv
import time
import plistlib
import sys
import os.path
import glob


def returnLatestXCResultFileCreated():
    folder_path = r'/Users/mdsremacadmin/Library/Developer/Xcode/DerivedData/findRecipe-*/Logs/Test/*xcresult'
    files = glob.glob(folder_path)
    print(files)
    max_file = max(files, key=os.path.getctime)
    print(max_file)
    return max_file


def createEmptyInitialBaselineFile(filePathForBaselinePlistFile):
	if os.path.exists(filePathForBaselinePlistFile)==False:
		print("file doesn't exist !")
		with open(filePathForBaselinePlistFile, 'wb') as fp:
			p = {'classNames':{}}
			plistlib.dump(p, fp)
			print('file created !')

def xcresulttoolCallWithoutId(baseFileToExtractValues, destinationFileToDumpValues):
	os.system("xcrun xcresulttool get --path " +baseFileToExtractValues+ " --format json > " +destinationFileToDumpValues)

def xcresulttoolCallWithId(baseFileToExtractValues, id, destinationFileToDumpValues):
	os.system("xcrun xcresulttool get --path " +baseFileToExtractValues+ " --format json --id " +testRefId+ " > " +destinationFileToDumpValues)

def getTestRefIdOfATestReport(filePathOfFileContainingTestReportInJSON):
	with open(filePathOfFileContainingTestReportInJSON,'r') as json_file:
		json_load=json.load(json_file)			#It will store the JSON as python dictionary  => json_load is now a dictionary
	testRefId=json_load['actions']['_values'][0]['actionResult']['testsRef']['id']['_value']	#gives the testsRef.id => which
	os.system("echo ------------------Printing testReferenceId : ")
	os.system("echo " +testRefId) 
	return testRefId

def extractAllTestsIdsAndTestName(filePathForFileContainingAllTestIdsAndtestNames):
	dictContainingTestIdAndTestName={}
	with open(filePathForFileContainingAllTestIdsAndtestNames,'r') as jsonFileContainingAllTestInfo:
	   jsonLoadedWithAllTestInfo=json.load(jsonFileContainingAllTestInfo)

	for i in range(0,len(jsonLoadedWithAllTestInfo['summaries']['_values'][0]['testableSummaries']['_values'][0]['tests']['_values'][0]['subtests']['_values'][0]['subtests']['_values'])):            # No. of testClasses
	      for j in range (0,len(jsonLoadedWithAllTestInfo['summaries']['_values'][0]['testableSummaries']['_values'][0]['tests']['_values'][0]['subtests']['_values'][0]['subtests']['_values'][i]['subtests']['_values'])):        # No. of test methods in each class
	         testName=jsonLoadedWithAllTestInfo['summaries']['_values'][0]['testableSummaries']['_values'][0]['tests']['_values'][0]['subtests']['_values'][0]['subtests']['_values'][i]['subtests']['_values'][j]['name']['_value']
	         testStatus = jsonLoadedWithAllTestInfo['summaries']['_values'][0]['testableSummaries']['_values'][0]['tests']['_values'][0]['subtests']['_values'][0]['subtests']['_values'][i]['subtests']['_values'][j]['testStatus']['_value']
	         currentTest = jsonLoadedWithAllTestInfo['summaries']['_values'][0]['testableSummaries']['_values'][0]['tests']['_values'][0]['subtests']['_values'][0]['subtests']['_values'][i]['subtests']['_values'][j]

	         # printing only those tests which have a measure
	         if 'summaryRef' in currentTest:
	            testId=currentTest['summaryRef']['id']['_value']
	            dictContainingTestIdAndTestName[testId]=testName
	return dictContainingTestIdAndTestName

def extractInfoAboutEveryTest(dictContainingTestIdAndTestName):
	dictContainingInfoAboutEveryTest={}
	for testMethodId in dictContainingTestIdAndTestName:
		jsonFilePathForATestMethodInfo = 'JSONFromXcresulttool/testMethod.json'

		os.system("xcrun xcresulttool get --path " +currentXCResultFilePath+ " --format json --id " +testMethodId+ " > " +jsonFilePathForATestMethodInfo)
		os.system("cat " +jsonFilePathForATestMethodInfo) 
		
		with open(jsonFilePathForATestMethodInfo,'r') as json_file:

			json_load=json.load(json_file)
			nameOfMethod=json_load['name']['_value']
			tempClassAndMethodName=(json_load['identifier']['_value'])
			print(tempClassAndMethodName)
			print('-------------------------------')
			nameOfTestClass=tempClassAndMethodName.split('/')[0]
			print(nameOfTestClass)
			print('-------------------------------')
			dictContainingInfoAboutATest={}
			dictContainingInfoAboutATest['correspondingClass']=nameOfTestClass
			for i in range(0,len(json_load['performanceMetrics']['_values'])):

				dictContainingInfoAboutAMetric={}
				displayNameOfAMetric=json_load['performanceMetrics']['_values'][i]['displayName']['_value']
				identifier=json_load['performanceMetrics']['_values'][i]['identifier']['_value']
				dictContainingInfoAboutAMetric['identifier'] = identifier				
				maxPercentRegression=json_load['performanceMetrics']['_values'][i]['maxPercentRegression']['_value']
				dictContainingInfoAboutAMetric['maxPercentRegression'] = maxPercentRegression
				maxPercentRelativeStandardDeviation=json_load['performanceMetrics']['_values'][i]['maxPercentRelativeStandardDeviation']['_value']
				# maxRegression=json_load['performanceMetrics']['_values'][i]['maxRegression']['_value']
				# maxStandardDeviation=json_load['performanceMetrics']['_values'][i]['maxStandardDeviation']['_value']
				unitOfMeasurement=json_load['performanceMetrics']['_values'][i]['unitOfMeasurement']['_value']
				dictContainingInfoAboutAMetric['unitOfMeasurement'] = unitOfMeasurement
				avg=0.0
				for j in range (0,len(json_load['performanceMetrics']['_values'][i]['measurements']['_values'])):
					avg+=float(json_load['performanceMetrics']['_values'][i]['measurements']['_values'][j]['_value'])
				avg=avg/float(len(json_load['performanceMetrics']['_values'][i]['measurements']['_values']))
				dictContainingInfoAboutAMetric['avg'] = avg
				dictContainingInfoAboutATest[displayNameOfAMetric] = dictContainingInfoAboutAMetric
			dictContainingInfoAboutEveryTest[nameOfMethod] = dictContainingInfoAboutATest
	return dictContainingInfoAboutEveryTest

def insertBaselinesOfNewlyAddedFunctionsInBaselineFile(filePathForBaselinePlistFile):
	with open(filePathForBaselinePlistFile, 'r+b') as fp:
		p = plistlib.load(fp)
		for testMethodName in dictContainingInfoAboutEveryTest:
			classNameForThisTestMethod=dictContainingInfoAboutEveryTest[testMethodName]['correspondingClass']
			if classNameForThisTestMethod not in p['classNames'].keys():
				with open(filePathForBaselinePlistFile, 'wb') as nfp:
					p['classNames'][classNameForThisTestMethod] = {}
					plistlib.dump(p, nfp)
			if testMethodName not in p['classNames'][classNameForThisTestMethod]:
					plistDictionaryContainingMetricsForThisTest={}
					for i in dictContainingInfoAboutEveryTest[testMethodName]:
						if i != 'correspondingClass':
							metricIdentifier = dictContainingInfoAboutEveryTest[testMethodName][i]['identifier']
							metricValue = int(dictContainingInfoAboutEveryTest[testMethodName][i]['avg'])
							metricMaxSD = int(float(dictContainingInfoAboutEveryTest[testMethodName][i]['maxPercentRegression']))
							plistDictionaryContainingMetricsForThisTest[metricIdentifier] = {'baselineAverage': metricValue, 'baselineIntegrationDisplayName': 'Local Baseline', 'maxPercentRelativeStandardDeviation': metricMaxSD}
					p['classNames'][classNameForThisTestMethod][testMethodName] = plistDictionaryContainingMetricsForThisTest
					with open(filePathForBaselinePlistFile, 'wb') as nfp:
						plistlib.dump(p, nfp)

def populateDictContainigViolatedMetrics(dictContainingInfoAboutEveryTest):
	dictForViolationOfBaselines = {}
	baselineForCPUCycles = 100
	baselineForCPUTime=0.0000094761455
	for testMethodName in dictContainingInfoAboutEveryTest:
		for info in dictContainingInfoAboutEveryTest[testMethodName]:
			if info=="CPU Cycles" and dictContainingInfoAboutEveryTest[testMethodName][info]['avg']>baselineForCPUCycles :
				dictForViolationOfBaselines[(info, testMethodName)] = [dictContainingInfoAboutEveryTest[testMethodName][info]['avg'],baselineForCPUCycles]
			if info=="CPU Time" and dictContainingInfoAboutEveryTest[testMethodName][info]['avg']>baselineForCPUTime :
				dictForViolationOfBaselines[(info, testMethodName)] = [dictContainingInfoAboutEveryTest[testMethodName][info]['avg'],baselineForCPUTime]
	return dictForViolationOfBaselines

def printViolatedMetrics(dictForViolationOfBaselines):
	if len(dictForViolationOfBaselines)!=0 :
		for keys in dictForViolationOfBaselines:
			print(f'Violated metric : {keys}, Current run average value : {dictForViolationOfBaselines[keys][0]}, Baseline value :  {dictForViolationOfBaselines[keys][1]}')
		print("Current Tests exceeded baselines !!", file = sys.stderr )

#for iphone 11 pro
baselinePlistFileName = 'F99382EE-3210-4DFD-AF2F-32BE84E47531'
filePathForBaselinePlistFile = f'findRecipe/findRecipe.xcodeproj/xcshareddata/xcbaselines/C34F493E27C47808003202A3.xcbaseline/{baselinePlistFileName}.plist'
currentXCResultFilePath = returnLatestXCResultFileCreated()
print("Current xcresult file : ")
print(currentXCResultFilePath)
# currentXCResultFilePath = f'/Users/research/Library/Developer/Xcode/DerivedData/findRecipe-*/Logs/Test/{currentXCResultFileName}'
CurrentTestJSONFilePath='JSONFromXcresulttool/CurrentTestBundle.json'
LookInsideTestBundleFilePath='JSONFromXcresulttool/LookInsideTestBundleForMethodIds.json'

xcresulttoolCallWithoutId(currentXCResultFilePath,CurrentTestJSONFilePath)

testRefId = getTestRefIdOfATestReport(CurrentTestJSONFilePath)

xcresulttoolCallWithId(currentXCResultFilePath, testRefId, LookInsideTestBundleFilePath)

dictContainingTestIdAndTestName = extractAllTestsIdsAndTestName(LookInsideTestBundleFilePath)
print(dictContainingTestIdAndTestName)

dictContainingInfoAboutEveryTest = extractInfoAboutEveryTest(dictContainingTestIdAndTestName)
print(dictContainingInfoAboutEveryTest)

dictForViolationOfBaselines={}

# createEmptyInitialBaselineFile(filePathForBaselinePlistFile)

insertBaselinesOfNewlyAddedFunctionsInBaselineFile(filePathForBaselinePlistFile)

dictForViolationOfBaselines = populateDictContainigViolatedMetrics(dictContainingInfoAboutEveryTest)

printViolatedMetrics(dictForViolationOfBaselines)

