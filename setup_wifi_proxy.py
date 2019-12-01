# -*- coding: utf-8 -*-

from uiautomator import Device
import time
from subprocess import Popen

d = Device("192.168.1.110:5555")
d.screen.on()

Popen('adb shell "am start -n com.android.settings/.Settings"')

def wait_and_click(**kwargs):
    d(**kwargs).wait.exists(timeout=3000)
    d(**kwargs).click()

print('click wlan setting')
wait_and_click(text='WLAN和互联网')
print('click wlan detail')
wait_and_click(text='WLAN')
wait_and_click(
    resourceId='com.android.settings:id/settings_button_no_background')
print('click current wifi detail')
wait_and_click(className='android.widget.TextView', index=0)

d(resourceId='com.android.settings:id/dialog_scrollview').wait.exists(timeout=3000)
d(resourceId='com.android.settings:id/dialog_scrollview').scroll.vert.forward(steps=10)

print('click current wifi advanted detail')
wait_and_click(
    resourceId='com.android.settings:id/wifi_advanced_togglebox')

d(resourceId='com.android.settings:id/dialog_scrollview').scroll.vert.forward(steps=10)
print('click current wifi proxy config')
wait_and_click(
    resourceId='com.android.settings:id/proxy_settings')
wait_and_click(
    index=1, className='android.widget.CheckedTextView')
d(resourceId='com.android.settings:id/dialog_scrollview').scroll.vert.forward(steps=20)

print('setup current wifi proxy config')
d(resourceId='com.android.settings:id/proxy_hostname').set_text('192.168.1.112')
d(resourceId='com.android.settings:id/proxy_port').set_text('8888')

wait_and_click(
    index=1, className='android.widget.Button', text="保存")
