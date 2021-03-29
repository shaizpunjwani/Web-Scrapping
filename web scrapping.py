# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:54:36 2021

@author: lenovo
"""

from bs4 import BeautifulSoup

with open('base.html','r') as html_file:
    txt=html_file.read()
    
    #lxml is used as an parser in beautiful soup and we used prettify to read the contents in the html file.
    soup=BeautifulSoup(txt,'lxml')
    #print(soup.title)
    #print(soup.body)
    #print(soup.div)
    #print(soup.p)
    #print(soup.title.name)
    #print(soup.title.string)
    #print(soup.find_all('h5'))
    #if you are finding anything in file so then only you can get its text using for loops as done below...
    #soup1=(soup.find_all('a'))
    
    #for t in soup1:
     #   print(t.text)
    #if you want to fetch specific class in div tag apply underscore in class because class is an inbuilt as well in python
    tags=soup.find_all('a',class_='dropdown-item')
    
    for tag in tags:
        print(tag.href)
        
        
#--------------------------------------------------
#now working for the websites 
from bs4 import BeautifulSoup
import lxml
#we imported requests to get to the websites
import requests
html_txt=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup=BeautifulSoup(html_txt,'lxml')
jobs=soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
#find method only finds the object that justifies the given condition

#we use strip to remove the spaces and text to just get only the text not the tags
company=soup.find('h3',class_="joblist-comp-name").text.strip()

skills=soup.find('span',class_='srp-skills').text.replace(' ','')  
time=soup.find('span', class_='sim-posted').text.strip()   


print('Company Name:\n \n{}\n \nJob Skills:\n \n{}\n \nTime:\n \n{}'.format(company,skills,time))

#----------------------------------------------------------------------------------------------------------

#we can run a for loop and can find a company time and skills in it

for job in jobs:
    company=soup.find('h3',class_="joblist-comp-name").text.strip()

    skills=soup.find('span',class_='srp-skills').text.replace(' ','')  
    time=soup.find('span', class_='sim-posted').text.strip()   


    print('Company Name:\n \n{}\n \nJob Skills:\n \n{}\n \nTime:\n \n{}'.format(company,skills,time))
    
    
#if we want time as few days in record
    
for job in jobs:
    
    time=soup.find('span', class_='sim-posted').text.strip()   

    if 'few' in time:
    
        company=job.find('h3',class_="joblist-comp-name").text.strip()

        skills=job.find('span',class_='srp-skills').text.replace(' ','')  

        more_info=job.header.h2.a['href']

        print('Company Name:\n \n{}\n \nJob Skills:\n \n{}\n \nTime:\n \n{}\n \nInfo{}'.format(company,skills,time,more_info))
    

#-------------------------------------------------------
#now we work on inputs and then searching

def Job_find():

    unfamiliar=input('enter your unfamiliar skill:')
    print('filtering out',unfamiliar)
    for job in jobs:
    
        time=job.find('span', class_='sim-posted').text.strip()   

        if 'few' in time:
    
            company=job.find('h3',class_="joblist-comp-name").text.strip()
            
            skills=job.find('span',class_='srp-skills').text.replace(' ','')  

            more_info=job.header.h2.a['href']
        
        if unfamiliar not in skills:
            with open ('jobhunt.txt','w') as file:
                file.write("company name: {}".format(company))
                file.write("Skills required: {}".format(skills))
                file.write("More information: {}".format(more_info))
            
    print('done')

Job_find()