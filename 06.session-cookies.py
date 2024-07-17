from flask import Flask, render_template, session, make_response, request, flash


app = Flask(__name__, template_folder="templates")
app.secret_key = "This is my secret key"


@app.route("/")
def index():
    return render_template("session_cookie.html", message="index")


@app.route("/set-data")
def set_data():
    session["name"] = "Yusuf"
    session["role"] = "Admin"

    return render_template("session_cookie.html", message="session is set")


@app.route("/get-data")
def get_data():
    if "name" in session.keys() and "role" in session.keys():
        name = session["name"]
        role = session["role"]
        return render_template(
            "session_cookie.html", message=f"Name: {name}, Role: {role}"
        )
    else:
        return render_template("session_cookie.html", message="Session not found")


@app.route("/clear-session")
def clear_data():
    session.clear()
    return render_template("session_cookie.html", message="Session cleared!")


@app.route("/set-cookie")
def set_cookie():
    res = make_response(render_template("session_cookie.html", message="cookie set"))
    res.set_cookie("cookie_name", "cookie-value")
    return res


@app.route("/get-cookie")
def get_cookie():
    cookie_value = request.cookies["cookie_name"]
    return render_template(
        "session_cookie.html", message=f"Cookie Value is: {cookie_value}"
    )


@app.route("/remove-cookie")
def remove_cookie():
    res = make_response(
        render_template("session_cookie.html", message="Cookie Removed")
    )
    res.set_cookie("cookie_name", expires=0)
    return res


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'yusuf' and password == '1234':
            flash('Successful Login')
            return render_template("session_cookie.html", message="")
        else:
            flash('Login Failed')
            return render_template("session_cookie.html", message="")




if __name__ == "__main__":
    app.run(debug=True)
