import json
with open('task_5.json','r') as file:
    details=json.load(file)
def director():
    d={}
    i=0
    while i<len(details):
        directr=details[i]['director']
        if directr in d:
            d[directr]+=1
        else:
            d[directr]=1
        i+=1
    print(d)
    with open("task_7.json",'w') as file1:
        json.dump(d,file1,indent=5)
director()
