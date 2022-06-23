
#!/usr/bin/python

import os
import plistlib

def main():

   currentMetricsDirectory = os.path.expanduser('/Users/administrator/Library/Developer/Xcode/DerivedData/findRecipe-cqxicvatywzmzvgrkucsqqrufzuq/Logs/Test/Test-findRecipe-2022.03.08_11-08-35-+0530.xcresult')
   if os.path.exists(currentMetricsDirectory):
      print('file found !')
      print('Is this a directory : %s\n' %os.path.isdir(currentMetricsDirectory))
      xcrun xcresulttool get --path ~/Library/Developer/Xcode/DerivedData/findRecipe-cqxicvatywzmzvgrkucsqqrufzuq/Logs/Test/Test-findRecipe-2022.03.08_11-08-35-+0530.xcresult --format json --id 0~OBHwrkRsiw-GVkf-M8HYYWSzgTt74Aqd5RI1Sd1itv2e0NCZf8orEXMvNz-9fgD5VB7jTsM0yXVDTV2bXrKOqQ==
   else:
      print('file not found')


if __name__ == '__main__':
   main()

# # similarly store correspoding values of metrics for each test case 