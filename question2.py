import json
# d={"name": "David", "class": "I", "age": 6}
# q=json.dumps(d)
# print(type(d))
# print(type(q))
# print(q)
# #it is used to dumps ofconvert python to json

import json
dict={'1':"pinki",'2':"muskan",'3':"somi"}
with open("ques2.json",'w') as file:
    json.dump(dict,file,indent=4)