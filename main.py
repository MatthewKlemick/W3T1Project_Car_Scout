#this code inports the libraries neaded for the software
from flask import Flask, render_template
import Web_scraper
main = Flask(__name__)

#cd C:\Users\mattk\Documents\Techtorium\year 2\python\weak3\W3T1Project_Car_Scout\E\Scripts
#activate
#set FLASK_APP=main.py
#flask run 

print(Web_scraper.scape("health-fitness"))

@main.route('/')
def index():
    LN , LA , Ln , LU = Web_scraper.scape("health-fitness")
    length = len(LN)
    return render_template('Scrapeddata.html', name = LN , address = LA, number = Ln , URL = LU , Length = length )