from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "password"
# SQL can be used in the future

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Request method to get user input from the login form
        # Users must fill out the form in 'login.html'
        
        if username == USERNAME and password == PASSWORD: # Data verification
            return redirect(url_for("welcome"))
        else:
            return render_template("login.html",
                                   error="Usuário ou Senha Inválidos")
    return render_template("login.html")

@app.route("/welcome") # Route accessed after successful login
def welcome():
    return render_template("welcome.html")

if __name__ == "__main__":
    app.run(debug=True)