#!/usr/bin/env python
import plexapi
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from plexapi.server import PlexServer

baseurl = 'http://127.0.0.1:32400'
token   = ''
plex    = PlexServer(baseurl, token)

movies = plex.library.section('Movies').all( )
for movie in movies:
  for part in movie.iterParts():
    score = fuzz.token_set_ratio( movie.title, part.file )
    if score < 94:
      print "score: " + str(score) + " title: " + movie.title + "\tfile: " + part.file

tvshows = plex.library.section('TV Shows').all()
for tv in tvshows:
  for episode in tv.episodes():
    showname = tv.title + '.s' + str(episode.parentIndex).zfill(2) + 'e' + str(episode.index).zfill(2)
    for part in episode.iterParts():
      score = fuzz.token_set_ratio( showname, part.file )
      if score < 89:
        print "score: " + str(score) + " title: " + showname+ "\tfile: " + part.file