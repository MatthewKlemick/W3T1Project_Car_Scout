#this code inports the libraries neaded for the software
from flask import Flask, render_template
import Web_scraper
import csv
main = Flask(__name__)

#cd \W3T1Project_Car_Scout\E\Scripts
#activate
#set FLASK_APP=main.py
#flask run 


@main.route('/')
def index():
    LN , LA , Ln , LU = Web_scraper.scape("health-fitness")
    length = len(LN)
    return render_template('Scrapeddata.html', name = LN , address = LA, number = Ln , URL = LU , Length = length )



LN , LA , Ln , LU = Web_scraper.scape("health-fitness")
length = len(LN)
with open('leads.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
    filewriter.writerow(["lead #", "lead name", "lead address", "lead number", "lead url"])
    for x in range(length):
        filewriter.writerow((x, LN[x], LA[x], Ln[x], LU[x]))