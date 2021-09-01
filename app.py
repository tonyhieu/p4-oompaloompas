from flask import Flask, render_template, request
import wikipedia
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


@app.route("/journal")
def journal():
    return render_template("changelog.html")


@app.route("/anthony", methods=['GET','POST'])
def anthony():
    if request.method=='POST':
        form = request.form
        search = (form['search'])
        try:
            searchsummary = wikipedia.summary(search)
        except:
            searchsummary = "Page not found"
        return render_template("individual/anthony.html", summary=searchsummary)
    return render_template("individual/anthony.html")


@app.route("/ellen", methods=['GET', 'POST'])
def ellen():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("individual/ellen.html", name=name)
    # starting and empty input default
    return render_template("individual/ellen.html", name="World")


@app.route("/alice", methods=['GET', 'POST'])
def alice():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("individual/alice.html", name=name)
    # starting and empty input default
    return render_template("individual/alice.html", name="World")

@app.route('/linda', methods=['GET', 'POST'])
def linda():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("individual/linda.html", name=name)
    # starting and empty input default
    return render_template("individual/linda.html", name="World")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
