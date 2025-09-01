# Створіть клас Song з атрибутами
#  name – назва пісні
#  author – ім’я автора
# Практичне завдання
# методи:
#  __eq__(self, other) – перевіряє чи дві пісні однакові
#  __str__(self, other) – повертає рядок з назвою та автором
# Створіть клас Playlist з атрибутами
#  songs – список пісень(об’єкти класу Song)
# методи:
#  __len__(self) – повертає кількість пісень
#  __contains__(self, item) – перевіряє чи є пісня в плейлисті
#  __iter__(self) – повертає літератор для циклу for
#  add_song(self, song) – додає пісню в плейлист
#  remove_song(self, song) – видаляє пісню з плейлиста
# Створіть порожній плейлист
# Створіть 3 пісні:
# "Imagine", "John Lennon"
# "Bohemian Rhapsody", "Queen"
# "Shape of You", "Ed Sheeran"
# Добавте їх в плейлист
# Пройдіться циклом for по плейлисту та виведіть кожну
# пісню на екран

class Song:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __eq__(self, other):
        return self.name == other.name and self.author == other.author

    def __str__(self):
        return f'{self.name} {self.author}'


class Playlist:
    def __init__(self):
        self.songs = []

    def __len__(self):
        return len(self.songs)

    def __contains__(self, item):
        return item in self.songs

    def __iter__(self):
        return iter(self.songs)

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)


playlist = Playlist()

song1 = Song("Imagine", "John Lennon")
song2 = Song("Bohemian Rhapsody", "Queen")
song3 = Song("Shape of You", "Ed Sheeran")

playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)


for song in playlist:
    print(song)

if song1 in playlist:
    print("song1 є в плейлісті")

target_song = Song("Imagine", "John Lennon")

for song in playlist:
    if song == target_song:
        print("ми знайшли те що треба, таргет_сонг є в плейлісті")