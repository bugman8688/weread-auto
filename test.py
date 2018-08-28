# coding:utf-8
import os
import subprocess
import sys

if __name__ == '__main__':
    title = os.path.basename(sys.argv[0])
    content = "这个是内容"

    # 执行AppleScripts命令， osascript -e 'display notification "内容" with title "标题"'
    cmd = 'display dialog "这是两位爸爸送给儿子的生日礼物" buttons {"OK", "取消"} default button 1 with title "test"'
    res = subprocess.call(["osascript", "-e", cmd])
    print(res)
    pass
