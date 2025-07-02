# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 14:27:24 2017

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

url = 'http://renaissanceastrology.com/agrippamars.html'
html = urllib.urlopen(url)
raw = BeautifulSoup(html).get_text()
raw= u"\n\n\n\n\nCornelius Agrippa on the Things Ruled by the Planet Mars\n\n\n\n\n\n\n\n\nSERVICES\n\n\nPAYMENT\n\n\nCOURSES\n\n\nBOOKS\n\n\nCONTACT\n\n\nSEARCH\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nChristopher Warnock, Esq.\n\n\n\n\n Agrippa on the Things Ruled by Mars\r\n\n\n\n\n\nHOME\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCornelius Agrippa on Saturn \n\n\n\n\nCornelius Agrippa on Jupiter \n\n\n\n\nCornelius Agrippa on Mars \n\n\n\n\nCornelius Agrippa on the Sun \n\n\n\n\nCornelius Agrippa on Venus \n\n\n\n\nCornelius Agrippa on Mercury \n\n\n\n\nCornelius Agrippa on the Moon \n\n\n\n\n\n\n\n\nLilly on Saturn \n\n\n\n\nLilly on  Jupiter \n\n\n\n\nLilly on  Mars \n\n\n\n\nLilly on the Sun \n\n\n\n\nLilly on  Venus \n\n\n\n\nLilly on  Mercury \n\n\n\n\nLilly on the Moon \n\n\n  Web Site Search\n\n\n\n\n\n\n\n\nWhat things are Martial or\r\nunder the power of Mars\r\n\n\n\r\nfrom Cornelius Agrippa's Three Books of Occult Philosophy\n\n\n\nElements & Tastes\nMetals & Stones\nPlants & Trees\nFoods\nAnimals\nBirds\nFish\nRegions & Countries\nIncense\nPlaces\n\n\n\n\n\n\n\n\nBOOK ONE\n\n\n\r\nCHAPTER XXVII.\r\n\n What things are under the power of Mars, and are called Martial.\n\n\n\n\n\nThings are Martiall, \r\namongst Elements, Fire, together with all adust, \r\nand sharp things. Amongst humours, Choller . \r\nalso bitter tasts, tart, and burning the tongue, and causing tears.\r\n\r\n\nAmongst  Metals, \r\nIron, and red Brass. and all fiery, red, and \r\nsulphureous things. Amongst Stones the Diamond, Loadstone, \r\nthe Blood-stone, the Jasper, the stone that consists\r\n of divers kinds, and the Amethist. \r\n\r\n\nAmongst\r\n  Plants and Trees, Hellebor, Garlick, \r\nEuphorbium, Cartabana, Armoniack, \r\nRadish, the Laurell, Wolfs-bane, Scammony, and all such as\r\n are poysonous, by reason of too much heat, and those which\r\n are beset round about with prickles, or by touching the skin, burn it, \r\nprick it, or make it swell, as Cardis, the Nettle, Crow-foot, \r\n\r\n\r\n\r\n\nAand such as being eaten  \r\n cause tears, as Onyons, \r\nAscolonia, Leeks, Mustardseed, and all thorny Trees, \r\nand the Dog-tree, which is dedicated to Mars.\r\n\r\n\nAnd all such Animals \r\n as are warlike, ravenous, bold, and of clear fancy, \r\nas the Horse, Mule, Goat, Kid, Wolf, Libard, \r\nthe wild Ass. Serpents also, and Dragons full of displeasure \r\nand poyson. also all such as are offensive to men, \r\nas Gnats, Flies, Baboon, by reason of his anger.\r\n\r\n\nAll such birds, \r\n\r\nthat are ravenous, devour flesh, break bones, as the Eagle,\r\n the Faulcon, the Hawk, the Vultur. and those \r\nwhich are called the fatall Birds, as the Horn-Owl, the Scrich-Owl, \r\nCastrels, Kites, and such as are hungry, and \r\nravenous, and such as make a noise in their swallowing, \r\nas Crows, Daws, the Pie, which above all the rest is dedicated to Mars.\r\n\r\n\r\n\nAnd amongst fishes, \r\n\r\nthe Pike, the Barbell, the Fork-fish, the Fish that hath horns like a Ram, \r\nthe Sturgeon, the Glacus, all which are great devourers, and ravenous. \r\n\r\n\r\n\r\n\n\n\n\n\r\nCHAPTER XXXI.\r\n\nHow Provinces, and Kingdoms are Distributed to Planets.\n\n\n\n\nTOP\nMars with Aries governs Brittany, France, Germany,\r\nBastarnia, the lower parts of Syria, Idumea and Judea. with Scorpio he rules\r\nSyria, Comagena, Cappadocia, Metagonium, Mauritania and Getulia.\r\n\r\n\n\n\n\n\r\nCHAPTER XLIV.\r\n\nThe Composition of Some Fumes Appropriated to the Planets.\n\n\n\n\n\nFor Mars take euphorbium, bdellium, gum armoniac, \r\nthe roots of both hellebores, the loadstone and a little sulfure, and incorporate\r\nthem all with the brain of a hart, the blood of a man and the blood of a black\r\ncat..\r\n\nTo Mars, all odoriferous woods, as sanders, cypress,\r\nlignum balsam, and lignum aloes.\r\n\n\n\n\n\r\nCHAPTER XLVII.\r\n\nWhat Places are Suitable to Every Star\n\n\n\n\n\nTo Mars, fiery and bloody places, furnacnes, bakehouses,\r\nshambles, places of execution and and places where there have been great battles\r\nfought and slaughters made and the like. \r\n\n\n\n\n\n\nTOP\n\n\n\n\nHOME\n\n\n\r\n\r\nPlease Contact me with any Questions or Comments.\r\n\n\r\nCopyright 2003 Christopher Warnock, All Rights Reserved.\r\n\r\n\r\n\r\n\n\n"

