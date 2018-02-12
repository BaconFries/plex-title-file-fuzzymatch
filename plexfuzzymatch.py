#!/usr/bin/env python
import plexapi
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from plexapi.server import PlexServer

baseurl = 'http://127.0.0.1:32400'
token   = ''
plex    = PlexServer(baseurl, token)
movies  = plex.library.section('HD Movies').all( )

for movie in movies:
  for part in movie.iterParts():
    score = fuzz.token_set_ratio( movie.title, part.file )
    if score < 94:
      print "score: " + str(score) + " title: " + movie.title + "\tfile: " + part.file