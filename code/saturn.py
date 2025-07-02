# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 10:34:28 2017

@author: raphaelle
"""
import nltk
from bs4 import BeautifulSoup
import urllib
url = 'http://renaissanceastrology.com/agrippasaturn.html'
html = urllib.urlopen(url)
#raw = html.read().decode('utf8')
raw = BeautifulSoup(html).get_text()
tokens = nltk.word_tokenize(raw)
#tokens = [w.lower() for w in tokens]
tagged = nltk.pos_tag(tokens)[:-20]
idx_list = []
for e in tagged :
    if e[0] == 'TOP' :
        tagged.remove(e)
    elif e[0] == 'Amongst':
        idx_list.append(tagged.index(e))
    elif e[0] == 'amongst' :
        idx_list.append(tagged.index(e))
    elif 'Amongst' in e[0] :
        idx_list.append(tagged.index(e))
    elif e[0] == 'Amongst' and e[1] == 'NNP' :
        idx_list.append(tagged.index(e))
    elif e[0] == 'XLIV':
        idx_list.append(tagged.index(e))
    elif e[0] == 'XXXI' :
        idx_list.append(tagged.index(e))
idx_list = sorted(list(set(idx_list)))
start=-1
stop =0
slices= {}
for i in idx_list :
    try :
        start+=1
        stop+=1
        slices[start] = tagged[idx_list[start]:idx_list[stop]]
    except IndexError,e :
        slices[start] = tagged[idx_list[-1]:]

