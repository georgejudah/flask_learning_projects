#1 setup flask backend
#2 forms- decide whether flask form or plain HTML or frameworks
#3 forms -create form 1, form 2 , form 3
#form1 - text banner, first name - required, last name - required , email - required(validate), application(dropdown or list, more than one application to choose), date picker req, save, cancel
#3 routes for posting data from the forms
#
#setup ssl for these websites

#1 setup flask backend
from flask import Flask, render_template,jsonify
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message":"app is up and running"})

@app.route("/login")
def login():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)