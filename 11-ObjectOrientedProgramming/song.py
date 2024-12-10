# class definition
class Song:
   def __init__(self, performer, title, album, year):
    self.performer = performer
    self.title = title
    self.album = album
    self.year = year

   def __str__(self):
     return f'{self.title}, {self.album}, perf:{self.performer}, {self.year}'

# object creation
song1 = Song("Ed Sheeran","Hearts Don't Break Around Here","Divide",2017)

## object usage
print(song1)
