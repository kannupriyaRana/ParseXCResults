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


# according to iphone 11 pro of lab device macmini1mdeios 
#dump new plist file only if any file corresponding to this iphone does not exist

#taking random
baselinePlistFileNameForIphone11Pro = 'F99382EE-3210-4DFD-AF2F-32BE84E47531'
filePathForBaselinePlistFile = f'findRecipe/findRecipe.xcodeproj/xcshareddata/xcbaselines/C34F493E27C47808003202A3.xcbaseline/{baselinePlistFileNameForIphone11Pro}.plist'
pathForInfoPlistFile = 'findRecipe/findRecipe.xcodeproj/xcshareddata/xcbaselines/C34F493E27C47808003202A3.xcbaseline/Info.plist'

def createRootFoldersForBaselineFiles():
	if os.path.exists('findRecipe/findRecipe.xcodeproj/xcshareddata')==False:
		os.chdir("findRecipe/findRecipe.xcodeproj")
		os.mkdir('xcshareddata')
	os.chdir("findRecipe/findRecipe.xcodeproj/xcshareddata")
	if os.path.exists("findRecipe/findRecipe.xcodeproj/xcshareddata/xcbaselines")==False:
		os.mkdir('xcbaselines')
	os.chdir("findRecipe/findRecipe.xcodeproj/xcshareddata/xcbaselines")
	if os.path.exists("findRecipe/findRecipe.xcodeproj/xcshareddata/xcbaselines/C34F493E27C47808003202A3.xcbaseline")==False:
		os.mkdir('C34F493E27C47808003202A3.xcbaseline')



# def createRootFoldersForBaselineFiles():
# 	if os.path.exists('findRecipe/findRecipe.xcodeproj/xcshareddata')==False:
# 		os.chdir("findRecipe/findRecipe.xcodeproj")
# 		os.mkdir('xcshareddata')
# 	os.chdir("/Users/research/Agent/_work/8/s/Mobile/IOSDefendersPoC/KannupriyaInternDemo/findRecipe/findRecipe.xcodeproj/xcshareddata")
# 	if os.path.exists("/Users/research/Agent/_work/8/s/Mobile/IOSDefendersPoC/KannupriyaInternDemo/findRecipe/findRecipe.xcodeproj/xcshareddata/xcbaselines")==False:
# 		os.mkdir('xcbaselines')
# 	os.chdir("/Users/research/Agent/_work/8/s/Mobile/IOSDefendersPoC/KannupriyaInternDemo/findRecipe/findRecipe.xcodeproj/xcshareddata/xcbaselines")
# 	if os.path.exists("/Users/research/Agent/_work/8/s/Mobile/Mobile/IOSDefendersPoC/KannupriyaInternDemo/findRecipe/findRecipe.xcodeproj/xcshareddata/xcbaselines/C34F493E27C47808003202A3.xcbaseline")==False:
# 		os.mkdir('C34F493E27C47808003202A3.xcbaseline')

def createEmptyInitialBaselineFile(filePathForBaselinePlistFile):
	if os.path.exists(filePathForBaselinePlistFile)==False:
		print("file doesn't exist !")
		with open(filePathForBaselinePlistFile, 'wb') as fp:
			p = {'classNames':{'AddIngredientUnitTests':{'testDeleteAllIngredientsMethodRemovesAllINgredientsFromUserDefaultsAndIngredientArray()':{'com.apple.dt.XCTMetric_CPU.cycles':{'baselineAverage':3,'baselineIntegrationDisplayName':'Local Baseline','maxPercentRelativeStandardDeviation':10}}}}}
			plistlib.dump(p, fp)
		print("Info.plist doesn't exist !")
		with open(pathForInfoPlistFile, 'wb') as fp:
			p = {'runDestinationsByUUID':{'F99382EE-3210-4DFD-AF2F-32BE84E47531':{'localComputer':{'busSpeedInMHz':400,'cpuCount':1,'cpuKind':'6-Core Intel Core i5','cpuSpeedInMHz':3000,'logicalCPUCoresPerPackage':6,'modelCode':'Macmini8,1','physicalCPUCoresPerPackage':6,'platformIdentifier':'com.apple.platform.macosx'},'targetArchitecture':'x86_64','targetDevice':{'modelCode':'iPhone12,3','platformIdentifier':'com.apple.platform.iphonesimulator'}}}}
			plistlib.dump(p, fp)
			print('entry for iphone11 pro created in Info.plist')

# os.chdir("/Users/research/Agent/_work/8/s/Mobile/IOSDefendersPoC/KannupriyaInternDemo")
os.system("echo pwd :")
os.system("pwd")
# os.system("echo ls of pwd :")
# os.system("ls")
# os.chdir("/Users/research/Agent/_work/8/s/Mobile/IOSDefendersPoC/KannupriyaInternDemo/findRecipe")
# os.system("ls")
# os.chdir("/Users/research/Agent/_work/8/s/Mobile/IOSDefendersPoC/KannupriyaInternDemo/findRecipe/findRecipe.xcodeproj")
# os.system("ls")
# os.chdir("/Users/research/Agent/_work/8/s/Mobile/IOSDefendersPoC/KannupriyaInternDemo/findRecipe/findRecipe.xcodeproj/xcshareddata/xcbaselines/C34F493E27C47808003202A3.baseline")
# os.system("ls")

# createRootFoldersForBaselineFiles()
updateInfoPlist(pathForInfoPlistFile)
createEmptyInitialBaselineFile(filePathForBaselinePlistFile)
os.system("cat " + filePathForBaselinePlistFile)
os.system("cat " + pathForInfoPlistFile)