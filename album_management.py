class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist
    
    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

# Create albums1 list with 5 albums
albums1 = [
    Album("Thriller", 9, "Michael Jackson"),
    Album("Back in Black", 10, "AC/DC"),
    Album("The Bodyguard", 12, "Whitney Houston"),
    Album("Bat Out of Hell", 7, "Meat Loaf"),
    Album("Their Greatest Hits", 17, "Eagles")
]

# Print albums1
print("Albums1:")
for album in albums1:
    print(album)

# Sort by number of songs
albums1.sort(key=lambda x: x.number_of_songs)
print("\nSorted by number of songs:")
for album in albums1:
    print(album)

# Swap elements at position 0 and 1
albums1[0], albums1[1] = albums1[1], albums1[0]
print("\nAfter swapping position 0 and 1:")
for album in albums1:
    print(album)

# Create albums2 and copy from albums1
albums2 = albums1.copy()

# Add two new albums
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did it Again", 16, "Britney Spears"))

print("\nAlbums2:")
for album in albums2:
    print(album)

# Sort alphabetically by album name
albums2.sort(key=lambda x: x.album_name)
print("\nAlbums2 sorted by name:")
for album in albums2:
    print(album)

# Search for Dark Side of the Moon
for i, album in enumerate(albums2):
    if album.album_name == "Dark Side of the Moon":
        print(f"\nDark Side of the Moon found at index: {i}")
        break
