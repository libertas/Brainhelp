#! /usr/bin/python2
import platform
import sys


HELP="""
USAGE:brainhelp SUBJECT OBJECT

"""


class brainhelp(OBJECT,str):
	bh=""
	bf=">>"
	variables={}
	variable_pointer=0
	
	def __init__(self,bh_code):
		bh=bh_code
	
	def show(self,items=[]):
		for i in items:
			variables[i]=variable_pointer
			variable_pointer+=1
	
	def go(self,variable):
		steps=variables[variable]
		
	
	def back(self,):
		
	
	def malloc(self,pointer,length):
		variable_pointer+=length
		self.go(pointer)
		



if __name__=="__main__":
	
	if not platform.python_version().startswith("2"):
		print ("This program needs Python 2.x")
	
	argv=sys.argv
	if "help" in argv or "H" in argv:
		print(HELP)
		exit()
	else:
		SUBJECT=argv[1]
		OBJECT=argv[2]
	
	try:
		INPUT=open(SUBJECT,'r').read()
	except:
		print("Input file error")
		exit()
	
	bf=brainhelp(INPUT)
	
