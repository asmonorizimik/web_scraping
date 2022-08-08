
import requests,json,time
from bs4 import BeautifulSoup
def movies_url():
    with open("imdb.json") as file:
        movieList=json.load(file)
    url=[]
    for i in movieList:
        url.append(i['url'])
    return url

def movies():
    with open("imdb.json") as file:
        movieList=json.load(file)
    print("Top rated movies name")
    movies=[]
    for i in movieList:
        movies.append(i['name'])
    return movies
    
def scrape_movie_details():
    movie_name=movies()
    movie_url=movies_url() 
    i=0
    while i<len(movie_name):
        print(i+1,":",movie_name[i])
        i+=1
    SelectMovie=int(input("select the movies"))-1
    if SelectMovie<len(movie_url):
        details={'name':'','director':'','country':'','language':'','poster':'','summary':'','runtime':'','genre':'','actors':''}
        url1=movie_url[SelectMovie]
        print("MOVIE NAME:\n",movie_name[SelectMovie])
        time.sleep(2)
        res=requests.get(url1)
        soup=BeautifulSoup(res.content,"html.parser")##source code
        d=soup.find('script').text
        x=json.loads(d)
        # print(x)
    # with open("task_4_1.json",'w') as f1:
    #     json.dump(x,f1,indent=5)
        movie1=soup.find('h1').text.replace("filmography",'')
        poster1=soup.find('div',class_='ipc-poster').a["href"]
        poster="https://www.imdb.com"+poster1
        CountryAndLanguage= soup.findAll("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
        summary=x['description']
        genre=x['genre']
        runtime=x['duration']
        actors=x['actor']
        Director=x['director']
        actors1=[]
        # for n in actors:
        #     actors1.append(n['name'])
        i=0
        while i<len(actors):
            p=actors[i]
            del (p['@type'])
            actors1.append(p)
            i+=1
        dir=""
        o=0
        while o<len(Director):
            p1=Director[o]
            del (p1['@type'])
            del (p1['url'])
            dir=p1
            o+=1
        for i in CountryAndLanguage:
            x=i.findAll('li',class_="ipc-metadata-list__item")
            for j in x:
                if "Country" in j.text:
                    country=j.find('div',class_="ipc-metadata-list-item__content-container").text
                elif "Language" in j.text:
                    language=j.findAll('a')
                    for l in language: 
                        details["language"]=l.text
                        details["country"]=country
        details['name']=movie1
        details['director']=dir
        details['poster']=poster
        details['summary']=summary
        details['genre']=genre
        details['runtime']=runtime
        details['actors']=actors1
        print(details)
    else:
        print("OOOPSS!!! ...somthing went wrong!!!")
    with open("task_4.json","w") as file:
        json.dump(details,file,indent=5)
scrape_movie_details()