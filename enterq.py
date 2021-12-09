import json
# f=open('enter.json')
# data=json.load(f)
# print(data)
# print(type(data))

lst=[1,2,3,4,5,6,7,8,9]
with open("lst.json","w")as file:
    i=0
    while i<len(lst):
        json.dump(lst[i],file,indent=4)
        i=i+1
