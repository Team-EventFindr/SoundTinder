import flask
import requests
import os
import random
import base64

from wikipedia import get_wiki_link
from tmdb import get_movie_data

app = flask.Flask(__name__)


MOVIE_IDS = [157336, 176689, 22321]  # actually IDK what this is


@app.route("/")
def index():
    movie_id = 157336
    [title, tagline, genre, poster_image] = get_movie_data(movie_id)
    wikipedia_url = get_wiki_link(title)
    return flask.render_template(
        "index.html",
        title=title,
        tagline=tagline,
        genre=genre,
        poster_image=poster_image,
        wiki_url=wikipedia_url,
    )


if __name__ == "__main__":
    app.run(  # 8080 for original port #
        host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", 5000)), debug=True
    )
