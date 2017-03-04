import csv 
from flask import Flask 
from flask import render_template
app = Flask(__name__)


def get_csv():
	csv_path = "static/la-riots-deaths.csv"
	# The code below tells Python to open the file and read it, instead of the default open and write aka delete
	csv_file = open(csv_path, 'rb')
	# This calls a method that organizes the data
	csv_obj = csv.DictReader(csv_file)
	csv_list = list(csv_obj)
	return csv_list


@app.route('/')
def index():
	template = "index.html"
	object_list = get_csv()
	return render_template(template, object_list=object_list)

# If this script is run from the command line...
if __name__ == "__main__":
	# Firing up the Flask text server
	app.run(debug=True, use_reloader=True)

