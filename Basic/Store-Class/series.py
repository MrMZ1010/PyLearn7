##### Mohammad Ali Mirzaei #####

from media import Media

class Series(Media):
    def __init__(self, type, name, director, imdb_score, url, duration, casts, part_no):
        """
        Constructor for the Series class, inheriting from the Media class.
        
        Parameters:
            type (str): Type of the series (e.g., TV show).
            name (str): Name of the series.
            director (str): Director of the series.
            imdb_score (float): IMDb score of the series.
            url (str): URL of the series.
            duration (str): Duration of each episode of the series.
            casts (list): List of actors/actresses in the series.
            part_no (int): Part number of the series (e.g., season number).
        """
        super().__init__(type, name, director, imdb_score, url, duration, casts)  # Calling the constructor of the parent class
        self.part_no = part_no  # Assigning the part number of the series
