#!/usr/bin/python
import sys
from AppKit import NSScreen
from ScriptingBridge import SBApplication

terminal=SBApplication.applicationWithBundleIdentifier_("com.apple.Terminal")
t_window=terminal.windows()[0]

if sys.argv[1]=="c":
	screen_height = NSScreen.mainScreen().frame().size.height
	screen_width = NSScreen.mainScreen().frame().size.width
	s_x=t_window.size().x
	s_y=t_window.size().y
	
	new_x=screen_width/2-s_x/2
	new_y=screen_height/2-s_y/2-15
	toPrint="Window centered"
elif sys.argv[1]=="m":
	factor=1.6
	s_x=570*factor
	s_y=390*factor
	new_x=t_window.position().x+(t_window.size().x-570*factor)/2
	new_y=t_window.position().y+(t_window.size().y-390*factor)/2
	toPrint="Medium size: {} by {}".format(s_x,s_y)
elif sys.argv[1]=="b":
	factor=2
	screen_height = NSScreen.mainScreen().frame().size.height
	screen_width = NSScreen.mainScreen().frame().size.width
	
	s_x=570*factor
	s_y=390*factor
	new_x=(screen_width-s_x)/2
	new_y=(screen_height-s_y)/2-15
	toPrint="Large size: {} by {}".format(s_x,s_y)
else:
	new_x=t_window.position().x+(t_window.size().x-570)/2
	new_y=t_window.position().y+(t_window.size().y-390)/2
	s_x=570
	s_y=390
	toPrint="Small size (default): {} by {}".format(s_x,s_y)

if s_x!=t_window.size().x or sys.argv[1]=="c":
	t_window.setBounds_([[new_x, new_y], [s_x, s_y]])
print(toPrint)
