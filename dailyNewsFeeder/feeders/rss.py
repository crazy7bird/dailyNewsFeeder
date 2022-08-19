#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nturl2path import url2pathname
from operator import ne
import feedparser

def rssFeeder(url : str, deth = 0) :

    #création d’une instance
    news_feed = feedparser.parse(url)
    # Titre du flux
    print("Feed Title:", news_feed.feed.title) 

    # Sous-titre du flux
    print("Feed Subtitle:", news_feed.feed.subtitle)

    # Lien du flux
    print("Feed Link:", news_feed.feed.link, "\n")

    toRead = len(news_feed.entries)
    if(deth > 0) :
        toRead = min(deth, toRead)

    for entry in news_feed.entries:
        print(f"{entry.title} \n--> {entry.link}\n")
        toRead -= 1 
        if toRead == 0 :
            break
 
if __name__ == '__main__':
    deth = 3
    url = 'https://korben.info/feed/'
    rssFeeder(url, deth)

"""
# Création d'une instance
#news_feed = feedparser.parse('https://www.cert.ssi.gouv.fr/alerte/feed/')
news_feed = feedparser.parse('https://korben.info/feed/')

# Propriétés du flux
#print(news_feed.feed.keys())

# Titre du flux
print("Feed Title:", news_feed.feed.title) 

# Sous-titre du flux
print("Feed Subtitle:", news_feed.feed.subtitle)

# Lien du flux
print("Feed Link:", news_feed.feed.link, "\n")

# Propriétés de chaque item du flux
#print(news_feed.entries[0].keys())

for entry in news_feed.entries:
    print(f"{entry.title} \n--> {entry.link}\n")
    
# Récupération du deernier feed (dernier bulletin CERT-FR)
for i in range(0, len(news_feed.entries)):
    if i == (len(news_feed.entries)-1):
        print("Alert: {} \nLink: {}".format(news_feed.entries[0]['title'], news_feed.entries[0]['id']))
"""