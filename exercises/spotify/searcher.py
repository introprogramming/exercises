import spotipy
import sys

# Create new API object wrapper
sp = spotipy.Spotify()

# Format a track: "Track name – Artist, Album"
def format_track(track):
  name = track['name'].encode('utf8')
  album = track['album']['name'].encode('utf8')
  artists = ", ".join(map(lambda a: a['name'], track['artists'])).encode('utf8')

  return "{0} - {1} ({2})".format(name, artists, album)

# Format an artist: "Artist name"
def format_artist(artist):
  return artist['name'].encode('utf8')

# Print API results with a formatter
def show_results(results, formatter):
  for i, t in enumerate(results['items'], 1):
    print "{0}. {1}".format(i, formatter(t))

# Search Spotify for a query with a limit
def search(query, limit):

  tracks = sp.search(q=query, limit=limit)
  artists = sp.search(q=query, limit=limit, type='artist')

  # Tracks

  print "\n"
  print "Found {1} tracks with: '{0}'\n".format(query, tracks['tracks']['total'])

  if tracks['tracks']['total'] > limit:
    print "(showing {0} first)".format(limit)

  show_results(tracks['tracks'], format_track)

  # Artists

  print "\n"
  print "Found {1} artists with: '{0}'\n".format(query, artists['artists']['total'])

  if artists['artists']['total'] > limit:
    print "(showing {0} first)".format(limit)

  show_results(artists['artists'], format_artist)

  print "\n"

# Usage:
#
#   python searcher.py <track or artist>
if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print "You must provide something to search for!"
    print "python searcher.py '<song or artist>'"
    sys.exit(0)

  search(sys.argv[1], limit=5)
