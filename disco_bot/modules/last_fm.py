import disco_bot.config;
import requests as req;
import grequests as greq;
import time;

from youtubesearchpython import VideosSearch;

from disco_bot.config import Development as Config
api_key = Config.API_KEY
user_agent = Config.USER_AGENT;

#chart top tracks
def chart():
	i = 0;
	url = "http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key=" + api_key + "&format=json";
	res = req.get(url);
	tracks = [];
	for r in res.json()['tracks']['track']:
		searches = VideosSearch((str(r['name']) + " - " + str(r['artist']['name']) + " lyrics"), limit = 1);
		for v in searches.result()['result']:
			tracks.append(str(r['name']) + " - " + str(r['artist']['name']) + "\n" + v['link'] + "\n");
		i += 1;
		if(i+1 == 11): break;
	return tracks;


#songs by artist
def artist(artist):
	i = 0;
	url = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=" + artist +"&api_key=" + api_key + "&format=json"
	res = req.get(url);
	artist_track = [];
	for r in res.json()['toptracks']['track']:
		searches = VideosSearch((str(r['name']) + " - " + artist + " lyrics"), limit = 1);
		for v in searches.result()['result']:
			artist_track.append(str(r['name']) + " - " + v['link'] + "\n");
		i += 1;
		if(i+1 == 11): break;
	return artist_track;


#get genre playlist from last.fm
def genre(genre):
	links = [];
	searches = VideosSearch(genre+" playlist", limit=10);
	for v in searches.result()['result']:
		links.append(str(v['link']) + " - " + str(v['title']) + "\n");
	return links;
