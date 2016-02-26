#coding: utf-8
import subprocess
from Tkinter import *
import os
import socket
import sys
import struct  
import time  
# print sys.path
import win32api  
import win32file
import win32con
import time
import socket

root = Tk()
root.title('Test Tool Fast Access')
root.geometry('830x210')
root.resizable(width = True, height = False)

TimeServer = 'cn.pool.ntp.org' #国家授时中心ip  
Port = 123  

#国家授时中心获取时间
def getTime():  
    TIME_1970 = 2208988800L  #
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    data = '\x1b' + 47 * '\0' #'\x23' 展开为 00 100 011 分别填充LI, VN, Mode字段
    #余下的47 * 8 = 376位都填充0
    client.sendto(data, (TimeServer, Port)) #报文+地址 
    data, address = client.recvfrom(1024)  
    data_result = struct.unpack('!12I', data)[10]  #
    data_result -= TIME_1970  #
    return data_result  

#修改本地计算机时间  
def setSystemTime(a):
	try:  
		print time.gmtime(getTime())
		tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = time.gmtime(getTime())  
    	#time.gmtime([secs]) 接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0.参数默认值为time.time()
		if a == 'addOneDay':
			tm_mday = tm_mday + 1
		elif a == 'reduceOneDay':
			tm_mday = tm_mday - 1
		elif a == 'addOneHour':
			tm_hour = tm_hour + 1
		elif a == 'reduceOneHour':
			tm_hour = tm_hour - 1
		elif a == 'keepSyn':
			pass    				
		win32api.SetSystemTime(tm_year, tm_mon, tm_wday, tm_mday, tm_hour, tm_min, tm_sec, 0)
	except Exception as e:
		print e


def dumpA(flag):
	while flag==0:
		symPath = raw_input('input symbol path: ')
		dumpPath = raw_input("input dump file path: ")
		flag = 1
	
	# os.system('D:\windbg\cdb.exe')	
	a = 'cdb -z ' + '"' + dumpPath +'"' + ' -y ' + '"' + symPath + '"' +' -logo out.txt -lines -c "!analyze -v;q"'
	os.system(a)

def startProcess(fun):
	currentPath = os.path.abspath('.')
	if fun == 'notepad':
		win32api.ShellExecute(0, 'open', 'notepad.exe','','',1) #1 前台运行
	elif fun == 'DataMonitor':
		win32api.ShellExecute(0, 'open', 'KuGouDataMonitor.exe','','',1)
	elif fun == 'Hashcal':	
		win32api.ShellExecute(0, 'open', 'HashCalc.exe','','',1)
	elif fun == 'PDataProcess':	
		win32api.ShellExecute(0, 'open', 'PDataProcessClient.exe','','',1)
	elif fun == 'QR':
		win32api.ShellExecute(0, 'open', 'PsQREdit.exe','','',1)
	elif fun == 'regedit':
		win32api.ShellExecute(0, 'open', 'regedit.exe','','',1)
	elif fun == 'fidder':	
		win32api.ShellExecute(0, 'open', 'Fiddler.exe','','',1)
	elif fun == 'wireShark':	
		win32api.ShellExecute(0, 'open', 'wireShark.exe','','',1)
	elif fun == 'PE':	
		win32api.ShellExecute(0, 'open', 'procexp.exe','','',1)
	elif fun == 'SQL':
		sqlPath = currentPath + '\sqlite\sqlitebrowser.exe'
		win32api.ShellExecute(0, 'open', sqlPath,'','',1)
	elif fun == 'Windbg':
		WindgPath = currentPath + '\Windbg\Windbg.exe'	
		win32api.ShellExecute(0, 'open',WindgPath,'','',1)
	elif fun == 'TCPView':		
		TCPViewPath = currentPath + '\\360TCPView\\360tcpview.exe'	
		win32api.ShellExecute(0, 'open',TCPViewPath,'','',1)
	elif fun == 'CCproxy':
		CCproxyPath = currentPath + '\\CCProxy\\CCProxy.exe'	
		win32api.ShellExecute(0, 'open',CCproxyPath,'','',1)			
	elif fun == 'sublime':
		sublimePath = currentPath + '\\Sublime\\sublime_text.exe'
		win32api.ShellExecute(0, 'open', sublimePath,'','',1)
	elif fun == ('geshouxiezhen'):
		win32api.ShellExecute(0, 'open','readsourcefile.exe','','',1)
	elif fun == 'decrypt':
		win32api.ShellExecute(0, 'open', 'decrypt.exe','','',1)
	elif fun == 'spy':	
		SpyPath = currentPath + '\\spy\\spyxx.exe'		
		win32api.ShellExecute(0, 'open',SpyPath,'','',1)
	elif fun == 'HttpA':		
		Path1 = currentPath + '\\HTTPAnalyzerFullV7\\HttpAnalyzerStdV7.exe'	
		win32api.ShellExecute(0,'open',Path1,'','',1)
	elif fun == 'killprocess':		
		os.system('taskkill /f /im kugou.exe /t')
	elif fun == '绑定Host':		
		win32api.ShellExecute(0, 'open','notepad.exe','C:\Windows\System32\Drivers\etc\hosts','',1)
	elif fun == 'dump':
		dumpA(flag = 0)


