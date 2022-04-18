from flask import Flask, redirect, render_template, request, session
from database import create_table, insert_data, login_user

app = Flask(__name__)
app.secret_key = "anytext"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


@app.route("/")
def index():
    if not session.get("email"):
        return render_template("login.html")

    return render_template("home.html", user=session.get("email"))


@app.route("/signup", methods=['POST', 'GET'])
def signup_user():
    if request.method == 'POST':
        email = request.form['signup-email']
        passwd = request.form['signup-password']
        print(email, passwd)
        sign_up(email, passwd)
        return "Sign Up Successfully Go To - <a href='/login'>Login</a>"  # temporary
    else:
        return render_template("signup.html")


@app.route("/login", methods=['POST', 'GET'])
def loginusers():
    if request.method == 'POST':
        email = request.form['login-email']
        passwd = request.form['login-password']
        res = loginUser(email, passwd)
        # if true then go
        if res:
            # store email in session for remember login
            session["email"] = email
            return "Log in Successfully Go To Home Page - <a href='/'>HOME</a>"  # temporary
        else:
            return "Password or Username is Incorrect"
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session["email"] = None
    return redirect("/")


def sign_up(email, passwd):
    # if table not exist then first create table
    create_table("User", ['username', 'password'])
    # Storing email and password
    insert_data("User", ['username', 'password'], [email, passwd])


def loginUser(email, passwd):
    data = login_user("User", email)
    # Checking user password
    if len(data) > 0:
        if passwd == str(data[0][-1]):
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    app.run()
