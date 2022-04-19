# app.py
# Basic Flask Application
# Flask Demo - Part 1

from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def index():
	# http://localhost:5000/
	# Return some test
	# return 'Hello World'
	return render_template("index.html")


@app.route('/jsonback')
	# http://localhost:5000/jsonback
	# Return some json
def jsonback():
	return jsonify({"message": "returning some json back"})


@app.route('/hello/<name>')
	# http://localhost:5000/hello/<name>
	# Return Hello and your Name
def hello_name(name):
	return 'Hello ' + name


@app.route('/admin')
	# http://localhost:5000/admin
	# Return Hello Admin
def hello_admin():
   return 'Hello Admin'


if __name__ == "__main__":
	debug = True
	app.run(host='0.0.0.0')

# Virt Env.
# >source /myvirtenvs/flaskenv/bin/activate

# >gunicorn -w 3 -b :5000 -t 30 --reload wsgi:app
# Default port is 5000

# localhost:5000

# To run using gunicorn on Linux
# >gunicorn -b 0.0.0.0:8000 app
# Will run on port 8000

# Build Docker Container
# >docker build --tag flask_gunicorn_app .
# >docker run --detach -p 8000:5000 flask_gunicorn_app
