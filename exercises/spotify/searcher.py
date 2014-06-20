import spotipy
import sys

if len(sys.argv) <= 1:
  print "You must provide something to search for!"
  print "python searcher.py <song or artist>"
  sys.exit(0)


sp = spotipy.Spotify()
tracks = sp.search(q='Stairway To Heaven', limit=5)

for i, t in enumerate(tracks['tracks']['items']):
    name = t['name']
    album = t['album']['name']
    artists = ", ".join(map(lambda a: a['name'], t['artists']))

    print "{0} - {1} ({2})".format(name, artists, album)
