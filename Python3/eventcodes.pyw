#!/usr/env/python3

import webbrowser
import requests
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

root = Tk()
root.title("Event Code Search")
root.geometry('350x150+500+350')

winLabel = Label(root, text="Log Source:").place(x=20, y=5)
winVar = IntVar()
winButton = Checkbutton(root, text="Windows", variable=winVar).place(x=20, y=30)
sysmVar = IntVar()
sysmButton = Checkbutton(root, text="Sysmon", variable=sysmVar).place(x=20, y=55)
appLockVar = IntVar()
appLockButton = Checkbutton(root, text="AppLocker", variable=appLockVar).place(x=20, y=80)
instVar = IntVar()
instButton = Checkbutton(root, text="Installer", variable=instVar).place(x=20, y=105)
inputLabel = Label(root, text="Event Code:").place(x=150, y=30)
codeVar = StringVar()
eventCode = Entry(root, textvariable=codeVar, width=10).place(x=150,y=55)
sysmonCodes = list(range(1, 25))
appLockerCodes = [8000, 8001, 8002, 8003, 8004, 8005, 8006, 8007, 8008, 8020, 8021, 8022, 8023, 8024, 8025, 8027, 8028, 8029, 8030, 8031, 8032, 8033, 8034, 8035, 8036, 8037, 8038, 8039, 8040]

def submit():

	srcWin = winVar.get()
	srcSysm = sysmVar.get()
	srcAppLock = appLockVar.get()
	srcInst = instVar.get()
	code = codeVar.get()
	checked = 0
	sources = [srcWin, srcSysm, srcAppLock, srcInst]
	
	for src in sources:
		if src:
			checked = checked + 1
	if checked > 1:
		msg = tkinter.messagebox.showinfo("Error!", "You can only select one source.")
		return
	if checked == 0:
		msg = tkinter.messagebox.showinfo("Error!", "You must select a log source.")
		return
	if code and srcInst:
		msg = tkinter.messagebox.showinfo("Error!", "Do not provide an event code if selecting the 'Installer' log source.")
		return
	if (checked == 1 and not srcInst) and not code: 
		msg = tkinter.messagebox.showinfo("Error!", "Please input an event code.")
		return
	
	if srcWin:
		url = 'https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=' + code
		check = requests.get(url)
		if check.url == "https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/":
			msg = tkinter.messagebox.showinfo("Error!", f"Event Code {code} does not exist in this database. Please make sure you typed the correct event code")
			return
		else:
			webbrowser.open_new_tab(url)
			exit()
	elif srcSysm:
		if int(code) in sysmonCodes:
			if len(code) == 1:
				url = "https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=9000" + code
				webbrowser.open_new_tab(url)
				exit()
			elif len(code) == 2:
				url = "https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=900" + code
				webbrowser.open_new_tab(url)
				exit()
		else:
			msg = tkinter.messagebox.showinfo("Error!", f"{code} is an invalid Sysmon event code.")
			return
	elif srcAppLock:
		if int(code) in appLockerCodes:
			url = "https://system32.eventsentry.com/applocker/event/" + str(code)
			webbrowser.open_new_tab(url)
			exit()
		else:
			msg = tkinter.messagebox.showinfo("Error!", f"{code} is an invalid AppLocker event code.")
			return
	elif srcInst:
		url = "https://learn.microsoft.com/en-us/windows/win32/msi/event-logging"
		webbrowser.open_new_tab(url)
		exit()

#Submit button
submit = Button(root, text="Submit", command=submit).place(x=150, y=90)

#Let it roll 
root.mainloop()
