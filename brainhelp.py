#! /usr/bin/python2
#


import platform
import sys



HELP="""
USAGE:brainhelp SUBJECT OBJECT

"""


class compiler(object):
	
	def __init__(self,code):
		self.code=code
	
	def phrase(self):
		pass
	


class brainhelp(object):
	
	### [empty] [back][data][steps][pointer]
	
	bh=""
	bf="###Struct###\n### [empty] [back][data][steps][pointer]###\n>>>>"
	variables={}
	variable_position=0
	
	def __init__(self,bh_code):
		self.bh=bh_code
	
	def extern(self,items=[]):
		for i in items:
			if i.startswith("*"):
				self.extern([i[1:],])
			self.variables[i]=self.variable_position
			self.variable_position+=1
	
	#This is the CORE PART
	def go(self,variable=0):
		if type(variable)==type('*') and variable.startswith("*"):
			self.go(variable[1:])
			self.bf+="[-<+<<<+>>>>]<<<<[->>>>+<<<<]>>>>>"
			self.back()
			self.bf+="<"
			self.go()	
		elif variable!=0:
			steps=self.variables[variable]
			self.bf+="<"+"+"*steps   #write steps into the tape
		self.bf+="[>[-<<<<+>>>>]"  #pointer to the left
		self.bf+="<[->+<]"*3+">+>>-]>"   #movement
	
	#This is the SECOND CORE PART	
	def back(self):
		self.bf+="<<<[-"   #preparing
		self.bf+="[-<+>]>"*3   #movement
		self.bf+="<<<<<[->>>>+<<<<]>]>>>"   #the left point to the right
	
	def malloc(self,pointer,length):
		self.go(pointer)
		self.bf+="+"*self.variable_position
		self.variable_position+=length+1
	
	def plus(self,items=[]):
		for i in items:
			try:
				backup=i
				i=str(i)
				if '"' in backup:
					i=ord(str(i))
					self.bf+="<<"+"+"*i+">>"
				else:
					self.go(i)
					self.bf+="[-<+<+>>]<[->+<]>"
					self.back()
			except:
				i=int(i)
				self.bf+="<<"+"+"*i+">>"
	
	def plus_assign(self,variable,items=[]):
		self.plus(items)
		
		self.go(variable)
		self.bf+="<<[->>+<<]>>"
		self.back()
	
	def minus_assign(self,variable,items=[]):
		first=items[0]
		self.plus(items[1:])
		
		try:
			dump=first
			first=str(first)
			if '"' in dump:
				first=ord(str(dump))
				self.bf+="<"+"+"*first
				self.bf+="<[->-<]>[-<+>]>"
			else:
				self.go(first)
				self.bf+="[-<+<<<+>>>>]<<<<[->>>>+<<<<-]>>[->-<]>[-<+>]>>"
				self.back()
		except:
			first=int(first)
			self.bf+="<"+"+"*first
			self.bf+="<[->-<]>[-<+>]>"
			
		self.go(variable)
		self.bf+="<<[->>+<<]>>"
		self.back()
	
	def input(self,variable):
		self.go(variable)
		self.bf+=",[>,]<[<]>>>>"
		self.back()
	
	def output(self,variable):
		self.go(variable)
		self.bf+="[>]<[<]>>>>"
		self.back()
	
	def compile(self):
		funcs=compiler(self.bh)
		funcs.phrase()
		
		
		




if __name__=="__main__":
	
	if not platform.python_version().startswith("2"):
		print ("This program needs Python 2.x")
		exit()
	
	argv=sys.argv
	if "help" in argv or "H" in argv or len(argv)<2:
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
	#bf.compile()
	
	n=1
	while n:
		exec(raw_input(">"))
	
	OUTPUT=bf.bf
	
	try:
		open(OBJECT,'w').write(OUTPUT)
	except:
		print(OUTPUT)

	exit()
