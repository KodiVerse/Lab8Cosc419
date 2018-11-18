from flask import Flask, render_template, request, Markup, session, redirect
from random import randint

MyApp = Flask(__name__)
MyApp.secret_key = 'HelloSecretKey'

@MyApp.route("/")
def template():
        return render_template("main.html")

@MyApp.route("/about")
def aboutPage():
        return render_template("about.html")

@MyApp.route("/contact")
def contactPage():
        return render_template("contact.html")

@MyApp.route("/logout", methods=["GET"])
def logout():
        session.pop('testMeBaby', None)
        return redirect("/")

@MyApp.route("/profile")
def profile():
        return render_template("profile.html")

@MyApp.errorhandler(418)
def error():
    return render_template('418_error.html'), 418

@MyApp.route("/secret")
def secret():
    if "testMeBaby" in session:
        return render_template("secretPage.html")
    else:
        return abort(418)

@MyApp.route("/login",  methods=["GET", "POST"])
def profilePage():
        if request.method == "POST":
                realUserName = 'testMeBaby'
                realPassword = 'letmein'
                userName = request.form["userName"]
                password = request.form["password"]
                if userName in session:
                        return render_template("homePage.html")
                elif realUserName == userName and realPassword == password:
                        session[userName] = password
                        var = "Thanks for logging in"
                        return render_template("homePage.html", desc=var)
                else:
                        var = "Did not login"
                        return render_template("homePage.html", desc=var)
        else:
                return render_template("login.html")



if __name__ == "__main__":
        MyApp.run()
