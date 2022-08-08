##DIRECTORS
import json
with open("task_5.json",'r') as file:
    details=json.load(file)

# def director_language():
#     d={}
#     directorlist=[]
#     langList=[]
#     for i in details:
#         director=i['director']
#         directorlist.append(director)
#         lang=i['language']
#         langList.append(lang)
#         d1={}
#         k=0
#         while k<len(directorlist):
#             lang1=i['language']
#             if director==directorlist[k] and lang==langList[k]:
#                 if langList[k] in d1:
#                     d1[lang1]+=1
#                 else:
#                     d1[lang1]=1
#                 d[director]=d1
#             k+=1

        
#     print(d)
#     # with open("task_8.json",'w') as file1:
#     #     json.dump(d,file1,indent=5)
# director_language()




def director_language():
    d={}
    for movies in details:
        for director in movies['director']:
            d[director]={}
    for i in range(len(details)):
        for director in d:
            if director in details[i]['director']:
                for language in details[i]['language']:
                    d[director][language]=0
    for i in range(len(details)):
        for director in d:
            if director in details[i]['director']:
                for language in details[i]['language']:
                    d[director][language]+=1
    print(d)
    # with open("task_8.json",'w') as file1:
    #     json.dump(d,file1,indent=5)
director_language()
