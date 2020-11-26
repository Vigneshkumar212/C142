from csv import reader

all_movies = []

with open('final.csv', encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)
    data = list(csv_reader)
    all_movies = data[1:]
    print(data[1])

liked_movies = []
not_liked_movies = []
did_not_watch = []



