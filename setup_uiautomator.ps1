$device = "192.168.1.110:5555"
@echo off
echo "start uiautomator"
adb -s $device shell am start -n com.github.uiautomator/.MainActivity
echo "setup port forward"
adb -s $device forward tcp:9008 tcp:9008
echo "start test stub"
:loop
adb -s $device shell am instrument -w com.github.uiautomator.test/android.support.test.runner.AndroidJUnitRunner
goto loop
@echo on