import glob
import os


list_of_files = glob.glob('/Users/administrator/Library/Developer/Xcode/DerivedData/findRecipe-cqxicvatywzmzvgrkucsqqrufzuq/Logs/Test/*.xcresult')

# print(list_of_files)
latest_file = max(list_of_files,key=os.path.getmtime)
print(latest_file)

