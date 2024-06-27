import os
import uuid

import pandas as pd
from flask import (
    Flask,
    Response,
    render_template,
    request,
    send_from_directory,
    jsonify,
)

app = Flask(__name__, template_folder="templates")


# User name & Password
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("another_index.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "yusuf" and password == "1234":
            return "Success"
        else:
            return "Failure"


# Accept file with formats
@app.route("/file_upload", methods=["POST"])
def file_upload():
    file = request.files["file"]

    if file.content_type == "text/plain":
        return file.read().decode()

    elif (
        file.content_type
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ):
        df = pd.read_excel("test.xlsx")
        return df.to_html()


@app.route("/convert_csv", methods=["POST"])
def convert_csv():
    file = request.files["file"]

    if (
        file.content_type
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ):
        df = pd.read_excel("test.xlsx")
        res = Response(
            df.to_csv(),
            mimetype="text/csv",
            headers={"Content/Disposition": "attachment; filename=download.csv"},
        )
        return res


@app.route("/convert_csv2", methods=["POST"])
def convert_csv2():
    file = request.files["file"]

    if (
        file.content_type
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ):
        df = pd.read_excel("test.xlsx")

        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        name_file = f"{uuid.uuid4()}.csv"
        df.to_csv(os.path.join("downloads", name_file))

        return render_template("download.html", filename=name_file)


@app.route("/downloads/<filename>")
def download(filename):
    return send_from_directory("downloads", filename, download_name="result.csv")


@app.route("/handle_post_req", methods=["POST"])
def handle_post_req():
    greet = request.json["greeting"]
    name = request.json["name"]

    with open("file.txt", "w") as f:
        f.write(f"{greet}: {name}")

    return jsonify({"Message": "Success"})


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)
