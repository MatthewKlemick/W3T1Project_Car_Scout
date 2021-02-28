scrape = {
#this code inports the libraries neaded for the software
import requests
from bs4 import BeautifulSoup
# import Web_scraper
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
                leadaddress.append(detals[0:detals.find("+")-1])
                detals = detals[:0] +  detals[detals.find("+"):]
                leadnumber.append(detals)
}
