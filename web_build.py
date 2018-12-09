# RUN THIS FILE IN TERMINAL USING python and file name to open the local host,
# then open the the web address given in your browser
import json, requests, urllib2
from flask import Flask, render_template


app = Flask(__name__)

# Links API and reads count from api
url = 'https://api.case.law/v1/cases/'
law_case = urllib2.urlopen(url)
wjson = law_case.read()
wjdata = json.loads(wjson)
# creates variable count that can be passed further to html as a var
count_var = wjdata['count']



# Returns index.html when goes to the main page or homepage
@app.route("/")
@app.route("/home")
def home():
    #passes count as variable in index.html
    return render_template('index.html', title="Home Page", count = count_var)

@app.route("/about")
def about():
    return render_template('about.html', title="About Page")

@app.route("/api")
def get_account_info():

    api_url = '{0}account'.format(api_url_base)

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

# allows to run it on local host without exporting FLASK_APP environment vars
# and refresh without restarting server
if __name__ == '__main__':
    app.run(debug=True)
