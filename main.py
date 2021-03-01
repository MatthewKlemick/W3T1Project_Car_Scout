#this code inports the libraries neaded for the software
from flask import Flask, render_template
import Web_scraper
main = Flask(__name__)

#cd \W3T1Project_Car_Scout\E\Scripts
#activate
#set FLASK_APP=main.py
#flask run 

print(Web_scraper.scape("health-fitness"))

@main.route('/')
def index():
    LN , LA , Ln = Web_scraper.scape("health-fitness")
    length = len(LN)
    return render_template('Scrapeddata.html',name = LN, address = LA, number = Ln, Length = length )