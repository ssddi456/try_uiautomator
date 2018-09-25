@echo off
echo "start uiautomator"
adb shell am start -n com.github.uiautomator/.MainActivity
echo "setup port forward"
adb forward tcp:9008 tcp:9008
echo "start test stub"
:loop
adb shell am instrument -w com.github.uiautomator.test/android.support.test.runner.AndroidJUnitRunner
goto loop
@echo on