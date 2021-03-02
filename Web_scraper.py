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
    pagenumber = 0
    leadurlN = 0  
    pagehtml = requests.get("https://www.nzdirectory.co.nz/" + cat + ".html")
    html = BeautifulSoup(pagehtml.text, 'html.parser')
    pages = len(html.find_all('div', class_="pages"))
    

    for page in range(pages):
                  
        if page == 1:
            pagehtml = requests.get("https://www.nzdirectory.co.nz/" + cat + ".html")
        else:
            pagehtml = requests.get("https://www.nzdirectory.co.nz/" + cat + "-"+ str(page) + ".html")

        html = BeautifulSoup(pagehtml.text, 'html.parser')
        lead_items = html.find_all('div', class_="listing_content")
        url = ""
        detals = ""
        

        for lead in lead_items:

            if lead.find('p',class_="address") in lead:

                detals=(lead.find('p',class_="address")).text
                url = html.find('li',class_="review")

                if detals.find("+") != -1:
                      
                    leaddetals.append(detals)
                    leadname.append(detals[0:detals.find(",")+1])
                    detals = detals[:0] +  detals[detals.find(",")+1:]
                    leadaddress.append(detals[0:detals.find("+")-1])
                    detals = detals[:0] +  detals[detals.find("+"):]
                    leadnumber.append(detals)
                    leadurl.append("error")
                    # url = url[:0] + url[url.find("?")+1:]
                    # leadurl.append(url[0:url.find("#")])
                    # url = url[url.find("</li>"):]
            else:
                T = False
                # url = url[url.find("</li>"):]

    return leadname,leadaddress,leadnumber,leadurl
#https://www.nzdirectory.co.nz/health-fitness.html
#<li class="review"><a href="profile/listed.php?www.activeagain.co.nz#reviews" title="Write a review about this listing" rel="nofollow">Review</a></li>

print(scape("health-fitness"))