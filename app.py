from flask import Flask, render_template, url_for, redirect, request
from db import CreateAcc, CreateTable

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register-page")
def registerpage():
      return render_template("registerpage.html")

@app.route("/register-account", methods=['POST'])
def registerAccount():
      username = request.form['userName']
      password = request.form['passWord']
      CreateAcc(username=username, password=password)
      return redirect(url_for('home'))
      

if __name__ == "__main__":
      try:
            CreateTable()
      except:
            print("Database error during table creation")
      app.run(debug=True)


