dictionary = {"c1":"v1", "c2":"v2", "c3":"v3"}
print(type(dictionary))
print(dictionary)

result = dictionary["c1"]
print(result)

customer = {"name":"Juan","last_name":"Fuentes","weight":88,"height":1.76}
query = customer["last_name"]
print(query)

dic = {"c1":55,"c2":[10,20,30],"c3":{"s1":100,"s2":200}}
print(dic["c2"])
print(dic["c2"][1])
print(dic["c3"])
print(dic["c3"]["s2"])

dic = {"c1":["a","b","c"],"c2":["d","e","f"]}
print(dic["c2"][1].upper())

dic = {1:"a",2:"b"}
print(dic)

dic[3] = "c"
print(dic)

dic[2] = "B"
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())