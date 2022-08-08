import requests,json,time
from bs4 import BeautifulSoup
def movies_url():
    with open("imdb.json") as file:
        movieList=json.load(file)
    url=[]
    for i in movieList:
        url.append(i['url'])
    return url
def scrape_movie_details(movie_url):
    k=0
    movie_details=[]
    while k<len(movie_url):
        details={'name':'','link':'','director':'','country':'','language':'','poster':'','summary':'','runtime':'','genre':'','actors':''}
        url1=movie_url[k]
        time.sleep(2)
        res=requests.get(url1)
        soup=BeautifulSoup(res.content,"html.parser")##source code
        d=soup.find('script').text
        x=json.loads(d)
        movie1=soup.find('h1').text.replace("filmography",'')
        poster1=soup.find('div',class_='ipc-poster').a["href"]
        CountryAndLanguage= soup.findAll("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
        details['name']=movie1
        details['link']=movie_url[k]
        details['director']=soup.find("li",class_="ipc-metadata-list__item").a.text
        details['poster']="https://www.imdb.com"+poster1
        details['summary']=x['description']
        details['genre']=x['genre']
        details['runtime']=x['duration']
        actors=x['actor']
        actors1=[]
        i=0
        while i<len(actors):
            p=actors[i]
            del (p['@type'])
            actors1.append(p)
            i+=1        
        # for n in actors:
        #     actors1.append(n['name'])
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
        details['actors']=actors1
        movie_details.append(details)
        k+=1
        with open("task_.json","w") as file:
            json.dump(movie_details,file,indent=5)
movie_url=movies_url() 
scrape_movie_details(movie_url)