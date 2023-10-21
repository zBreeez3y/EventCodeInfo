# EventCodeInfo
A simple script with a GUI to quickly look up Windows event codes.

This script gives you a quick and easy way to pull up the details on an Event ID you come across when digging through logs. You can look up ID's from Windows native events, Sysmon, Applocker and Installer sources
  - I haven't found a suitable source for Installer logs yet, so for now I'm just having the script pull up the Microsoft documentation on it which displays all the codes on a single page. Due to this, the way to jump to the ID you're looking for would be to search the page for it. I didn't want to allow the script to interact with your browser any further than just loading the webpage, so for now it will just load that page and you scroll to find the code. It's not that many anyways :)

#### Note
I intended the script to be turned into either an Application (macOS) or an Executable (Windows using Pyinstaller) so I could pin it to my Dock/Taskbar and use it at the click of a button, so I have provided instructions on converting the scripts below

## Installation
### Windows
1. Download the Python3 version of EventCodeInfo and move the file to your preferred directory
2. Download and install Python3 to your Windows host
   - This can be done via the Microsoft store, or the Python <a href="https://www.python.org/downloads/">downloads</a> page.
3. Download and install Pyinstaller via PIP
   -     python3 -m pip install pyinstaller
4.  Run Pyinstaller and provide the EventCodeInfo script as the argument
    -     pyinstaller eventcodes.pyw
    - If you receive a "command not found" error, ensure you have the PyInstaller binaries path added to your %PATH%. To find the binaries path, you can type the following into CMD:
      -     where pyinstaller.exe
5. The EventCodes exectuable will be in the "\dist\eventcodes\" directory that's created from running PyInstaller. Find "eventcodes.exe", right-click and select "Pin to taskbar" 

### macOS
1. Download the AppleScript version of EventCodeInfo and move the file to your preferred directory
2. Open the script with the Script Editor application
3. Select File->Export
4. Change the file format from "Script" to "Application" and save the file
5. Control-click the ".app" file and add to dock
#### Note
You can also use the Python3 version on macOS. I installed Homebrew and reinstalled Python3 through that which uses a version of the Tkinter module that works correctly on macOS. 
