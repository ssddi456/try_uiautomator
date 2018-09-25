# -*- coding: utf-8 -*-  1

from uiautomator import Device
import time
from subprocess import Popen
d = Device("ba1d4eb6")
print d.info
d.screen.on()

Popen('adb shell am force-stop com.eg.android.AlipayGphone')
time.sleep(1)
Popen('adb shell am start -n com.eg.android.AlipayGphone/com.eg.android.AlipayGphone.AlipayLogin')
time.sleep(1)

d.wait.update()
d(text=u"扫一扫").click()
d.wait.update()
d(text=u"相册").click()
d.wait.update()
d(resourceId=u"com.alipay.mobile.beehive:id/iv_photo",instance=0).click()
time.sleep(3)
d.wait.update()
xml = d.dump()
print xml.encode('utf-8')
