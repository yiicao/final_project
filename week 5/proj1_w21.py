#########################################
##### Name:    Yi Cao               #####
##### Uniqname:    yiicao           #####
#########################################

import json
import requests
import webbrowser


class Media:

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL"):
        self.title = title
        self.author = author
        self.release_year = release_year
        self.url = url
        self.json = None
    
    def info(self):
        return self.title + " by " + self.author + " (" + self.release_year + ")"
    
    def length():
        return 0
    
    def get_json(self, dict):
        self.json = dict

    def create_object_by_json(self):
        
        if "trackName" in self.json.keys():
            self.title = self.json["trackName"]
        else:
            self.title = self.json["collectionName"]

        self.author = self.json["artistName"]
        self.release_year = self.json["releaseDate"][:4]
        if "trackViewUrl" in self.json.keys():
            self.url = self.json["trackViewUrl"]
        else:
            self.url = self.json["collectionViewUrl"]


# Other classes, functions, etc. should go here

class Song(Media):

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", album ="No Album", genre="No Genre", track_length=0):
        super().__init__(title, author, release_year, url)
        self.album = album
        self.genre = genre
        self.track_length = track_length
        self.json = None
    
    def info(self):
        return super().info(), " [" + self.genre +"]"
    
    def length(self):
        return round(self.track_length)
    
    def get_json(self, dict):
        return super().get_json(dict)

    def create_object_by_json(self):
        super().create_object_by_json()
        self.album = self.json["collectionName"]
        self.genre = self.json["primaryGenreName"]
        self.track_length = self.json["trackTimeMillis"]

class Movie(Media):

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url="No URL", rating="No Rating", movie_length=0):
        super().__init__(title, author, release_year, url)
        self.rating = rating
        self.movie_length = movie_length
        self.json = None
    
    def info(self):
        return super().info(), " [" + self.rating +"]"
    
    def length(self):
        return round(self.movie_length)
    
    def get_json(self, dict):
        return super().get_json(dict)

    def create_object_by_json(self):
        super().create_object_by_json()
        self.rating = self.json["contentAdvisoryRating"]
        self.genre = self.json["primaryGenreName"]
        self.track_length = self.json["trackTimeMillis"]

def get_api_resource(terms, timeout=10):
    url = "https://itunes.apple.com/search?"
    if terms:
        params = {"term": "{}".format(terms)}
        response = requests.get(url, params, timeout=timeout).json()
        data = response["results"]
    else:
        response = requests.get(url, timeout=timeout).json()
        data = response["results"]
    
    return data





if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    query_input = input("Enter a search term, or 'exit' to quit:")

    while True:
        if query_input != 'exit':
            break
        else:
            print("Thanks for your participation")
            break
        
    
    query_results = get_api_resource(query_input)
    
    Songs = []
    Movies = []
    Other_Media = []

    for item in query_results:
        if item["wrapperType"] == "track" and item["kind"] == "feature-movie":
            Movies.append(item)
        if item["wrapperType"] == "track" and item["kind"] == "song":
            Songs.append(item)
        else:
            Other_Media.append(item)
    
    print("SONGS")
    for item in Songs:
        song = Song("1","2","3","4","5","6",7)
        song.get_json(item)
        song.create_object_by_json()
        print(f"{Songs.index(item) + 1} {song.info()}")
    
    print("MOVIES")
    for item in Movies:
        movie = Movie("1","2","3","4","5",6)
        movie.get_json(item)
        movie.create_object_by_json()
        print(f"{Movies.index(item) + 1} {movie.info()}")
    
    print("OTHER MEDIA")
    for item in Other_Media:
        media = Media("1","2","3","4")
        media.get_json(item)
        media.create_object_by_json()
        print(f"{Other_Media.index(item) + 1} {media.info()}")
    
    launch_input = input("Enter a number for more info, or another search term, or exit")

    if launch_input.isnumeric():
        launch_input = int(launch_input)
    else:
        launch_input = int(input("Error. Please enter a number (e.g., 3)"))

    results_list = Songs + Movies + Other_Media

    if launch_input < len(results_list):
        print("LAUNCHING")
        if "trackViewUrl" in results_list[launch_input-1].keys():
            print(results_list[launch_input-1]["trackViewUrl"])
            webbrowser.open(results_list[launch_input-1]["trackViewUrl"])
            print("in the browser...")
        else:
            print(results_list[launch_input-1]["collectionViewUrl"])
            webbrowser.open(results_list[launch_input-1]["collectionViewUrl"])
            print("in the browser...")
    else:
        launch_input = int(input("Out of range."))