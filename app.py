from flask import Flask, render_template, url_for, redirect, request
from db import CreateAcc, CreateTable, CheckCredentials

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register-page")
def register_page():
      return render_template("registerpage.html")

@app.route("/home-page")
def home_page():
      return render_template("homepage.html")

@app.route("/register-account", methods=['POST'])
def register_account():
      username = request.form['userName']
      password = request.form['passWord']
      CreateAcc(username=username, password=password)
      return redirect(url_for('home'))

@app.route("/verify-credentials", methods=['POST'])
def check_credentials():
      username = request.form['reg-username']
      password = request.form['reg-password']
      is_registered = CheckCredentials(username, password)
      if is_registered == True:
            return redirect(url_for('home_page'))
      elif is_registered == False:
            return redirect(url_for('home'))
      

if __name__ == "__main__":
      try:
            CreateTable()
      except:
            print("Database error during table creation")
      app.run(debug=True)


