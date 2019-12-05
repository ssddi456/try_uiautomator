# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
from subprocess import Popen
from optparse import OptionParser


import socket

localip = socket.gethostbyname_ex(socket.gethostname())[-1][0]

parser = OptionParser()
parser.add_option("-s", "--series", dest="series",
                  help="adb device series", metavar="SERIES")
(options, args) = parser.parse_args()

deviceSerise = options.series


if deviceSerise == None:
    raise 'you muse input series for adb'
# Popen('adb connect ' + deviceSerise)
# d.screen.on()
d = u2.connect(deviceSerise)

Popen('adb -s ' + deviceSerise +
      ' shell "am start -n com.android.settings/.Settings"')

d = u2.connect(deviceSerise)

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
d.press("back")

d(resourceId='com.android.settings:id/dialog_scrollview').scroll.vert.forward(steps=10)
print('click current wifi proxy config')
wait_and_click(
    resourceId='com.android.settings:id/proxy_settings')
wait_and_click(
    index=1, className='android.widget.CheckedTextView')
d(resourceId='com.android.settings:id/dialog_scrollview').scroll.vert.forward(steps=30)

print('setup current wifi proxy config')
d(resourceId='com.android.settings:id/proxy_hostname').set_text(localip)
d.press("back")
d(resourceId='com.android.settings:id/proxy_port').set_text('8888')
d.press("back")

wait_and_click(
    index=1, className='android.widget.Button', text="保存")
