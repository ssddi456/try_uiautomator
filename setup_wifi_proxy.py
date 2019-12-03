# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
from subprocess import Popen

import socket

localip = socket.gethostbyname_ex(socket.gethostname())[-1][0]

deviceSerise = "172.30.21.109:5555"
# Popen('adb connect ' + deviceSerise)
d = u2.connect(deviceSerise)
# d.screen.on()

Popen('adb -s ' + deviceSerise + ' shell "am start -n com.android.settings/.Settings"')

def wait_and_click(**kwargs):
    d(**kwargs).wait(3)
    d(**kwargs).click()

print('click wlan setting')
wait_and_click(text='WLAN和互联网')
print('click wlan detail')
wait_and_click(text='WLAN')
wait_and_click(
    resourceId='com.android.settings:id/settings_button_no_background')
print('click current wifi detail')
wait_and_click(className='android.widget.TextView', index=0)

d(resourceId='com.android.settings:id/dialog_scrollview').wait(3)
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
d(resourceId='com.android.settings:id/dialog_scrollview').scroll.vert.forward(steps=30)

print('setup current wifi proxy config')
d(resourceId='com.android.settings:id/proxy_hostname').set_text(localip)
d(resourceId='com.android.settings:id/proxy_port').set_text('8888')

wait_and_click(
    index=1, className='android.widget.Button', text="保存")
