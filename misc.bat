rem list activity
adb shell dumpsys activity activities 
rem list window
adb shell dumpsys window windows
rem current window
adb shell dumpsys window windows | grep current
