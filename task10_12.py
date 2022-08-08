import json

# from os import remove
# with open('task_4_1.json','r') as file:
#     x=json.load(file)
# actor=x['actor']
# i=0
# l=[]
# while i<len(actor):
#     p=actor[i]
#     del (p['@type'])
#     l.append(p)
#     i+=1
# print(l)



# import json
# with open("task_4.json","r") as file:
#     x=json.load(file)
# p=x['actors'][0]['url']
# print(p[6:-1])


# with open("task_5_1.json",'r') as file:
#     x=json.load(file)
# l=[]
# i=0
# while i<len(x):
#     actor=x[i]['actors']
#     d={}
#     j=0
#     while j <len(actor):
#         name=actor[j]['name']
#         p=actor[j]['url']
#         id=p[6:-1]
#         j+=1
#         d['imdb_id']=id
#         d['name']=name
#     i+=1
#     l.append(d)
# with open('task_10.json','w') as file1:
#     json.dump(l,file1,indent=5)