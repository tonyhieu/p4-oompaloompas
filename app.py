from flask import Flask, render_template

app = Flask("app")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/changelog")
def changelog():
    return render_template("changelog.html")


@app.route("/anthony")
def anthony():
    return render_template("individual/anthony.html")


@app.route("/ellen")
def ellen():
    return render_template("individual/ellen.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
