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
	ending=".bf"
	if elf.endswith(".b"):
		ending=".b"
	system("brainhelp "+bh+" "+bh[:-3]+ending)
	if elf.endswith(".bf") or elf.endswith(".b"):
		exit(0)
	cout=1
	bh=bh[:-3]
	bh+=".bf"
	
if bh.endswith(".bf") or bh.endswith(".b"):
	if bh.endswith(".bf"):
		bh_c=-3
	elif bh.endswith(".b"):
		bh_c=-2
	system("awibh <"+bh+" >"+bh[:bh_c]+".c")
	if cout==1:
		system("rm "+bh)
	if elf.endswith(".c"):
		exit(0)
	cout=2
	bh=bh[:bh_c]
	bh+=".c"

if bh.endswith(".c"):
	system("gcc -o "+elf+" "+bh)
	if cout==2:
		system("rm "+bh)
