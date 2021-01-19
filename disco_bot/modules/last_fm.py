import disco_bot.config;
import requests as req;
from youtube_search import YoutubeSearch as yt;

from disco_bot.config import Development as Config
api_key = Config.API_KEY
user_agent = Config.USER_AGENT;

#chart top tracks
def chart():
	i = 1;
	url = "http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key=" + api_key + "&format=json";
	res = req.get(url);
	tracks = [];
	for r in res.json()['tracks']['track']:
		if(i == 11): break;
		track_url = yt((str(r['name']) + " - " + str(r['artist']['name']) + " lyrics"), max_results=1).to_dict();
		for t in track_url:
			yt_url = "https://www.youtube.com/watch?v=" + str(t['id']);
		text = str(r['name']) + " - " + str(r['artist']['name']) + "\n" + yt_url + "\n";
		tracks.append(text);
		i += 1;
	return tracks;


#songs by artist
def artist(artist):
	i = 1;
	url = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=" + artist +"&api_key=" + api_key + "&format=json"
	res = req.get(url);
	artist_track = [];
	for r in res.json()['toptracks']['track']:
		if(i == 11): break;
		track_url = yt((str(r['name']) + " - " + artist + " lyrics"), max_results=1).to_dict();
		for t in track_url:
			yt_url = "https://www.youtube.com/watch?v=" + str(t['id']);
		text = str(r['name']) + " - " + yt_url + "\n";
		artist_track.append(text);
		i += 1; print(i);
	return artist_track;


#get genre playlist from last.fm
def genre(genre):
	links = [];
	yt_url = yt(genre+" playlist", max_results=10).to_dict();
	for r in yt_url: 
		links.append("https://www.youtube.com/watch?v=" + str(r['id']) + " - " + str(r['title']) +"\n");
	return links;
