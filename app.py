from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Username and Password loaded from '.env'
db_username = os.getenv("db_username")
db_password = os.getenv("db_password")
# In future, you can add the SQL DataBase

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Request method to get user input from the login form
        # Users must fill out the form in 'login.html'
        
        if username == db_username and password == db_password: # Data verification
            return redirect(url_for("welcome", user=username))
        else:
            return render_template("login.html",
                                   error="Usuário ou Senha Inválidos")
    return render_template("login.html")

@app.route("/welcome") # Route accessed after successful login
def welcome():
    user = request.args.get("user")
    return render_template("welcome.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)