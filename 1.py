from ctypes import CDLL
a=CDLL("./Brainhelp_Shared.so")
b='2'
print a.char2int(b)
