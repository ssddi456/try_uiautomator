@echo off
echo "--- android home           ---"
echo %ANDROID_HOME%
echo "--- java home              ---"
echo %JAVA_HOME%
echo "--- if uiautomator install ---"
adb shell pm list packages | grep uiautomator
echo "--- if uiautomator alive   ---"
adb shell ps | grep uiautomator
echo "--- if port forward exists ---"
adb forward --list
echo "--- if port listening      ---"
adb shell netstat -lpn | grep 9008
echo "--- if server echo         ---"
curl -d '{"jsonrpc":"2.0","method":"deviceInfo","id":1}' localhost:9008/jsonrpc/0
@echo on