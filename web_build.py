# RUN THIS FILE IN TERMINAL USING python and file name to open the local host,
# then open the the web address given in your browser

from flask import Flask, render_template

# __ name __ special var name in pyth which is name of the module
app = Flask(__name__)

# Returns index.html when goes to the main page or homepage
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

# Returns about.html from templates folder when add /about to the website address
@app.route("/about")
def about():
    return render_template('about.html')

# allows to run it on local host without exporting FLASK_APP environment vars
# and refresh without restarting server
if __name__ == '__main__':
    app.run(debug=True)
