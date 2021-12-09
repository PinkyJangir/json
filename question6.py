import json
num='{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}'
A=json.loads(num)
print(type(A))
print(A)