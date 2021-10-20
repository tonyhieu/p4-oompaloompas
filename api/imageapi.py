from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

images = []
image_links = [
    "https://image.shutterstock.com/image-photo/wide-panorama-sunset-sky-clouds-260nw-731576737.jpg",
    "https://i.redd.it/j79d4w01vmn01.jpg",
    "https://www.710beachrentals.com/wp-content/uploads/2017/02/La-Jolla-cove.jpg",
    "https://a0.muscache.com/pictures/f870caa5-509e-4802-aa30-85dc27f358e0.jpg",
    "https://theshoallajolla.com/latest/wp-content/uploads/2019/02/shutterstock_217914379.jpg"
]
image_titles = [
    "Sunset",
    "Beach1",
    "La Jolla Cove",
    "Beach2",
    "Beach3"
]


def _init_images ():
    for i in range(len(image_links)):
        images.append({"id": i+1, "title": image_titles[i], "link": image_links[i], "likes": 0, "dislikes": 0})

@api_bp.route('/images')
def get_images():
    if len(images) == 0:
        _init_images()
    return jsonify(images)

@api_bp.route('/images/<id>')
def get_image(id):
    if len(images) == 0:
        _init_images()
    try:
        return jsonify(images[int(id)-1])
    except:
        return "Invalid ID"