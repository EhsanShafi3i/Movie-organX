import os
from defines import *
import shutil
while True:
    print("Welcome")
    print("Choose")
    print("1-Currant directory")
    print("2-Change directory")
    print("3-Exit")
    choice = input("\n--> ")
    if choice == "1":
        movies = get_all_movies()
        for movie in movies:
            if search_for_year_in_name(movie):
                year = search_for_year_in_name(movie)
                if f"{year}" in os.listdir():
                    shutil.move(movie, f"{year}")
                else:
                    os.mkdir(f"{year}")
                    shutil.move(movie, f"{year}")
            else:
                year = search_for_year_in_imdb(movie)
                if f"{year}" in os.listdir():
                    shutil.move(movie, f"{year}")
                else:
                    os.mkdir(f"{year}")
                    shutil.move(movie, f"{year}")
    elif choice == "2":
        path = input("enter the path : ")
        go_to_dirct(path)
        movies = get_all_movies()
        for movie in movies:
            if search_for_year_in_name(movie):
                year = search_for_year_in_name(movie)
                if f"{year}" in os.listdir():
                    shutil.move(movie, f"{year}")
                else:
                    os.mkdir(f"{year}")
                    shutil.move(movie, f"{year}")
            else:
                year = search_for_year_in_imdb(movie)
                if f"{year}" in os.listdir():
                    shutil.move(movie, f"{year}")
                else:
                    os.mkdir(f"{year}")
                    shutil.move(movie, f"{year}")
    elif choice == 3:
        break
    else:
        input("not valid")
