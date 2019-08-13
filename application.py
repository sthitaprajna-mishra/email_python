from flask import Flask, render_template, request, redirect
import smtplib
import os

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods = ["POST"])
def register():
	sender = request.form.get("sender")
	password = request.form.get("password")
	receiver = request.form.get("receiver")
	messagein = request.form.get("message")
	if not password or not sender or not messagein or not receiver:
		return render_template("failure.html")
	#message = f"Hi {messagein}! I'm sending this message through Gmail using an indigenous Python web-app built from scratch. Hope this message reaches you. Cheers!"
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(sender, password)
	server.sendmail(sender, receiver, messagein)
	return render_template("success.html")

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)    
