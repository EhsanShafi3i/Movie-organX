import os
import re
import imdb


def get_all_movies():
    movies = [i for i in os.listdir() if i.endswith("mp4")
              or i.endswith("mkv")]
    return movies


def go_to_dirct(x):
    os.chdir(x)


def search_for_year_in_name(movie):
    match = re.search(r'\b\d{4}\b', movie)
    if match:
        year = int(match.group())
        if year not in [1080, 720, 480, 240, 144]:
            return year
    return False


def search_for_year_in_imdb(movie):
    ia = imdb.IMDb()
    search = ia.search_movie(name_divider(movie))

    if search:
        year = search[0]['year']
        return year
    else:
        return None


def name_divider(name):
    pattern = r'(.+?)\.(\d{4})\.?(\d{3,4}p)?\.(.+)\.(mp4|mkv)$'
    match = re.match(pattern, name)

    if match:
        return match.group(1).encode('utf-8')
    else:
        return b''



