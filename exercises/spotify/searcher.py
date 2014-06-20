import spotipy
import sys

if len(sys.argv) <= 1:
  print "You must provide something to search for!"
  print "python searcher.py '<song or artist>'"
  sys.exit(0)

q = sys.argv[1]

sp = spotipy.Spotify()
tracks = sp.search(q=q, limit=5)

print "Searching for tracks of '{0}'\n".format(q)

for i, t in enumerate(tracks['tracks']['items'], 1):
    name = t['name']
    album = t['album']['name']
    artists = ", ".join(map(lambda a: a['name'], t['artists']))

    print "{3}. {0} - {1} ({2})".format(name, artists, album, i)
