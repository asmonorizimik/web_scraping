import json
with open("task_2.json") as file:
    year_list=json.load(file)
def group_by_decade(year_list):
    y1=1950
    dic={}
    for i in range(y1,2030,10):
        l=[]
        for j in year_list:
            if y1<int(j) and int(j)<y1+10:
                l.append(year_list[j])
        dic[y1]=l
        y1+=10
    with open('task_3.json',"w") as file1:
        json.dump(dic,file1,indent=5)
    print(dic)
group_by_decade(year_list)

