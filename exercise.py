# import requests,json
# from bs4 import BeautifulSoup
# url="https://www.imdb.com/title/tt0066763/"
# page=requests.get(url)##get the response

# # print(page)
# soup=BeautifulSoup(page.content,'html.parser') #source code
# # print(soup)
# soup.find('h1')
# soup.find('h1').get_text()
# print(soup)### get the html page
# x=soup.json()




# import json
# file1 = open("imdb.json")
# movies = json.load(file1)
# def group_by_year():
#     emp_dic={}
#     for i in movies:
#         movie_list=[]
#         year=i["year"]
#         if year not in  emp_dic:
#             for j in movies:
#                 if year==j["year"]:
#                     movie_list.append(j)
#             emp_dic[year]=movie_list
#         print(emp_dic)
#     with open("task2.json","w")as file:
#         json.dump(emp_dic,file,indent=4)
#     # print(file)    

# group_by_year()




# from bs4 import BeautifulSoup   
# import requests
# import json
# def scrape_movie_details():
#     details_dict = {}
#     url="https://www.imdb.com/title/tt0066763/"
#     page= requests.get(url)
#     soup=BeautifulSoup(page.text,"html.parser")
#     d=soup.find('script').text.json()
#     print(d)
#     poster=soup.find("div",class_="ipc-poster").a["href"]
#     details_dict["poster_image_url"]="https://www.imdb.com"+poster
#     details_dict["bio"]=d.find("span",class_="GenresAndPlot__TextContainerBreakpointXL-cum89p-2 gCtawA").text
#     details_dict["Movie_name"]=soup.find("div",class_="TitleBlock__Container-sc-1nlhx7j-0 hglRHk").h1.text
#     data= soup.findAll("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
#     # print(data) 
#     for i in data:
#         f=i.findAll('li',class_="ipc-metadata-list__item")
#         for fi in f:
#             if "Country" in fi.text:
#                 country=fi.find('div',class_="ipc-metadata-list-item__content-container").text
#             elif "Language" in fi.text:
#                 language=fi.findAll('a')
#                 for l in language: 
#                     details_dict["language"]=l.text
#                     details_dict["country"]=country
#                 # print(details_dict)
#     runtine=soup.find("div",class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt")
#     run=runtine.findAll("li",class_="ipc-inline-list__item")
#     # print(runtime)
#     s=0
#     for i in run:
#         if s==2:
#             details_dict["runtime"]=i.text
#         s+=1
#     details_dict["Genres"]=soup.find("div",class_="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL").text
#     details_dict["director"]=soup.find("li",class_="ipc-metadata-list__item").a.text
#     print(details_dict)
    
#     # with open("web_task4.json","w")as file:
#     #     json.dump(details_dict,file,indent=4) 

# scrape_movie_details()





import requests
import json
from bs4 import BeautifulSoup
from task1IMDB import topMovies

def scrape_movie_details(movies):
    s=[] 
    for i in movies:
        s.append(i)
    s1=s[:10]
    list1=[]
    for j in s1:
        # print(j)
        # print(j['movies_name'])
        url=j["url"]
        dict1={}
        req = requests.get(url)
        soup = BeautifulSoup(req.text,"html.parser")
        poster=soup.find("div",class_="ipc-poster").a["href"]        
        poster_link="https://www.imdb.com"+poster

        # dict1["name"]=j["Movie_name"]
        dict1["poster_image_url"]=poster_link

        data1=soup.find_all('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
        for k in data1:
            data2=k.find_all('li')
            # print(para2)
            for i in data2:
                if "Language" in i.text:
                    a=i.find('a').text
                    dict1["langauge"]=a
                    # print(dict1)
                elif 'Country of origin' in i.text:
                    a=i.find('a').text
                    dict1["country"]=a
                    # print(dict1)

        find_data=soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-all Storyline__StorylineMetaDataList-sc-1b58ttw-1 esngIX ipc-metadata-list--base")
        # print(find_data)
        name_data=find_data.find_all("li",class_="ipc-metadata-list__item")
        # print(name_data)        
        lis1=[]
        for j in name_data:
            if "Genres" in j.text:
                k=j.find_all('a')
                for l in k:
                    lis1.append(l.text)
                break
        dict1['Genres']=lis1
        # print(dict1)
        der=soup.find('ul',class_="ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt")
        # print(der)
        der1=der.find_all('li')
        der2=der1[0].find_all('a')
        # print(der1)

        list2=[]
        for k in der2:
            list2=(k.text)
        dict1['director']=list2
        list1.append(dict1)
    # print(list1)

    with open ("web_task5.json","w")as file:
        json.dump(list1,file,indent=4)
scrape_movie_details()