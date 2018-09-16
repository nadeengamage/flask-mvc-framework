import os
from app import application as app
from flask import render_template

# Web controller for show particular template.
class WebController():

	# Render welcome template with static files.
	@app.route('/')
	def index():
		return render_template("welcome.html")