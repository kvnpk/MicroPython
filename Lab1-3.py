a = {2023, 15000, "Kevin"}   #SET
b = [2023, 15000, "Kevin"]   #List
c = (2023, 15000, "Kevin")   #Tuple
d = {1:2023, 'salary':15000, "name":"Kevin"} #Dictionary

b[1] = 25000
d['salary']= 35000

print(a)
print(b)
print(c)
print(d)
print(d[1])
print(d["name"])
print(type(a))