from flask import Flask, render_template, request
# our gallery website


app = Flask("app")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet", methods=['GET', 'POST'])
def greet():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")

@app.route("/changelog")
def changelog():
    return render_template("changelog.html")


@app.route("/anthony")
def anthony():
    return render_template("individual/anthony.html")


@app.route("/ellen", methods=['GET', 'POST'])
def ellen():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("individual/ellen.html", name=name)
    # starting and empty input default
    return render_template("individual/ellen.html", name="World")

@app.route("/alice")
def alice():
    return render_template("individual/alice.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
