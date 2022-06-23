# !/bin/bash 

#to read a result bundle, i.e. .xcresult file which corresponds to the details of a particular run of test suite

CurrentTestBundleFileName='CurrentTest.json'

xcrun xcresulttool get --path ~/Library/Developer/Xcode/DerivedData/findRecipe-cqxicvatywzmzvgrkucsqqrufzuq/Logs/Test/Test-findRecipe-2022.03.11_11-10-46-+0530.xcresult --format json  > ~/Desktop/CurrentTest.json  

testReferenceID=$((python ~/Desktop/ReadJSON.py $CurrentTestBundleFileName) 2>&1)
echo $testReferenceID
#id used here is testsRef.id from Current.json made in previous command
#Resultant file from this command will contain  id for each individual tests, using which we can get info about each test

CurretnTestDetailsFileName='lookinsideTextTestsRef.json'

xcrun xcresulttool get --path ~/Library/Developer/Xcode/DerivedData/findRecipe-cqxicvatywzmzvgrkucsqqrufzuq/Logs/Test/Test-findRecipe-2022.03.09_14-29-44-+0530.xcresult --format json --id $testReferenceID > ~/Desktop/lookinsideTextTestsRef.json
# methodsIds=$((python ~/Desktop/GenerateEachMethodId.py $CurretnTestDetailsFileName) 2>&1)
# echo $methodsIds


#a particular id(corresponding to a particular test) is chosen from file generated through previous command
# Now the resultant file from this command will contain all info regarding that particular test
xcrun xcresulttool get --path ~/Library/Developer/Xcode/DerivedData/findRecipe-cqxicvatywzmzvgrkucsqqrufzuq/Logs/Test/Test-findRecipe-2022.03.09_14-29-44-+0530.xcresult --format json --id 0~H01Bn-WdcQl86Y9H2IoSAaJisoVRTER5BtOzHJ2pwkD4KLEfwGG1YtQaq0SplVB4Yo5aSlzMTpDLtTHQ4MF6vg== > ~/Desktop/lookInsideParticularTest.json



# cd ~/Desktop

#####These two lines are not working here, but if I simply run the python file in terminal, it is running
# chmod u+x ReadMetricsPlistFilles.py
# python3 ReadMetricsPlistFilles.py
