from flask import Flask, jsonify, request
from csv import reader

all_movies = []


# read csv file as a list of lists
with open('movies.csv',  encoding="utf8") as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    data = list(csv_reader)
    print(data[1])
    all_movies = data[1:]


liked_movies = []
not_liked_movies = []
did_not_watch = []

app = Flask(__name__)


@app.route("/get-movie")
def get_movie():
   return jsonify({
       "data": all_movies[0],
       "status": "success"
   })

@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-movie", methods=["POST"])
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-watch", methods=["POST"])
def did_not_watch():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()