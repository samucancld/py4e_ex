import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('tracksass.sqlite')
cur = conn.cursor()

cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')
fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
found = False

def lookup(track, key):
    found = False
    for item in track:
        if item.tag == 'key' and item.text == key:
            found = True
            continue
        if found == True:
            return item.text
            found == False
            break
    if found == False: return None

for track in all:
    name = lookup(track, 'Name')
    artist = lookup(track, 'Artist')
    album = lookup(track, 'Album')
    count = lookup(track, 'Play Count')
    rating = lookup(track, 'Rating')
    length = lookup(track, 'Total Time')
    genre = lookup(track, 'Genre')

    if name is None or artist is None or album is None or genre is None : continue
    print(f'name: {name}\nartist: {artist}\nalbum: {album}\ncount: {count}\nrating: {rating}\nlength: {length}\ngenre: {genre}')
    

    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES ( ? )', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES ( ? )', (genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]
    
    cur.execute('INSERT OR REPLACE INTO Track(title, album_id, genre_id, len, rating, count) VALUES ( ?, ?, ?, ?, ?, ? )', ( name, album_id, genre_id, length, rating, count ) )
    conn.commit()