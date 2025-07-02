# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:08:57 2017

@author: raphaelle
"""



import nltk
from bs4 import BeautifulSoup
import urllib
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import json

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

url = 'http://renaissanceastrology.com/agrippamercury.html'
html = urllib.urlopen(url)
raw = BeautifulSoup(html).get_text()
raw= u"\n\n\n\n\nCornelius Agrippa on the Things Ruled by Mercury\n\n\n\n\n\n\n\n\nSERVICES\n\n\nPAYMENT\n\n\nCOURSES\n\n\nBOOKS\n\n\nCONTACT\n\n\nSEARCH\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nChristopher Warnock, Esq.\n\n\n\n\n Agrippa on the Things Ruled by Mercury\r\n\r\n\n\n\n\n\nHOME\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCornelius Agrippa on Saturn \n\n\n\n\nCornelius Agrippa on Jupiter \n\n\n\n\nCornelius Agrippa on Mars \n\n\n\n\nCornelius Agrippa on the Sun \n\n\n\n\nCornelius Agrippa on Venus \n\n\n\n\nCornelius Agrippa on Mercury \n\n\n\n\nCornelius Agrippa on the Moon \n\n\n\n\n\n\n\n\nLilly on Saturn \n\n\n\n\nLilly on  Jupiter \n\n\n\n\nLilly on  Mars \n\n\n\n\nLilly on the Sun \n\n\n\n\nLilly on  Venus \n\n\n\n\nLilly on  Mercury \n\n\n\n\nLilly on the Moon \n\n\n  Web Site Search\n\n\n\n\n\n\n\n\nWhat things are Mercurial or\r\nunder the power of Mercury\r\n\n\n\r\nfrom Cornelius Agrippa's Three Books of Occult Philosophy\n\n\n\nElements & Tastes\nMetals & Stones\nPlants & Trees\nFoods\nAnimals\nBirds\nFish\nRegions & Countries\nIncense\nPlaces\n\n\n\n\n\n\n\n\nBOOK ONE\n\n\n\r\nCHAPTER XXIX.\r\n\n What things are under the power of Mercury, and are called Mercuriall.\n\n\n\n\n\nThings under Mercury are these.\r\namongst Elements, Water, although it moves\r\n all things indistinctly. \r\namongst humors, those especially which are mixed, \r\nas also the Animall spirit. amongst tasts those that are various, strange, and mixed. \r\n\r\n\nAmongst  Metals, \r\n Quick-silver, Tin, the Slver Marcasite.\r\n amongst stones, the Emrald, Achates, red Marble, Topaze,\r\n and those which are of divers colours, and various \r\nfigures naturally, & those that are artificiall, as \r\nglass, & those which have a colour mixed with yellow, and green.\r\n\r\n\r\n\nAmongst\r\n  Plants and Trees, \r\n\r\nthe Hazle, Five-leaved-grass, the Hearb Mercury, Fumitary, Pimpernell, \r\nMarjoram, Parsly, and such as have shorter and less leaves,\r\n being compounded of mixed natures, and divers colours.\r\n\r\n\nAmongst \r\n Animals, also, that are of quick sence,\r\n ingenious, strong, inconstant, swift, and such as become easily \r\nacquainted with men, as Dogs, Apes, Foxes, Weesels, the Hart, and Mule. \r\nand all Animals that are of both sexes, and those which can change \r\ntheir Sex, as the Hare, Civet-Cat, and such like.\r\n\r\n\r\n\nAmongst birds, \r\n those which are naturally witty, melodious, and inconstant, as the Linet,\r\n Nightingale, Blackbird, Thrush, Lark, the Gnat-sapper, \r\nthe bird Calandra, the Parret, the Pie, the Bird Ibis, the bird\r\n Porphyrio, the black Betle with one horn. \r\n\r\n\nAnd amongst fish, \r\n\r\nthe fish called Trochius, which goes into himself, \r\nalso Pourcontrell for deceitfulness, and changeableness, \r\nand the Fork fish for its industry. the Mullet also that\r\n shakes off the bait on the hook with his taile. \r\n\r\n\r\n\r\n\r\n\n\n\n\n\r\nCHAPTER XXXI.\r\n\nHow Provinces, and Kingdoms are Distributed to Planets.\n\n\n\n\nTOP\nMercury with Gemini rules Hircania, Armenia, Mantiana,\r\nCyrenaica, Marmarica, and the Lower Egypt. but with Virgo, Greece, Achaia, \r\nCreta, Babylon, Mesopotamia, Assyria, and Ela, whence they of that place are in\r\nScripture called Elamites. \r\n\n\n\n\n\r\nCHAPTER XLIV.\r\n\nThe Composition of Some Fumes Appropriated to the Planets.\n\n\n\n\n\nFor Mercury take mastic, frankincense, cloves and the\r\nherb cinquefoil, and the stone achates, and incorporate them all with the brain of\r\na fox or a weasel and the blood of a pie.\r\n\nTo Mercury, all the peels of wood and fruit, as cinnamon,\r\nlignum-cassia, mace, citron peel, and bayberries, and whatever seeds are odoriferous.\r\n\n\n\n\n\r\nCHAPTER XLVII.\r\n\nWhat Places are Suitable to Every Star\n\n\n\n\n\nTo Mercury, shops, schools, warehouses, an exchange\r\nfor merchants and the like. \r\n\n\n\n\n\n\nTOP\n\n\n\n\nHOME\n\n\n\r\n\r\nPlease Contact me with any Questions or Comments.\r\n\n\r\nCopyright 2003 Christopher Warnock, All Rights Reserved.\r\n\r\n\r\n\r\n\n\n"

sentences = sent_tokenize(raw)
keywords_list = ['Amongst', 'amongst', 'XXXI', 'XLIV', 'XLVII']
idx_list = []
for sent in sentences :
    for keyword in keywords_list :
        if keyword in sent :
            idx_list.append(sentences.index(sent))
        
idx_list = sorted(list(set(idx_list)))
start=-1
stop =0
slices= []
for i in range(len(idx_list)) :
    start+=1
    stop+=1
    try :
        slices.append(sentences[idx_list[start]:idx_list[stop]])
    except IndexError,e :
        slices.append(sentences[idx_list[stop-1]:])
tagged = {}
for i in slices :
    token = []
    for sent in i : 
        token.append(nltk.pos_tag((nltk.word_tokenize(sent))))
    tagged[slices.index(i)]=token
tagged[11] = tagged[11][:-2]

mercury = {}
for k, v in tagged.iteritems() :
    mercury[k] = {}
    for sent in v :
        for word in sent :
            
            if word[0] == "Amongst" :
                mercury[k][sent[sent.index(word) + 1][0]] = []
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                except ValueError, e : 
                    pass
            elif word[0] == "amongst" :
                mercury[k][sent[sent.index(word) + 1][0]] = []
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                except ValueError, e:
                    pass
            elif word[0] == "Animals" :
                mercury[k]["Animals"] = []
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                except ValueError, e:
                    pass
            elif "CHAPTER" in word[0] :
                v.remove(sent)
            elif word[0] == "TOP" :
                try :
                    sent.remove(word)
                except ValueError, e:
                    pass
            elif word[0] == "mercury" :
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                    sent.remove(sent[sent.index(word) - 1])
                except ValueError, e:
                    pass

for sent in tagged[10] :
    for word in sent :
        if "Fumes" in word[0] :
            mercury[10]["Fumes"] = []
            tagged[10].remove(sent)
        elif "fumes" in word[0] :
            sent.remove(word)
for sent in tagged[9] :
    for word in sent :
        if "Provinces" in word[0] :
            mercury[9]["Provinces"] = []
            tagged[9].remove(sent)
for sent in tagged[11] :
    for word in sent :
        if "Places" in word[0] :
            mercury[11]["Places"] = []
cleaned = {}
for k, v in tagged.iteritems() :
    cleaned[k] = []
    for sent in v :
        for word in sent :
            if word[0] not in stopwords.words('english') :
                cleaned[k].append(word[0])
                



for k,v in cleaned.iteritems() :
    idx = list_duplicates_of(cleaned[k], ',')
    stt = -1
    stp=0
    for i in range(len(idx)) :
        stt+=1
        stp+=1
        try :
            mercury[k][mercury[k].keys()[0]].append(v[idx[stt]:idx[stp]])
        except IndexError,e:
            mercury[k][mercury[k].keys()[0]].append(v[idx[stp-1]:])


f = open('~/astrologie/mercury.json', 'w')
f.write(json.dumps(mercury, indent=1))
f.close()


