import keys;
import requests as req;
import threading;
import time;

from youtubesearchpython import VideosSearch;

api_key = keys.lfm_api_key();
user_agent = keys.lfm_user_agent();

tracks = list(range(0,10));
empty = [];
threads  = [];

#threading function
def thread_reqs(name, artist_name, i, func):
	try: searches = VideosSearch((name + " - " + artist_name + " lyrics"), limit = 1);
	except: thread_reqs(name, artist_name, i, func);
	if func=="chart":
		for v in searches.result()['result']:
			#print(i, "(t)", name, " - ", artist_name);
			tracks[i] = (name + " - " + artist_name + "\n" + v['link'] + "\n");
	elif func=="artist":
		for v in searches.result()['result']:
			tracks[i] = (name + " - " + v['link'] + "\n");

#chart top tracks - threads
def chart():
	#tracks = list(range(0,10));
	i = 0;
	try:
		url = "http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key=" + api_key + "&format=json";
		res = req.get(url);
		for r in res.json()['tracks']['track']:
			process = threading.Thread(target = thread_reqs, args = [str(r['name']), str(r['artist']['name']), i, "chart"]);
			process.start();
			threads.append(process);
			i += 1;
			if i == 10: break;
	except Exception as e: 
		print(e);
		return empty;

	for process in threads:
		process.join();
	
	return tracks;

#artist top 10 tracks - threads
def artist(artist):
	#tracks = list(range(0,10));
	i = 0;
	try:
		url = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=" + artist +"&api_key=" + api_key + "&format=json"
		res = req.get(url);
		for r in res.json()['toptracks']['track']:
			process = threading.Thread(target = thread_reqs, args = [str(r['name']), str(r['artist']['name']), i, "artist"]);
			process.start();
			threads.append(process);
			i += 1;
			if i == 10: break;
	except KeyError: 
		print("Artist Not Found");
		return empty;

	for process in threads:
		process.join();

	return tracks;


#get genre playlist from last.fm
def genre(genre):
	tracks.clear();
	try:
		try: searches = VideosSearch(genre+" playlist", limit=10);
		except: genre(genre);
		for v in searches.result()['result']:
			tracks.append(str(v['link']) + " - " + str(v['title']) + "\n");
	except Exception as e: 
		print(e);
		return empty;

	return tracks;
