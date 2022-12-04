#dictionary
#key value
#ordered
#duplicate are not allowed
#changeable / mutable
d={"name":"Saiful","class":"KOC28","age":18,"roll no.":"A11"}
#print(d)
#print(len(d))
a=d.get("name")
#OR
b=d["name"]
#print(a,b)
#print(d.keys())
#print(d.values())
#print(d.items())
#d["name"]="saif"
#print(d)
#d.update({"age":22})
#print(d)#
#print(d.pop("age"))
print(d)
#for i in d:
#    print(i,d[i])
mydi={
    "class":{
        "students":{
            "name":"abc","marks":{
                "python":90,"web":95
            }
        }
    }
}
print(mydi["class"]["students"]["marks"]["web"])
#for i in d:
#   print(d[i])