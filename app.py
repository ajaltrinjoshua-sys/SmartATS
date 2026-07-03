from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    if file:

        file.save(
            os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )
        )

        return f"""
          Resume uploaded successfully! <br><br>
          File Name: {file.filename}
 """

if __name__ == "__main__":
    app.run(debug=True)