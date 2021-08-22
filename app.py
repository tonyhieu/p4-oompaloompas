from flask import Flask, render_template


app = Flask("app")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/anthony")
def anthony():
    return render_template("individual/anthony.html")

app.run(host="0.0.0.0", port=8080)