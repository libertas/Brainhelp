#! /usr/bin/env python3
# Brainhelp compiler
from sys import argv
from os import system
try:
	bh=argv[1]
except:
	print("bh:input error")
	exit()
try:
	elf=argv[2]
except:
	elf="a.out"

cout=0
if bh.endswith(".bh"):
	system("brainhelp "+bh+" "+bh+".bf")
	cout=1
	bh+=".bf"
	
if bh.endswith(".bf") or bh.endswith(".b"):
	system("awib <"+bh+" >"+bh+".c")
	if cout==1:
		system("rm "+bh)
	cout=2
	bh+=".c"

if bh.endswith(".c"):
	system("gcc -o "+elf+" "+bh)
	if cout==2:
		system("rm "+bh)
