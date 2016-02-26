#coding: utf-8
import os
import win32api
flag = 0

def dumpA():
	while flag==0:
		symPath = raw_input('input symbol path: ')
		dumpPath = raw_input("input dump file path: ")
		flag = 1
	
	a = 'cdb -z ' + dumpPath + ' -y ' + symPath +' -logo out.txt -lines -c "!analyze -v;q"'
	print a
	os.system(a)
# os.system('cdb -z dumpPath -y symPath -logo out.txt -lines -c "!analyze -v;q"')