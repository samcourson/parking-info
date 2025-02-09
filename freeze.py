from flask_frozen import Freezer
from app import app

freezer = Freezer(app)

@freezer.register_generator
def freeze_static():
    yield '/static/IMG_7331.jpg' 

if __name__ == '__main__':
    freezer.freeze()