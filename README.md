README.txt

This program demonstrates basic object-oriented programming and list operations in Python using a simple Album class.

Album Class
The Album class stores information about a music album, including:

album_name

number_of_songs

album_artist

The str method returns the album details in the format:
(album_name, album_artist, number_of_songs)

Creating the First Album List (albums1)
The script creates a list named albums1 containing five predefined Album objects.
The program prints all albums in the list.

Sorting by Number of Songs
The albums1 list is sorted in ascending order based on the number_of_songs field using:
albums1.sort(key=lambda x: x.number_of_songs)

Swapping Elements
After sorting, the program swaps the albums at index positions 0 and 1.

Copying to albums2 and Adding More Albums
The program creates a copy of albums1 named albums2.
Two new Album objects are added:

Dark Side of the Moon

Oops!... I Did it Again

Sorting Alphabetically by Album Name
The albums2 list is sorted alphabetically using:
albums2.sort(key=lambda x: x.album_name)

Searching for a Specific Album
The program searches for "Dark Side of the Moon" within albums2.
When found, it prints the index at which the album occurs.

Running the Program
No external libraries are required.
Run the script using:
python filename.py

This script demonstrates:

Creating objects

Working with lists

Sorting lists with lambda functions

Swapping elements

Copying lists

Searching through a list
