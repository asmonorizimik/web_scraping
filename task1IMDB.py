from bs4 import BeautifulSoup
import requests,json
url= 'https://www.imdb.com/india/top-rated-indian-movies/'
page= requests.get(url)
# The get() method sends a GET request to the specified url.
# The get() method returns the value of the item with the specified key.

soup=BeautifulSoup(page.content,"html.parser")##source code

# text will get you the text from the HTML element for the banner advertisement.
# text attribute will return a string stripped of any HTML tags and metadata.
def scrap_top_list():
    main_div=soup.find('div',class_='lister')##This class will find the given tag with the given attribute. it will find all the div having class as entry-content
    tbody=main_div.find('tbody',class_='lister-list')
    trs=tbody.find_all('tr')

    movie_ranks=[]
    movie_name=[]
    yearOfRelease=[]
    movie_urls=[]
    movie_ratings=[]

    for tr in trs:
        position=tr.find('td',class_="titleColumn").get_text().strip()
        # return position
        rank=''
        for i in position:
            if "." not in i:
                rank+=i
            else:
                break
        movie_ranks.append(rank)

        title=tr.find('td',class_="titleColumn").a.get_text()
        movie_name.append(title)

        year=tr.find('td',class_="titleColumn").span.get_text()
        yearOfRelease.append(year)

        imdbRating=tr.find('td',class_="ratingColumn imdbRating").strong.get_text()
        movie_ratings.append(imdbRating)

        link=tr.find('td',class_="titleColumn").a['href']
        movie_link="https://www.imdb.com"+link
        movie_urls.append(movie_link)
    topMovies=[]
    details={'name':'','year':'','position':'','rating':'','url':''}
    for i in range(0,len(movie_ranks)):
        details['name']=str(movie_name[i])
        yearOfRelease[i]=yearOfRelease[i][1:5]
        details['year']=int(yearOfRelease[i])
        details['position']=int(movie_ranks[i])
        details['rating']=float(movie_ratings[i])
        details['url']=movie_urls[i]
        topMovies.append(details.copy())
    with open("imdb.json","w") as f:
        json.dump(topMovies,f,indent=6)
    return topMovies
# print(scrap_top_list())
topMovies=scrap_top_list()
b=0
while b<len(topMovies):
    d1=topMovies[b]
        # print(d1)
    for k in d1:
        print(k,d1[k])
    b+=1

