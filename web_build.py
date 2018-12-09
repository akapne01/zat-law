# RUN THIS FILE IN TERMINAL USING python and file name to open the local host,
# then open the the web address given in your browser
import json, requests, urllib2, os
from flask import Flask, render_template
from random import randint

app = Flask(__name__)

# api_key = os.environ["API_KEY"]

# Links API and reads count from api
url = 'https://api.case.law/v1/cases/'
# opens case url
law_case = urllib2.urlopen(url)
# reads case url
wjson = law_case.read()
wjdata = json.loads(wjson)

# Funtions returning random number between 0 and 99
def random_number():
    return randint(0, 99)

# assigns random number to the case using random_number() function
random_case_number = random_number()
# gets assigns id number of random case to the variable
api_id = wjdata['results'][random_case_number]['id']
# gets and assigns name of the case to variable
api_name = wjdata['results'][random_case_number]['name']
# gets and assigns url of this case to var
api_url = 'https://api.case.law/v1/cases/{}/?full_case=true&format=html'.format(api_id)
# gets and assigns decidion date of this case to var
api_decision_date = wjdata['results'][random_case_number]['decision_date']

# Returns index.html when goes to the main page or homepage
@app.route("/")
@app.route("/home")
def home():
    # passes variables got on this file to be used in index.html
    return render_template('index.html', title="Home Page", id = api_id, url = api_url, name = api_name,
    decision_date= api_decision_date)

@app.route("/about")
def about():
    return render_template('about.html', title="About Page")

@app.route("/random")
def random():
    return render_template('random.html', title="Randomly Generated Case")

# allows to run it on local host without exporting FLASK_APP environment vars
# and refresh without restarting server
if __name__ == '__main__':
    app.run(debug=True)
