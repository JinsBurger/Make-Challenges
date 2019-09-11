#gdb --command run_gdb.py
import gdb
import time
import os
import signal
import sys

#signal.alarm(10)

print('''      ___       ___  __   __         ___    ___  __      __   __   __  
|  | |__  |    |__  /  ` /  \\  |\\/| |__      |  /  \\    / _` |  \\ |__) 
|/\\| |___ |___ |___ \\__, \\__/  |  | |___     |  \\__/    \\__> |__/ |__) 
                                                                      ''')

try :
	command = input("gdb command : ")

	print("Running ...")
	time.sleep(1)

	for i in range(0,len(command)-1) :
		if command[i].isalpha() :
			print("no")
			sys.exit()

	gdb.execute(command)
	gdb.execute("quit")

except:
	sys.exit()
