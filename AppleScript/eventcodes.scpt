set sourceOptions to {"Windows", "Sysmon", "AppLocker", "Installer"}
set appLockerCodes to {"8000", "8001", "8002", "8003", "8004", "8005", "8006", "8007", "8008", "8020", "8021", "8022", "8023", "8024", "8025", "8027", "8028", "8029", "8030", "8031", "8032", "8033", "8034", "8035", "8036", "8037", "8038", "8039", "8040"}
set sysmonCodes to {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"}
set theLoop to true
set source to choose from list sourceOptions with prompt "Select Log Source:"
if source is false then
	error number -128
end if
if source contains "Installer" then
	set theUrl to "https://learn.microsoft.com/en-us/windows/win32/msi/event-logging"
	open location theUrl
	error number -128
end if
set theLoop to true
repeat while (theLoop is true)
	set response to display dialog "What event code would you like to search?" default answer ""
	set eventcode to (text returned of response)
	if source contains "Windows" then
		set theLoop to false
		set theUrl to "https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=" & eventcode
	else if source contains "Sysmon" then
		if eventcode is in sysmonCodes then
			set theLoop to false
			if length of eventcode is equal to 2 then
				set theUrl to "https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=900" & eventcode
			else if length of eventcode is equal to 1 then
				set theUrl to "https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=9000" & eventcode
			end if
		else
			display dialog eventcode & " is not a valid Sysmon code."
			set theLoop to true
		end if
	else if source contains "AppLocker" then
		if eventcode is in appLockerCodes then
			set theLoop to false
			set theUrl to "https://system32.eventsentry.com/applocker/event/" & eventcode
		else
			display dialog eventcode & " is not a valid Applocker Event code."
			set theLoop to true
		end if
	end if
	if theLoop is false then
		try
			if source contains "Windows" then
				do shell script "curl " & theUrl
				if result contains "Object moved" then
					display dialog "Event code " & eventcode & " does not exist in this database. Please make sure you typed the correct Event code"
					set theLoop to true
				else
					open location theUrl
				end if
			else
				open location theUrl
			end if
		end try
	end if
end repeat
