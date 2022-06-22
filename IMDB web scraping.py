#!/usr/bin/env python
# coding: utf-8

# 
# # IMDB web scraping for top movies of 2022

# In[66]:


from bs4 import BeautifulSoup
import requests
import openpyxl


# In[73]:


# creating a excel sheet using openpyxl to store the scraped movies:

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "IMDB TOP MOVIES 2022"
sheet.append(["Rank","Title","Year","Ratings","No_of_Ratings"])

# scrapping imdb website using beautifulsoup:

response = requests.get("https://www.imdb.com/chart/top/?sort=us,desc&mode=simple&page=1")
soup = BeautifulSoup(response.text,"html.parser")
movies = soup.find("tbody",class_ = "lister-list").find_all("tr")

# using a loop to get all the movies in loop iteration:

for movie in movies:
    rank = movie.find("td",class_ = "titleColumn").get_text(strip = True).split(".")[0]
    name = movie.find("td",class_ = "titleColumn").a.text
    year = movie.find("td",class_ = "titleColumn").span.text.replace("("," ")
    year = year.replace(")"," ")
    imdb_ratings = movie.find("td",class_ = "ratingColumn imdbRating").strong.text
    no_of_ratings = movie.find("td",class_ = "ratingColumn imdbRating").strong.get_text
    no_of_ratings = str(no_of_ratings).split(" ")[-3]
    
    #print(rank,name,year,imdb_ratings,no_of_ratings)
    
    sheet.append([rank,name,year,imdb_ratings,no_of_ratings])
    
excel.save("IMDB top movies 2022.xlsx")


# In[ ]:




