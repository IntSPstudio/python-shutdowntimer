#|==============================================================|#
# Made by IntSPstudio
# Shutdown Timer
# Thank you for using this software!
# Version: 1.0.1.20161103
# ID: 980002001
#
# Twitter: @IntSPstudio
#|==============================================================|#

#SYSTEM
import os
import sys
import time

#CMD COLOR
#os.system("color a")

#BACKGROUND
bgdline = "----------------------------------------------------------------"

#BASIC VRB
continuity ="1"
mainPage ="0"
askSetTime =0
drawMainTime =0
mainTime =10

#TEXT
mainInfoText ='==] INFO\n  ]\n  ] Code: shutdown.exe /p /f \n  ]\n  ]\n  ]\n  ]\n  ]\n==]'
shutDownMessage ="Goodbye"

#MENU LOOP
while continuity == "1":
	#START COUNTDOWN
	if mainPage == "1":
		#TIMING
		for i in range(0,mainTime):
			#TA
			os.system("cls")
			drawMainTime = mainTime -i
			#TB
			print(bgdline)
			print("==]")
			print("  ]")
			print("  ]")
			print("  ] Computer is shutting down in",drawMainTime,"minutes")
			print("  ]")
			print("  ]",shutDownMessage)
			print("  ]")
			print("  ]")
			print("==]")
			#TC
			time.sleep(60)
		#TA
		os.system("cls")
		os.system("shutdown.exe /p /f")
		#TB
		print(bgdline)
		print("==]")
		print("  ]")
		print("  ]")
		print("  ]")
		print("  ] Computer is shutting down...")
		print("  ]")
		print("  ]")
		print("  ]")
		print("==]")
		#TC
		wtmn =input("")
		continuity ="0"
	#SET TIME
	elif mainPage == "2":
		#TA
		os.system("cls")
		#TB
		print(bgdline)
		#TC
		askSetTime = input("==] How many minutes?: ")
		if askSetTime != "":
			mainTime = int(askSetTime)
		mainPage ="0"
	#SET MESSAGE
	elif mainPage == "3":
		#TA
		os.system("cls")
		#TB
		print(bgdline)
		#TC
		shutDownMessage = input("==] Shutdown message: ")
		if shutDownMessage == "":
			shutDownMessage ="Goodbye"
		mainPage ="0"
	#INFO
	elif mainPage == "4":
		#TA
		os.system("cls")
		#TB
		print(bgdline)
		print(mainInfoText)
		#TC
		wtmn =input("")
		mainPage ="0"
	#EXIT
	elif mainPage == "5":
		#TA
		os.system("cls")
		continuity ="0"
	#MENU
	else:
		#TA
		os.system("cls")
		drawMainTime = mainTime
		#TB
		print(bgdline)
		print("==] MENU")
		print("  ]")
		print(" 1] Start countdown")
		print(" 2] Set time ["+str(drawMainTime)+"min]")
		print(" 3] Set message ["+shutDownMessage+"]")
		print(" 4] Info")
		print(" 5] Exit")
		print("  ]")
		mainPage =input("==] Select the number: ")
