# -*- coding: utf-8 -*-  1
from urllib import urlencode
import urllib2 as urllib
import json



opener = urllib.build_opener(urllib.ProxyHandler({}))
urllib.install_opener(opener)

def read_json( req ) :
  # force no proxy
  resp = urllib.urlopen(req)
  return json.loads(resp.read().decode('utf8', 'ignore'))

def http_post ( url, body ):
  req = urllib.Request(url, body, headers= { 'content-type': 'application/json'})
  req.get_method = lambda : 'POST'
  return read_json(req)

def http_get (url):
  req = urllib.Request(url)
  req.get_method = lambda : 'GET'
  return read_json(req)


from uiautomator import Device
import time
from subprocess import Popen

d = Device("ba1d4eb6")
d.screen.on()

with open('config.json') as f:
  qrcodeIndex = json.loads(f.read())

print qrcodeIndex

report_url = 'http://172.22.166.33:8008/test_log'

result = {}


def testAliPay():
  Popen('adb shell am force-stop com.eg.android.AlipayGphone')
  time.sleep(1)
  Popen('adb shell am start -n com.eg.android.AlipayGphone/com.eg.android.AlipayGphone.AlipayLogin')
  time.sleep(1)
  result['alipay'] = {}
  for k in qrcodeIndex:
    print k
    d.wait.update()
    d(text=u"扫一扫").click.wait()

    d(text=u"相册").click.wait()

    d(resourceId=u"com.alipay.mobile.beehive:id/iv_photo", instance= qrcodeIndex[k]).click.wait()
    time.sleep(3)
    print 'if i am blocked?'
    try:
      d(resourceId=u"com.alipay.mobile.nebula:id/h5_tv_title").wait.exists(timeout=3)
      view = d(resourceId=u"com.alipay.mobile.nebula:id/h5_tv_title")
      for i in xrange(1,4):
        title_text = view.info['text']
        print 'title text ' + title_text.encode('utf8')
        if view.info['text'] == u'安全提示':
          time.sleep(1)
        else:
          raise Exception('yes i am ok')
      print 'i am blocked ' + k + ' under alipay'
      result['alipay'][k]  = 0
    except Exception, e:
      print 'i am not blocked ' + k + ' under alipay'
      result['alipay'][k]  = 1
      print e

    d.press.back()


def testWechart() :
  Popen('adb shell am force-stop com.tencent.mm')
  time.sleep(1)
  Popen('adb shell am start -n com.tencent.mm/com.tencent.mm.ui.LauncherUI')
  time.sleep(5)
  d.wait.update() 

  result['wechat'] = {}

  for k in qrcodeIndex:
    print k

    for view in d(className="android.widget.RelativeLayout", clickable=True):
      if view.info[u'contentDescription'] == u'更多功能按钮':
        view.click()
        break

    d(text=u"扫一扫").wait.exists(timeout=3000)
    d(text=u"扫一扫").click.wait()


    d(resourceId="com.tencent.mm:id/iw").wait.exists(timeout=3000)
    d(resourceId="com.tencent.mm:id/iw").click.wait()

    d(resourceId="com.tencent.mm:id/jm", instance=1).wait.exists(timeout=3000)
    d(resourceId="com.tencent.mm:id/jm", instance=1).click.wait()

    d(resourceId=u"com.tencent.mm:id/gv", instance=qrcodeIndex[k]).click.wait()

    time.sleep(10)

    print 'if i am be blocked?'
    print 'i am not blocked ' + k + ' under wechat'

    result['wechat'][k]  = 1

    d.press.back()


testAliPay()
testWechart()

http_post(report_url, json.dumps(result))