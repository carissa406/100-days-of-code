import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "90ab173b27f246de8f27c568f2aebf57"
CLIENT_SECRET = "80923625a75948c093d557d9ee62002c"
REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"
USERNAME = "121236184"

travel_year = "1996-04-06"
#input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{travel_year}/"

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')
titles = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in titles]

#print(song_names)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME))

user_id = sp.current_user()["id"]
#print(user_id)

song_ids = []
#i = 0
for song in song_names:
    result = sp.search(q=song,
                type="track",
                limit=1)
    #i+=1
    #print(i)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_ids.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify")

#print(song_ids)
        
result = sp.user_playlist_create(user=USERNAME,
                        name=f"{travel_year} Billboard 100",
                        public=False,
                        collaborative=False,
                        description="top 100s")
#print(result)

sp.playlist_add_items(playlist_id=result["id"],
                      items=song_ids)