import urllib.request
import os
import ctypes
import time
import subprocess

#关于令牌验证
token = input("请输入验证令牌: ")


token_url = 'URL'
with urllib.request.urlopen(token_url) as f:
    expected_token = f.read().decode().strip()


if token != expected_token:
    ctypes.windll.user32.MessageBoxW(0, "验证失败，请加入QQ群303915645获取令牌", "验证失败", 0)
    exit()

#下载配置文件
url = 'URL'
urllib.request.urlretrieve(url, 'name.json')

os.system('isp.exe')

subprocess.Popen(['keep.exe'])

#写入hosts
with open(r'C:\Windows\System32\drivers\etc\hosts', 'r+', encoding='utf-8') as f:
    content = f.read()
    if '127.0.0.1 mc.hypixel.net' not in content:
        f.write('\n127.0.0.1 mc.hypixel.net')
        print("hosts写入成功")
    f.close()
time.sleep(3)


title = '加速完成！'
message = '请点击确定按钮，然后使用mc.hypixel.net进入hypixel服务器'
ctypes.windll.user32.MessageBoxW(0, message, title, 0)


os.system('加速组件')
