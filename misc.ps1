
$device = "192.168.1.110:5555"
adb connect $device
echo "list activity"
adb -s $device shell dumpsys activity activities 
echo "list window"
adb -s $device shell dumpsys window windows
echo "current window"
adb -s $device shell "dumpsys window windows | grep current"
echo "current activity"
adb -s $device shell "dumpsys activity activities | grep ResumedActivity"

