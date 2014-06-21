import spotipy
import sys

sp = spotipy.Spotify()

def search(query, limit):

  tracks = sp.search(q=query, limit=limit)
  artists = sp.search(q=query, limit=limit, type='artist')

  print "Found {1} tracks with: '{0}' (showing {2} first)\n".format(query, tracks['tracks']['total'], limit)

  for i, t in enumerate(tracks['tracks']['items'], 1):
      _name = t['name'].encode('utf8')
      _album = t['album']['name'].encode('utf8')
      _artists = ", ".join(map(lambda a: a['name'], t['artists'])).encode('utf8')

      print "{3}. {0} - {1} ({2})".format(_name, _artists, _album, i)

  print "\nFound {1} artists with: '{0}' (showing {2} first)\n".format(query, artists['artists']['total'], limit)

  for i, t in enumerate(artists['artists']['items'], 1):
      name = t['name'].encode('utf8')

      print "{0}. {1}".format(i, name)


if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print "You must provide something to search for!"
    print "python searcher.py '<song or artist>'"
    sys.exit(0)

  search(sys.argv[1], limit=5)
