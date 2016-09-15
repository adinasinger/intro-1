from urllib2 import urlopen
from json import load
from Movie_class import *

apiURL = "https://data.sfgov.org/resource/wwmu-gmzc.json?"

#release_year=2002
#filter for films shot in SF and released in 2002 

response = urlopen(apiURL)

json_obj = load(response)

#print json_obj

film_list = []
for i in json_obj:
	for item in i:
		if i[item] == "2002":
			if i["title"] not in film_list:
#				film_list.append(i["title"])
				director = (i["director"])
				release_year = (i["release_year"])
				
				
print director

# for film in film_list:
# 	print film

#for each film in JSON,
# MovieInfo(director, release_year, title, actor_1, actor_2, location)

#film_title = MovieInfo(director, release_year, title, actor_1, actor_2, location)