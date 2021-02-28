#this code inports the libraries neaded for the software
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
# import Web_scraper
main = Flask(__name__)
pages = 1
leaddetals = []
leadname = []
leadnumber = []
leadaddress = []
# this code scrapes the web page
def scape(cat):
    max
    pagenumber = 0
    
    pagehtml = requests.get("https://www.nzdirectory.co.nz/" + cat + ".html")
    html = BeautifulSoup(pagehtml.text, 'html.parser')
    pages = len(html.find_all('div', class_="pages"))
    
    for page in range(pages):
                
        if page == 1:
            pagehtml = requests.get("https://www.nzdirectory.co.nz/" + cat + ".html")
            html = BeautifulSoup(pagehtml.text, 'html.parser')
            lead_items = html.find_all('div', class_="listing_content")
            detals = ""
          
        else:
            pagehtml = requests.get("https://www.nzdirectory.co.nz/" + cat + "-"+ str(page) + ".html")
            html = BeautifulSoup(pagehtml.text, 'html.parser')
            lead_items = html.find_all('div', class_="listing_content")
            detals = ""
    
        for lead in lead_items:

            if lead.find('p',class_="address") in lead:
                detals=(lead.find('p',class_="address")).text  
                leaddetals.append(detals)
                leadname.append(detals[0:detals.find(",")+1])
                detals = detals[:0] +  detals[detals.find(",")+1:]
                if detals.find("+") != -1 :
                    leadaddress.append(detals[0:detals.find("+")-1])
                    detals = detals[:0] +  detals[detals.find("+"):]
                    leadnumber.append(detals)
                else:
                    leadaddress.append(detals[0:])
                    leadnumber.append("N/A")
    return leadname,leadaddress,leadnumber

#https://www.nzdirectory.co.nz/health-fitness.html

#cd 
#activate
#set FLASK_APP=main.py
#flask run 

scape("health-fitness")
print(leadname)
print(leadaddress)
print(leadnumber)

@main.route('/')
def index(LN = leadname,LA = leadaddress,Ln = leadnumber):
    LN , LA , Ln = scape("health-fitness")
    length = len(LN)
    return render_template('Scrapeddata.html',name = LN, address = LA, number = Ln, Length = length )