import json
with open("task_10.json","r") as file:
    x=json.load(file)
l=[]
l1=[]
i=0
while i<len(x):
    d=x[i]
    l.append(d['name'])
    l1.append(d['imdb_id'])
    i+=1
# print(l)
d1={}
for name in l:
    if name in d1:
        d1[name]+=1
    else:
        d1[name]=1
# print(d1)

d={}
for url in l1:
    if url in d:
        d[url]+=1
    else:
        d[url]=1
id=[]
id2=[]
for key,value in d.items():
    id.append(key)
    id2.append(value)

name1=[]
for n in d1.keys():
    name1.append(n)


d2={}
k=0
while k<len(id):
    d3={}
    for x in d1:
        d3['name']=name1[k]
        d3['number_of_movie']=id2[k]
    d2[id[k]]=d3
    k+=1
with open("task_15.json","w") as file1:
    json.dump(d2,file1,indent=5)