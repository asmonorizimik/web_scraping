import json
def all_movies():
    with open("imdb.json") as file:
        allMovies=json.load(file)
    return allMovies
def group_by_year(movies):
    dic1={}
    i=0
    while i<len(movies):
        year=movies[i]['year']
        j=0
        l1=[]
        while j<len(movies):
            if year==movies[j]['year']:
                l1.append(movies[j])
            j+=1
        i+=1
        dic1[year]=l1
    d1=dict(sorted(dic1.items()))
    print(d1)
    with open('task_2.json','w') as f:
        json.dump(d1,f,indent=5)
movies=all_movies()
group_by_year(movies)



