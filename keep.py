import time
import psutil
import os

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

while True:
    # 检测main.exe进程是否存在
    main_exist = False
    for p in psutil.process_iter(['name']):
        if p.name() == 'main.exe':
            main_exist = True
            break
    
    #后台结束组件，清除hosts
    if not main_exist:
        for p in psutil.process_iter(['name']):
            if p.name() == 'name' or p.name() == 'name':
                p.kill()
        with open(hosts_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        with open(hosts_path, 'w', encoding='utf-8') as f:
            for line in lines:
                if line.strip() != '127.0.0.1 mc.hypixel.net':
                    f.write(line)
        os._exit(0)
    
    time.sleep(3)