Label(root,text = u'酷狗专用测试工具',bg = 'yellow').grid()
# Button(root,text = u'歌词解密',relief = RAISED).grid(row = 0,column = 1)
Button(root,text = u'Sqlite',relief = RAISED,command = lambda:startProcess('SQL')).grid(row = 0,column = 2)
# Button(root,text = u'音效插件',relief = RAISED).grid(row = 0,column = 3)
Button(root,text = 'kill process',relief = RAISED,command = lambda:startProcess('killprocess')).grid(row = 0,column = 4)
Button(root,text = u'统计监控',relief = RAISED,command = lambda:startProcess('DataMonitor')).grid(row = 0,column = 3)
Button(root,text = u'数据分析',relief = RAISED,command = lambda:startProcess('PDataProcess')).grid(row = 0,column = 1)
Button(root,text = u'歌手写真资源编辑器',relief = RAISED,command = lambda:startProcess('geshouxiezhen')).grid(row = 0,column = 5)

Label(root,text = u'抓包/代理',bg = 'yellow').grid(row = 7)
Button(root,text = 'CCproxy',relief = RAISED,command = lambda:startProcess('CCproxy')).grid(row = 7,column = 2)
Button(root,text = 'HTTPAnalyser',relief = RAISED,command = lambda:startProcess('HttpA')).grid(row = 7,column = 3)
Button(root,text = 'Fiddler',relief = RAISED,command = lambda:startProcess('fidder')).grid(row = 7,column = 1)
Button(root,text = 'Wireshake',relief = RAISED,command = lambda:startProcess('wireShark')).grid(row = 7,column = 4)

Label(root,text = u'进程监控',bg = 'yellow').grid(row = 2)
Button(root,text = 'Process Monitor',relief = RAISED,fg="red",command = lambda:startProcess('Process Monitor')).grid(row = 2,column = 2)
Button(root,text = u'Procexp',relief = RAISED,command = lambda:startProcess('PE')).grid(row = 2,column = 1)

Label(root,text = u'windows实用工具',bg = 'yellow').grid(row = 3)
Button(root,text = 'windb',relief = RAISED,command = lambda:startProcess('Windbg')).grid(row = 3,column = 1)
Button(root,text = 'spy',relief = RAISED,command = lambda:startProcess('spy')).grid(row = 3,column = 2)
Button(root,text = 'Hashcal',relief = RAISED,command = lambda:startProcess('Hashcal')).grid(row = 3,column = 3)
Button(root,text = u'QR识别',relief = RAISED,command = lambda:startProcess('QR')).grid(row = 3,column = 4)


Label(root,text = u'加密解密',bg = 'yellow').grid(row = 4)
Button(root,text = 'decrypt',relief = RAISED,command = lambda:startProcess('decrypt')).grid(row = 4,column = 1)
Button(root,text = 'urlencode',fg="red",relief = RAISED).grid(row = 4,column = 2)
Button(root,text = 'MD5',fg="red",relief = RAISED).grid(row = 4,column = 3)


Label(root,text = u'时间调节',bg = 'yellow').grid(row = 6)
Button(root,text = '+1D',fg="red",relief = RAISED,command = lambda:setSystemTime('addOneDay')).grid(row = 6,column = 4)
Button(root,text = '-1D',fg="red",relief = RAISED,command = lambda:setSystemTime('reduceOneDay')).grid(row = 6,column = 5)
Button(root,text = '+1H',fg="red",relief = RAISED,command = lambda:setSystemTime('addOneHour')).grid(row = 6,column = 2)
Button(root,text = '-1H',fg="red",relief = RAISED,command = lambda:setSystemTime('reduceOneHour')).grid(row = 6,column = 3)
Button(root,text = u'校准时间',relief = RAISED,command = lambda:setSystemTime('keepSyn')).grid(row = 6,column = 1)


Label(root,text = u'快速入口',bg = 'yellow').grid(row = 5)
Button(root,text = 'dump文件解析',relief = RAISED,command = lambda:startProcess('dump')).grid(row = 5,column = 6)
Button(root,text = 'NotePad',relief = RAISED,command = lambda:startProcess('notepad')).grid(row = 5,column = 1)
# a.bind('<Button-1>',startProcess)
Button(root,text = 'Host',relief = RAISED,command = lambda:startProcess('绑定Host')).grid(row = 5,column = 3)
Button(root,text = u'Host无法保存',fg="red",relief = RAISED).grid(row = 5,column = 7)
Button(root,text = 'Sublime',relief = RAISED,command = lambda:startProcess('sublime')).grid(row = 5,column = 2)
# Label(root,text = u'注册表',bg = 'yellow').grid(row = 5)
Button(root,text = 'Regedit',relief = RAISED,command = lambda:startProcess(u'注册表')).grid(row = 5,column = 4)
Button(root,text = u'独占工具',fg="red",relief = RAISED).grid(row = 5,column = 8)
Button(root,text = u'网络流量监控',relief = RAISED,command = lambda:startProcess('TCPView')).grid(row = 5,column = 5)

# Label(root,text = u'dump文件解析需先安装windbg').grid(row = 8)

# photo = PhotoImage(file='kugou2.gif')
# label = Label(image=photo)
# label.image = photo
# label.grid(row=1, column=6, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)

root.mainloop()