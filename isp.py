import requests
import json
print("正在自动判断您的运营商")
response = requests.get("https://ip.ping0.cc/geo") #从ping0.cc的api判断运营商
geo_data = response.text
#从此处开始判断运营商并设定URL以方便后续下载配置文件
if "移动" in geo_data:
    url = "URL"
    me = "移动"
elif "电信" in geo_data:
    url = "URL"
    me = "电信"
elif "联通" in geo_data:
    url = "URL"
    me = "联通"
else:
    url = "URL"
    me = "其他"
print("判断完成")
print("您的运营商为：", me)

response = requests.get(url)  # 根据判断的运营商下载配置文件并保存
config_data = response.text
with open('config.json', 'w') as f:
    f.write(config_data)
print("配置文件下载完成！")
