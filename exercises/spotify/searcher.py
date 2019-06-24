import spotipy
import spotipy.oauth2 as oauth2
import sys
import auth_data

try:
    credentials = oauth2.SpotifyClientCredentials(
        client_id=auth_data.client_id,
        client_secret=auth_data.client_secret)
except oauth2.SpotifyOauthError:
    print(
        "Invalid client_id or secrept provided, make sure to register the application at "
        "https://developer.spotify.com/dashboard/ and then fill out the 'client_id' and 'client_secret' fields in "
        "auth_data.py in order to use this application.")
    sys.exit(1)

token = credentials.get_access_token()

# Create new API object wrapper
spotify = spotipy.Spotify(auth=token)

# Format a track: "Track name – Artist, Album"
def format_track(track):
    name = track['name']
    album = track['album']['name']
    artists = ", ".join(map(lambda a: a['name'], track['artists']))

    return "{0} - {1} ({2})".format(name, artists, album)


# Format an artist: "Artist name"
def format_artist(artist):
    return artist['name']


# Print API results with a formatter
def show_results(results, formatter):
    for i, t in enumerate(results['items'], 1):
        print("{0}. {1}".format(i, formatter(t)))


# Search Spotify for a query with a limit
def search(query, limit):
    tracks = spotify.search(q=query, limit=limit)
    artists = spotify.search(q=query, limit=limit, type='artist')

    # Tracks

    print("\n")
    print("Found {1} tracks with: '{0}'\n".format(query, tracks['tracks']['total']))

    if tracks['tracks']['total'] > limit:
        print("(showing {0} first)".format(limit))

    show_results(tracks['tracks'], format_track)

    # Artists

    print("\n")
    print("Found {1} artists with: '{0}'\n".format(query, artists['artists']['total']))

    if artists['artists']['total'] > limit:
        print("(showing {0} first)".format(limit))

    show_results(artists['artists'], format_artist)

    print("\n")


# Usage:
#
#   python searcher.py <track or artist>
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("You must provide something to search for!")
        print("python searcher.py '<song or artist>'")
        sys.exit(0)

    search(sys.argv[1], limit=5)
