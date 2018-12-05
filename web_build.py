# RUN THIS FILE IN TERMINAL USING python and file name to open the local host,
# then open the the web address given in your browser
import json, requests
from flask import Flask, render_template

# api_url_base = 'https://api.case.law/v1/cases/'

app = Flask(__name__)

{
    "count": 6454632,
    "next": "https://api.case.law/v1/cases/?cursor=cD0xNjczLTEwLTI4",
    "previous": null,
    "results": [
        {
            "id": 1021505,
            "url": "https://api.case.law/v1/cases/1021505/",
            "name": "William Stone against William Boreman",
            "name_abbreviation": "Stone v. Boreman",
            "decision_date": "1658",
            "docket_number": "",
            "first_page": "1",
            "last_page": "5",
            "citations": [
                {
                    "type": "official",
                    "cite": "1 Md. 1"
                }
            ],
            "volume": {
                "url": "https://api.case.law/v1/volumes/32044057896128/",
                "volume_number": "1"
            },
            "reporter": {
                "url": "https://api.case.law/v1/reporters/732/",
                "full_name": "Maryland reports, being a series of the most important law cases argued and determined in the Provincial Court and Court of Appeals of the then province of Maryland, from the year 1700 [i.e. 1658] down to the [end of 1799]"
            },
            "court": {
                "url": "https://api.case.law/v1/courts/md/",
                "id": 8823,
                "slug": "md",
                "name": "Court of Appeals of Maryland",
                "name_abbreviation": "Md."
            },
            "jurisdiction": {
                "url": "https://api.case.law/v1/jurisdictions/md/",
                "id": 50,
                "slug": "md",
                "name": "Md.",
                "name_long": "Maryland",
                "whitelisted": false
            }
        }
}

# Returns index.html when goes to the main page or homepage
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title="Home Page")

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
