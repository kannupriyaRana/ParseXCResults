#!/usr/bin/python

import os
import plistlib

def main():

   fileName=os.path.expanduser('/Users/administrator/Desktop/clonedRepo/WD.Internal.PoC/Mobile/IOSDefendersPoC/KannupriyaInternDemo/findRecipe/findRecipe.xcodeproj/xcshareddata/xcbaselines/C34F493E27C47808003202A3.xcbaseline/7270C6BB-FC92-4790-AB38-E977E8599516.plist')
   
   if os.path.exists(fileName):

      pl=plistlib.readPlist(fileName)
      print('The plist full contents is %s\n' % pl)

      if 'classNames' in pl:
#         print('The aString value is %s\n' % pl['classNames'])
	if 'AddIngredientUnitTests' in pl['classNames']:
		print('The aString value is %s\n' % pl['classNames']['AddIngredientUnitTests'])
      else:
         print('There is no aString in the plist\n')

   else:
      print('%s does not exist, so can\'t be read' % fileName)

if __name__ == '__main__':
   main()


