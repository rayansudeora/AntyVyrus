from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
import requests
import json
import scraper

app = Flask(__name__)



@app.route('/')
def index():
	return render_template("home.html")

@app.route("/covidupdates")
def covid():
	return render_template("myform.html")

@app.route("/covidupdates",methods=["POST"])
def covidform():
	text = request.form["text"].upper()
	#scraper.main(text)
	return render_template("postform.html", text=text, data=scraper.main(text))


@app.route("/selftest")
def selftest():
	return "SELFTEST"


if __name__ == '__main__':
	app.run(debug=True)



