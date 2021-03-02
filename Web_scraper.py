#this code inports the libraries neaded for the software
import requests
from bs4 import BeautifulSoup
# import Web_scraper
pages = 1
leaddetals = []
leadname = []
leadnumber = []
leadaddress = []
leadurl = []

# this code scrapes the web page
def scape(cat):
    leadurl = []
    urlitmes = []
    elementcont = []
    pagenumber = 0
    number = 0  
    pagehtml = requests.get("https://www.nzdirectory.co.nz/" + cat + ".html")
    html = BeautifulSoup(pagehtml.text, 'html.parser')
    pages = len(html.find_all('div', class_="pages"))

    for page in range(pages + 1):
                  
        if page == 1:
            pagehtml = requests.get("https://www.nzdirectory.co.nz/" + cat + ".html")
        else:
            pagehtml = requests.get("https://www.nzdirectory.co.nz/" + cat + "-"+ str(page) + ".html")

        htmlp = BeautifulSoup(pagehtml.text, 'html.parser')
        lead_items = htmlp.find_all('div', class_="listing_content")
        urlitmes = htmlp.find_all('ul', class_="options")
        url = ""
        detals = ""
        

        for lead in lead_items:

            if lead.find('p',class_="address") in lead:

                detals=(lead.find('p',class_="address")).text
                
                if detals.find("+") != -1:
                      
                    leaddetals.append(detals)
                    leadname.append(detals[0:detals.find(",")+1])
                    detals = detals[:0] +  detals[detals.find(",")+1:]
                    leadaddress.append(detals[0:detals.find("+")-1])
                    detals = detals[:0] +  detals[detals.find("+"):]
                    leadnumber.append(detals)
                    elementcont.append(1)

                else:
                    elementcont.append(0)
            else:
                elementcont.append(0)
        for lead in urlitmes:
  
            if lead.find('li',class_="review") in lead:

                url = lead.find('li',class_="review")

                if elementcont[number] == 1:

                    url = str(url)
                
                    url = url[url.find("?")+1:]
                    leadurl.append(url[0:url.find("#")])

            number = number + 1

    return leadname,leadaddress,leadnumber,leadurl