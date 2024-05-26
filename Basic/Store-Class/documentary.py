##### MohammadAli Mirzaei #####
from media import Media  # Import the Media class from the media module

class Documentary(Media):  # Define a class named Documentary, which inherits from the Media class
    def __init__(self, type, name, director, imdb_score, url, duration, casts):  # Define a constructor method that takes the instance (self) and several parameters
        super().__init__(type, name, director, imdb_score, url, duration, casts)  # Call the constructor of the parent class (Media) using super(), passing all required parameters
