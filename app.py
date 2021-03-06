from flask import Flask, render_template, request
import wikipedia, requests
from algorithms.image import image_data
from PIL import Image, ImageDraw, ImageFont
from ctypes import *
from api.imageapi import api_bp


app = Flask(__name__)


@app.route("/")
def index():
    url = "http://oompaloompas.nighthawkcodingsociety.com/api/images"
    print(url)
    response = requests.request("GET", url)
    return render_template("index.html", images=response.json())


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/rgb', methods=["GET", "POST"])
def rgb():
    return render_template('minilab/rgb.html', images=image_data())


@app.route("/variables")
def variables():
    if request.form:
        try:
            list1 = request.form.get("list1")
            if len(list1) != 0:  # input field has content
                return render_template("minilab/tpt/varAndLists.html", list1 = list1)
            # starting and empty input default
        except:
            return render_template("minilab/tpt/varAndLists.html", list1 = [])
    return render_template("minilab/tpt/varAndLists.html", list1 = [])


@app.route("/bases")
def bases():
    return render_template("minilab/numberBases.html")


@app.route("/binary-addition")
def binary_addition():
    return render_template("minilab/binary-addition.html")


@app.route("/signed-binary-addition.html")
def signed_binary_addition():
    return render_template("minilab/signed-binary-addition.html")


@app.route("/binary", methods=['GET','POST'])
def binary():
    if request.form:
        try:
            bits = request.form.get("bits")

            if request.form["picture_change"] == "Light Bulbs": # checks which button is pressed; if light bulbs button is pressed, light bulbs are the picture and vice versa
                if len(bits) != 0:
                  return render_template("minilab/binary.html", bits=int(bits), image_path_on="/static/assets/bulb_on.gif", image_path_off="/static/assets/bulb_off.png")
            if request.form["picture_change"] == "Mortensen Bulbs":
                if len(bits) != 0:  # input field has content
                  return render_template("minilab/binary.html", bits=int(bits), image_path_on="/static/assets/images/linkedinMort.PNG", image_path_off="/static/assets/images/upsetMort.PNG")

            # starting and empty input default
        except:
            return render_template("minilab/binary.html", bits=8, image_path_on="/static/assets/bulb_on.gif", image_path_off="/static/assets/bulb_off.png")
    return render_template("minilab/binary.html", bits=8, image_path_on="/static/assets/bulb_on.gif", image_path_off="/static/assets/bulb_off.png")

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
        return render_template("individual/anthony/anthony.html", summary=searchsummary)
    return render_template("individual/anthony/anthony.html")


@app.route("/anthony/binary")
def anthonyBinary():
    return render_template("individual/anthony/binary.html")


@app.route("/anthony/shapes")
def anthonyShapes():
    return render_template("individual/anthony/shapes.html")


@app.route("/anthony/binary-logic")
def anthonyBinaryLogic():
    return render_template("individual/anthony/binary-logic.html")


@app.route("/nested-and-iteration", methods=['GET', 'POST'])
def nested_and_iteration():
    so_file = "algorithms/tptOctEleven.so"
    functions = CDLL(so_file)
    if request.form.get("size"):
        size = request.form.get("size")
        if len(size) != 0:  # input field has content
            size = int(size)
            return render_template("minilab/tpt/nested-and-iteration.html", arr=create_array(size), ts=functions.findTs(size))
    return render_template("minilab/tpt/nested-and-iteration.html", arr=create_array(20), ts=functions.findTs(20))


def create_array (size):
    arr = []
    for i in range(int(size)):
        arr.append(i)
    return arr


@app.route("/ellen", methods=['GET', 'POST'])
def ellen():
    if request.form.get("name"):
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("individual/ellen.html", name=name)
    if request.form.get("note"):
        note = request.form.get("note")
        if len(note) != 0:  # input field has content
            return render_template("individual/ellen.html", note=note)
    # starting and empty input default
    return render_template("individual/ellen.html", name="World", note="Text")


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
            return render_template("individual/Linda/linda.html", name=name)
    # starting and empty input default
    return render_template("individual/Linda/linda.html", name="World")


@app.route("/quoteGen")
def quoteGen():
    return render_template("individual/Linda/quoteGen.html")


@app.route("/message")
def message():
    return render_template("individual/Linda/message.html")


@app.route('/picture')
def picture():
    return render_template("individual/Linda/picGen.html")


@app.route('/challenge')
def challenge():
    return render_template("individual/Linda/challenges.html")

@app.route('/onclick')
def onclick():
    return render_template("individual/Linda/onclick.html")

@app.route('/lindalogic')
def lindalogic():
    return render_template("individual/Linda/logic.html")


@app.route("/lindaBinary", methods=['GET','POST'])
def lindaBinary():
    if request.form:
        try:
            bits = request.form.get("bits")

            if request.form["picture_change"] == "Light Bulbs": # checks which button is pressed; if light bulbs button is pressed, light bulbs are the picture and vice versa
                return render_template("individual/Linda/lindaBinary.html", bits=int(bits), image_path_on="/static/assets/bulb_on.gif", image_path_off="/static/assets/bulb_off.png")
            if request.form["picture_change"] == "Switch":
                return render_template("individual/Linda/lindaBinary.html", bits=int(bits), image_path_on="/static/assets/pictures/on.png", image_path_off="/static/assets/pictures/off.png")

            # starting and empty input default
        except:
            return render_template("individual/Linda/lindaBinary.html", bits=8, image_path_on="/static/assets/pictures/on.png", image_path_off="/static/assets/pictures/off.png")
    return render_template("individual/Linda/lindaBinary.html", bits=8, image_path_on="/static/assets/bulb_on.gif", image_path_off="/static/assets/bulb_off.png")


@app.route('/sanvi', methods=['GET', 'POST'])
def sanvi():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("individual/sanvi/sanvi.html", name=name)
    # starting and empty input default
    return render_template("individual/sanvi/sanvi.html", name="World")


@app.route("/image/<id>")
def image(id):
    url = "http://oompaloompas.nighthawkcodingsociety.com/api/images/" + id
    response = requests.request("GET", url)
    try:
        image_data = response.json()
        print(image_data)
        return render_template("image.html", image=image_data)
    except:
        return "Invalid ID"

app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

