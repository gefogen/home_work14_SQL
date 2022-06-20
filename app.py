import sqlite3
from flask import Flask, jsonify
from functions import *

app = Flask(__name__)


@app.route("/movie/<title>/")
def page_movie(title):
    """ Поиск по названию """
    post_movie = search_by_name(title)
    return jsonify(post_movie)


@app.route("/movie/<year>/to/<years>")
def page_movies_by_years(year, years):
    post_movie = search_by_years(year, years)
    return jsonify(post_movie)


@app.route("/rating/children/")
def page_movies_by_children():
    post_movie = search_by_rating_children()
    return jsonify(post_movie)


@app.route("/rating/family/")
def page_movies_by_family():
    post_movie = search_by_rating_family()
    return jsonify(post_movie)


@app.route("/rating/adult/")
def page_movies_by_adult():
    post_movie = search_by_rating_adult()
    return jsonify(post_movie)


@app.route("/genre/<genre>")
def page_movies_by_genre(genre):
    post_movie = search_by_genre(genre)
    return jsonify(post_movie)


if __name__ == "__main__":
    app.run(debug=True)
