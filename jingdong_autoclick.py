# -*- coding:utf-8 -*-
import os
import time

# 坐标
zhengzhidaole = '530 1324'
fengqiangyiyi = '975 1292'
lingjinbi = '965 1648'
guanghaodian = '920 770'
jingcaihuichang = '920 983'
jingxuanhaowu = '920 1208'
haowanhudong = '920 1435'
zhibo_shipin = '920 1860'
back = 'adb shell input keyevent KEYCODE_BACK'
a, b, c, d, e = 0, 0, 0, 0, 0
# 连接模拟器
os.system(r'cd D:\Program Files\Microvirt\MEmu')
os.system('adb connect 127.0.0.1:21503')
time.sleep(2)
# 查看京东app是否运行
app_current = os.popen('adb shell dumpsys window windows | findstr "Current"').read()
if 'jingdong' in app_current:
    os.system('adb shell am force-stop com.jingdong.app.mall')
# 开启京东app
os.system('adb shell am start -n com.jingdong.app.mall/com.jingdong.app.mall.MainFrameActivity')
time.sleep(5)
# 点击疯抢一亿图标
os.system('adb shell input tap {}'.format(fengqiangyiyi))
time.sleep(2.5)
# 点击领金币后开始循环
os.system('adb shell input tap {}'.format(lingjinbi))
time.sleep(2.5)
while a < 25:
    a += 1
    os.system('adb shell input tap {}'.format(guanghaodian))
    time.sleep(0.6)
    os.system(back)
    time.sleep(2)
    os.system('adb shell input tap {}'.format(zhengzhidaole))
    time.sleep(2)
while b < 3:
    b += 1
    os.system('adb shell input tap {}'.format(jingcaihuichang))
    time.sleep(0.6)
    os.system(back)
    time.sleep(2)
    os.system('adb shell input tap {}'.format(zhengzhidaole))
    time.sleep(2)
while c < 25:
    c += 1
    os.system('adb shell input tap {}'.format(jingxuanhaowu))
    time.sleep(0.6)
    os.system(back)
    time.sleep(2)
    os.system('adb shell input tap {}'.format(zhengzhidaole))
    time.sleep(2)
while d < 4:
    d += 1
    os.system('adb shell input tap {}'.format(haowanhudong))
    time.sleep(0.6)
    os.system(back)
    time.sleep(2)
    os.system('adb shell input tap {}'.format(zhengzhidaole))
    time.sleep(2)
while e < 4:
    e += 1
    os.system('adb shell input tap {}'.format(zhibo_shipin))
    time.sleep(0.6)
    os.system(back)
    time.sleep(2)
    os.system('adb shell input tap {}'.format(zhengzhidaole))
    time.sleep(2)

os.system(back)
os.system(back)
os.system(back)
