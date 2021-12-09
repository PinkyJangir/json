import json
file_name="que.txt"
dict1={}
with open (file_name) as file:
    for line in file:
        key,value=line.split(None,1)
        dict1[key]=value.strip()
    print(dict1)