import json
# a='{"Name":"Ram","Class":"IV","Age":9 }'
# parsed=json.loads(a)
# print(parsed)
# print(type(parsed))
# print("\nName: ",parsed["Name"])
# print("Class: ",parsed["Class"])
# print("Age: ",parsed["Age"]) 

with open("ques1.json","r") as file:
    data=file.read()
    print(data)
