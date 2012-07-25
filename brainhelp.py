#! /usr/bin/python2
#


import platform
import sys



HELP="""
USAGE:brainhelp SUBJECT OBJECT

"""
					



class brainhelp(object):
	
	### [empty] [back][data][steps][pointer]
	
	bh=[]
	bf="###Struct###\n### [empty] [back][data][steps][pointer]###\n>>>>"
	variables={}
	variable_position=0
	
	def __init__(self,bh_code):
		self.bh=bh_code
	
	def run(self):
		for i in self.bh:
			exec("self."+i)
	
	def bfchar(self,*items):
		for i in items:
			if i.startswith("*"):
				self.bfchar([i[1:],])
			else:
				self.variables[i]=self.variable_position
				self.variable_position+=1
	
	#This is the CORE PART
	def go(self,variable=0):
		if type(variable)==type('*') and variable.startswith("*"):
			self.go(variable[1:])
			self.bf+="[-<+<<<+>>>>]<<<<[->>>>+<<<<]>>>>"
			self.back()
			self.bf+="<"	
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
		self.back()
	
	def plus(self,items):
		for i in items:
			if type(i) == type(1):
				self.bf+="<<"+"+"*i+">>"
			elif type(i) == type("1"):
				backup=i
				i=str(i)
				if '"' in backup:
					end=len(i)-1
					i=ord(i[1:end])
					self.plus([i])
				else:
					self.go(i)
					self.bf+="[-<+<+>>]<[->+<]>"
					self.back()
			
	
	def plus_assign(self,variable,*items):
		self.plus(items)
		self.go(variable)
		self.bf+="[-]<<[->>+<<]>>"
		self.back()
	
	def minus_assign(self,variable,*items):
		first=items[0]
		self.plus(items[1:])
		
		if type(first)==type('1'):
			temp=first
			first=str(first)
			if '"' in temp:
				end=len(first)-1
				first=ord(first[1:end])
				self.bf+="<"+"+"*first
				self.bf+="<[->-<]>[-<+>]>"
			else:
				self.go(first)
				self.bf+="[-<+<<<+>>>>]<<<<[->>>>+<<<<]>>[->-<]>[-<+>]>"
				self.back()
		elif type(first)==type(1):
			first=int(first)
			self.bf+="<"+"+"*first
			self.bf+="<[->-<]>[-<+>]>"
			
		self.go(variable)
		self.bf+="[-]<<[->>+<<]>>"
		self.back()
	
	def input(self,variable):
		self.go(variable)
		self.bf+=",[>,]<[<]>>>>"
		self.back()
	
	def output(self,variable=0):
		if not '"' in variable:
			self.go(variable)
			self.bf+="[>]<[<]>>>>"
			self.back()
		elif '"' in variable:
			end=len(variable)-1
			text=variable[1:end]
			self.bf+="<<<<"
			for i in text:
				self.bf+="+"*ord(i)
				self.bf+="[-]"
			self.bf+=">>>>"
			
	
	def startwhile(self,variable):
		self.go(variable)
		self.bf+="["
		self.back()
		
	def endwhile(self,variable):
		self.go(variable)
		self.bf+="]"
		self.back()
	
	def startif(self,variable):
		self.startwhile(variable)
	
	def endif(self,variable=0):
		self.bf+="<<<<]>>>>"
		 
	def opposite(self,variable):
		self.go(variable)
		self.bf+="<+>[<[-]>][-]<[->+<]>"
	
		

def phrase(code=""):
	IGNORE="""}	"""
	result=[]
	tmp=""
	
	for i in code:
		
		if i in IGNORE:
			pass
			
		elif i ==";" or i =="{":
			result.append(tmp)
			tmp=""
		
		else:
			tmp+=i
	
	tmp=result
	result=[]
	
	for i in tmp:
		if not i.startswith("#"):
			result.append(i)
			
	return result
	




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
	
	INPUT=phrase(INPUT)
	bf=brainhelp(INPUT)
	bf.run()
	
	
	OUTPUT=bf.bf
	
	try:
		open(OBJECT,'w').write(OUTPUT)
	except:
		print(OUTPUT)

	exit()
