# coding:utf-8
from uiautomator import device as d
import time
import datetime


# 点亮屏幕
def light_screen():
    d.screen.on()


# 滑动页面
def auto_swipe():
    d.swipe(1000, 500, 200, 500)
    time.sleep(30)


# 执行5小时
if __name__ == '__main__':
    # 获取当前时间
    startTime = datetime.datetime.now()
    while 1:
        nowTime = datetime.datetime.now()
        mkt_last = time.mktime(startTime.timetuple())
        mkt_now = time.mktime(nowTime.timetuple())
        delt_time = (mkt_now - mkt_last) / 60  # 转成分钟
        # 5小时 ＝＝＝ 300分钟
        leftTime = 300 - delt_time
        if leftTime > 0:
            if leftTime % 30 == 0 and leftTime != 300:
                print("可以领一个书币了")
            print("剩余" + str(int(leftTime)) + '分钟')
            auto_swipe()
        else:
            print("自动读书完毕")
            break
