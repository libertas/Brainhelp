#! /usr/bin/env python3
from sys import argv
from os import system
try:
	bf=argv[1]
except:
	print("bf:input error")
	exit()
try:
	elf=argv[2]
except:
	elf="a.out"

system("awib <"+bf+" >"+bf+".c")
system("gcc -o "+elf+" "+bf+".c")
system("rm "+bf+".c")
