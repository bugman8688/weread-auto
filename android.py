# coding:utf-8
import os
import random
import subprocess
import sys

from uiautomator import device as d
import time
import datetime


# 点亮屏幕
def light_screen():
    d.screen.on()


title = os.path.basename(sys.argv[0])


# 滑动页面
def auto_swipe():
    d.swipe(1000, 500, 200, 500)
    sleep_time = random.randint(30, 60)
    time.sleep(sleep_time)
    pass


def notify(content="测试"):
    # 执行AppleScripts命令， osascript -e 'display notification "内容" with title "标题"'
    cmd = 'display notification "%s" with title "%s"' % (content, title)
    subprocess.call(["osascript", "-e", cmd])
    pass


def check():
    # title = os.path.basename(sys.argv[0])
    # 执行AppleScripts命令， osascript -e 'display notification "内容" with title "标题"'
    cmd = 'display dialog "请确认读书环境是否就绪" buttons {"就绪", "取消"} default button 1 with title "%s"' % title
    return subprocess.call(["osascript", "-e", cmd])


# 执行5小时
if __name__ == '__main__':
    # 获取当前时间
    fileName = os.path.basename(sys.argv[0])

    if check() != 0:
        exit()

    notify("开始读书")

    startTime = datetime.datetime.now()
    planTime = 300
    leftTime = planTime
    while leftTime > 0:
        nowTime = datetime.datetime.now()
        mkt_last = time.mktime(startTime.timetuple())
        mkt_now = time.mktime(nowTime.timetuple())
        delt_time = (mkt_now - mkt_last) / 60  # 转成分钟
        leftTime = planTime - delt_time

        if leftTime % 30 == 0 and leftTime != planTime:
            notify("一个小时用眼辛苦了")
        print("剩余" + str(int(leftTime)) + '分钟')
        auto_swipe()

    notify("自动读书完毕")
    pass
