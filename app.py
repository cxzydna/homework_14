from flask import Flask

from movies_bp.movies_bp import movies_bp
from rating_bp.rating_bp import rating_bp
from genre_bp.genre_bp import genre_bp

app = Flask(__name__)

app.register_blueprint(movies_bp, url_prefix='/movie')
app.register_blueprint(rating_bp, url_prefix='/rating')
app.register_blueprint(genre_bp, url_prefix='/genre')


@app.route('/')
def index():
    return '<h1>Main page</h1>'


if __name__ == '__main__':
    app.run(debug=True)
