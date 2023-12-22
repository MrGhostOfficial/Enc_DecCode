# -*- coding=utf-8 -*-
#MrGhostOfficial[NetHunter]
#Binary_: 01010011 01101111 01101101 01110010 01100001 01100001 01110100
#Mystylecustommodifiedcolorcode*
#Normal below are the colors
yellow = '\033[1;33m'
black = '\033[1;30m'
red = '\033[1;31m'
whitelite = '\033[0;37m'
finished = '\033[0m'
#×××××××××××××××××××××××××××××××××××:
import os
file = open(raw_input(black +"┌─["+ red +"Input"+ black +" /sdcard/Download/\n"+ black +"└─["+ red +"Decrypt"+ black +"]"+ whitelite +"> "+ yellow)).read()
percobaan = 0
while True:
	if "exec" in file and "marshal" in file and "import" in file:
		kontol = file.replace("exec","x = ")
		percobaan += 1
		print("\033[31m - \033[00mMembuka ke > \033[36m" + str(percobaan))
	else:
		print("\n" +file)
		try:
			os.remove("sc.py")
			print("\n \033[31m - \033[00mBerhasil \033[32m✓")
		except:
			print("\n \033[31m - \033[00mgagal Mampus Tobat Bro \033[31m !")
		break
	sc = """from sys import stdout
import marshal
from uncompyle6.main import decompile
"""+kontol+"""
decompile(2.7,x, stdout) """
        open("sc.py","w").write(sc)
        os.system("python2 sc.py > decom.py")
        file = open("decom.py").read()