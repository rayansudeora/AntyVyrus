from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
import requests
import json
import scraper


app = Flask(__name__)



@app.route('/')
def index():
	return render_template("index.html")

@app.route("/covidupdates")
def form():
	return render_template("myform.html")

@app.route("/covidupdates",methods=["POST"])
def retrieve_data():
	text = request.form["selectcountries"]
	return render_template("postform.html", text=text, data=scraper.main(text))


@app.route("/selftest")
def selftest():
	return render_template("selftest.html")


if __name__ == '__main__':
	app.run(debug=True)
