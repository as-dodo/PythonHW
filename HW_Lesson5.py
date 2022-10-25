from datetime import datetime

class Song:
    def __init__(self, name, genre, artist, release_year):
        self.name = name
        self.__genre = genre
        self.artist = artist
        self.release_year = release_year
        print('Song is created')

    def get_genre(self):
        print(f'Music genre is {self.__genre}')
        return self.__genre

    def set_genre(self, new_genre):
        self.__genre = new_genre

    def __str__(self):
        return f'The song named {self.name}, genre - {self.__genre}, is sung by {self.artist}, year of release is {self.release_year}.'



song60 = Song('Gimme Shelter', 'Rock', 'The Rolling Stones', 1969)
print(song60)
song60.get_genre()
song60.set_genre("Rock'n'roll")
song60.get_genre()

class HitSong(Song):

    def __init__(self, name, genre, artist, release_year, album):
        super().__init__(name, genre, artist, release_year)
        self.album = album
        print('Song is created')

    def count_years(self):
        current_year = datetime.now().year
        years = current_year - self.release_year
        return f"The hit song named {self.name} is {years} years old."


hitsong1 = HitSong('Satisfaction', 'rock', 'The Rolling Stones', 1965, 'Out of Our Heads')
print(hitsong1)
print(hitsong1.count_years())

