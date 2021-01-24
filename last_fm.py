import keys;
import requests as req;
import threading;
import time;

from youtubesearchpython import VideosSearch;

api_key = keys.lfm_api_key();
user_agent = keys.lfm_user_agent();


tracks = [];
threads  = [];

#thread requests
def thread_reqs(name, artist_name, i, func):
	tracks.clear();
	searches = VideosSearch((name + " - " + artist_name + " lyrics"), limit = 1);
	if func=="chart":
		for v in searches.result()['result']:
			tracks.insert(i, (name + " - " + artist_name + "\n" + v['link'] + "\n"));
	elif func=="artist":
		for v in searches.result()['result']:
			tracks.insert(i, (name + " - " + v['link'] + "\n"));

#chart top tracks - threads
def chart_t():
	i = 0;
	url = "http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key=" + api_key + "&format=json";
	res = req.get(url);
	for r in res.json()['tracks']['track']:
		process = threading.Thread(target = thread_reqs, args = [str(r['name']), str(r['artist']['name']), i, 'chart']);
		process.start();
		threads.append(process);
		i += 1;
		if i == 10: break;

	for process in threads:
		process.join();
	
	return tracks;

#artist top 10 tracks - threads
def artist_t(artist):
	i = 0;
	try:
		url = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=" + artist +"&api_key=" + api_key + "&format=json"
		res = req.get(url);
		for r in res.json()['toptracks']['track']:
			process = threading.Thread(target = thread_artist, args = [str(r['name']), str(r['artist']['name']), i, 'artist']);
			process.start();
			threads.append(process);
			i += 1;
			if i == 10 : break;
	except KeyError: print("Artist not found");

	for process in threads:
		process.join();

	return tracks;

#chart top tracks
def chart():
	tracks.clear();
	i = 0;
	url = "http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key=" + api_key + "&format=json";
	res = req.get(url);
	try:
		for r in res.json()['tracks']['track']:
			# takes and avg of 1.2s for each request w/o threading.
			searches = VideosSearch((str(r['name']) + " - " + str(r['artist']['name']) + " lyrics"), limit = 1);
			for v in searches.result()['result']:
				tracks.append(str(r['name']) + " - " + str(r['artist']['name']) + "\n" + v['link'] + "\n");
			i += 1;
			if i == 10: break;
	except Exception as e:
		print(e.__class__);
	
	return tracks;


#songs by artist
def artist(artist):
	tracks.clear();
	i = 0;
	try:
		url = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=" + artist +"&api_key=" + api_key + "&format=json"
		res = req.get(url);
		for r in res.json()['toptracks']['track']:
			searches = VideosSearch((str(r['name']) + " - " + artist + " lyrics"), limit = 1);
			for v in searches.result()['result']:
				artist_track.append(str(r['name']) + " - " + v['link'] + "\n");
			i += 1;
			if i == 10: break;
	except KeyError: print("Artist not found");

	return tracks;


#get genre playlist from last.fm
def genre(genre):
	tracks.clear();
	try:
		searches = VideosSearch(genre+" playlist", limit=10);
		for v in searches.result()['result']:
			links.append(str(v['link']) + " - " + str(v['title']) + "\n");
	except Exception as e: print(e.__class__);

	return tracks;