sentences = sent_tokenize(raw)

keywords_list = ['Amongst', 'amongst', 'tasts', 'Animals', 'birds', 'XXXI', 'XLIV', 'XLVII']
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
tagged[12] = tagged[12][:-2]
del tagged[0]
mars = {}
for k, v in tagged.iteritems() :
    mars[k] = {}
    for sent in v :
        for word in sent :
            
            if word[0] == "Amongst" :
                mars[k][sent[sent.index(word) + 1][0]] = []
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                except ValueError, e : 
                    pass
            elif word[0] == "amongst" :
                mars[k][sent[sent.index(word) + 1][0]] = []
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                except ValueError, e:
                    pass
            elif word[0] == "Animals" :
                mars[k]["Animals"] = []
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
            elif word[0] == "mars" :
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                    sent.remove(sent[sent.index(word) - 1])
                except ValueError, e:
                    pass

for sent in tagged[11] :
    for word in sent :
        if "Fumes" in word[0] :
            mars[11]["Fumes"] = []
            tagged[11].remove(sent)
        elif "fumes" in word[0] :
            sent.remove(word)
for sent in tagged[10] :
    for word in sent :
        if "Provinces" in word[0] :
            mars[10]["Provinces"] = []
            tagged[10].remove(sent)
for sent in tagged[12] :
    for word in sent :
        if "Places" in word[0] :
            mars[12]["Places"] = []
for sent in tagged[3] :
    for word in sent :
        if "tasts" in word[0] :
            mars[3]["tasts"] = []
for sent in tagged[8] :
    for word in sent :
        if "birds" in word[0] :
            mars[8]["birds"] = []
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
            mars[k][mars[k].keys()[0]].append(v[idx[stt]:idx[stp]])
        except IndexError,e:
            mars[k][mars[k].keys()[0]].append(v[idx[stp-1]:])


f = open('~/astrologie/mars.json', 'w')
f.write(json.dumps(mars, indent=1))
f.close()


