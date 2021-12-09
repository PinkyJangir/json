
import json
emp1=["neelam","programer","24","2400",]
emp2=["komal","trainer","24","20000"]
emp3=["anuradha","HR","25","40000"]
emp4=["Abhishek","manager","29","63000"]
name=["name","work","age","salary"]
dict1={}
dict2={}
dict3={}
dict4={}
dict={}
i=0
while i<len(emp1):
    j=0
    while j<len(emp1):
        dict1[name[i]]=emp1[i]
        dict2[name[i]]=emp2[i]
        dict3[name[i]]=emp3[i]
        dict4[name[i]]=emp4[i]
        dict["emp1"]=dict1
        dict["emp2"]=dict2
        dict["emp3"]=dict3
        dict["emp4"]=dict4
        j+=1
    i+=1
file = open("file8.json", "w")
data=json.dump(dict, file, indent = 6)


