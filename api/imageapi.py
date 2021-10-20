from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

images = []

def _init_images ():
    images.append({"id": 1, "title": "Sunset", "url": "https://image.shutterstock.com/image-photo/wide-panorama-sunset-sky-clouds-260nw-731576737.jpg"})
    images.append({"id": 2, "title": "Beach1", "url": "https://i.redd.it/j79d4w01vmn01.jpg"})
    images.append({"id": 3, "title": "La Jolla Cove", "url": "https://www.710beachrentals.com/wp-content/uploads/2017/02/La-Jolla-cove.jpg"})
    images.append({"id": 4, "title": "Beach2", "url": "https://a0.muscache.com/pictures/f870caa5-509e-4802-aa30-85dc27f358e0.jpg"})
    images.append({"id": 5, "title": "Beach3", "url": "https://theshoallajolla.com/latest/wp-content/uploads/2019/02/shutterstock_217914379.jpg"})

@api_bp.route('/images')
def get_images():
    if len(images) == 0:
        _init_images()
    return jsonify(images)