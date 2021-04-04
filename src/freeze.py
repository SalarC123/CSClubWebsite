from flask_frozen import Freezer
from routes import app

freezer = Freezer(app)

@freezer.register_generator
def error_handlers():
    yield "/404.html"

if __name__ == '__main__':
    freezer.freeze()