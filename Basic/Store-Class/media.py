##### MohammadAli Mirzaei #####

from pytube import YouTube
from actor import *  # Importing from an actor module (assuming it contains necessary classes or functions)

MEDIA = []  # A list to hold instances of Media class

class Media:
    def __init__(self, type, name, director, imdb_score, url, duration, casts):
        """
        Constructor for the Media class.
        
        Parameters:
            type (str): Type of media (e.g., movie, TV show).
            name (str): Name of the media.
            director (str): Director of the media.
            imdb_score (float): IMDb score of the media.
            url (str): URL of the media.
            duration (str): Duration of the media.
            casts (list): List of actors/actresses in the media.
        """
        self.type = type
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.casts = casts

    @staticmethod
    def show_info(media_name):
        """
        Static method to display information about a specific media.
        
        Parameters:
            media_name (str): Name of the media to display information about.
        """
        for obj in MEDIA:
            if media_name in obj.name:
                print(
                    f"type: {obj.type}\nname: {obj.name}\nDirector: {obj.director}\nImdb_score: {obj.imdb_score}\nUrl: {obj.url}\nDuration: {obj.duration}\ncasts: {obj.casts}\n=======================\n"
                )
                break
        else:
            print("Media not found...!")

    @staticmethod
    def download(media_name):
        """
        Static method to download a specific media.
        
        Parameters:
            media_name (str): Name of the media to download.
        """
        for obj in MEDIA:
            if obj.name == media_name:
                link = obj.url
                first_stream = YouTube(link).streams.first()
                first_stream.download(output_path="./", filename=f"{obj.name}.mp4")
