# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 10:34:28 2017

@author: raphaelle
"""
import nltk
from bs4 import BeautifulSoup
import urllib
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import json

url = 'http://renaissanceastrology.com/agrippajupiter.html'
html = urllib.urlopen(url)
raw = BeautifulSoup(html).get_text()
raw= u"\n\n\n\n\nCornelius Agrippa on the Things Ruled by the Planet Saturn\n\n\n\n\n\n\n\n\nSERVICES\n\n\nPAYMENT\n\n\nCOURSES\n\n\nBOOKS\n\n\nCONTACT\n\n\nSEARCH\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nChristopher Warnock, Esq.\n\n\n\n\n Agrippa on the Things Ruled by Saturn\r\n\r\n\n\n\n\n\nHOME\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCornelius Agrippa on Saturn \n\n\n\n\nCornelius Agrippa on Jupiter \n\n\n\n\nCornelius Agrippa on Mars \n\n\n\n\nCornelius Agrippa on the Sun \n\n\n\n\nCornelius Agrippa on Venus \n\n\n\n\nCornelius Agrippa on Mercury \n\n\n\n\nCornelius Agrippa on the Moon \n\n\n\n\n\n\n\n\nLilly on Saturn \n\n\n\n\nLilly on  Jupiter \n\n\n\n\nLilly on  Mars \n\n\n\n\nLilly on the Sun \n\n\n\n\nLilly on  Venus \n\n\n\n\nLilly on  Mercury \n\n\n\n\nLilly on the Moon \n\n\n  Web Site Search\n\n\n\n\n\n\n\n\nWhat things are Saturnine or\r\nunder the power of Saturn\r\n\n\n\r\nfrom Cornelius Agrippa's Three Books of Occult Philosophy\n\n\n\nElements & Tastes\nMetals & Stones\nPlants & Trees\nFoods\nAnimals\nBirds\nFish\nRegions & Countries\nIncense\nPlaces\n\n\n\n\n\n\n\n\nBOOK ONE\n\n\n\r\nCHAPTER XXVI.\r\n\n Chapter xxv. What things are Saturnine, or under the power of Saturne.\n\n\n\n\n\nSaturnine things, \r\namongst Elements, are Earth and , Water.\r\nAmongst humors, black Choller that is moist, \r\nas well natural, as adventitious, adust Choller  excepted. \r\nAmongst tasts, soure, tart, and dead. Amongst  Metals, Lead, and Gold, \r\nby reason of its weight, and the golden Marcasite. Amongst stones, \r\nthe Onix, the Ziazaa, the Camonius, the Sapphire, the brown Jasper, \r\nthe Chalcedon, the Loadstone, and all dark, weighty, earthy things.\r\n\r\n\r\n\r\n\nAmongst\r\n  Plants and Trees, the Daffodill, Dragonwort, \r\nRue, Cummin, Hellebor, the tree from whence Benzoine comes, \r\nMandrake, Opium, and those things which stupifie, and those \r\nthings which are never sown, and never bear fruit, and those \r\nwhich bring forth berries of a dark colour, and black fruit, \r\nas the black Fig-tree, the Pine-tree, the Cypress-tree, \r\n\nAnd \r\na certain tree used at burials, which never springs afresh with \r\nberries, rough, of a bitter tast, of a strong smell, of \r\na black shadow, yielding a most sharp pitch, bearing a most unprofitable fruit, \r\nnever dies with age, deadly, dedicated to Pluto, as is the Hearb pass-flower, \r\nwith which they were wont Anciently to strow the graves before they put \r\nthe dead bodies into them, wherefore it was lawfull to make their Garlands \r\nat feasts with all Hearbs, and Flowers besides pas-flowers, because \r\nit was mournfull, and not conducing to mirth.\r\n\r\n\nAlso all creeping  Animals,\r\n living apart, \r\nand solitary, nightly, sad, contemplative, dull, covetous, \r\nfearfull, melancholly, that take much pains, slow, that feed grossly, \r\nand such as eat their young. Of these kinds therefore are the Ape, \r\nthe Cat, the Hog, the Mule, the Camel, the Bear, the Mole, the Asses, \r\nthe Wolfe, the Hare, the Dragon, the Basilisk, the Toad, \r\nall Serpents, and creeping things, Scorpions, Pismires, and such\r\n things as proceed from putrefaction in the Earth, in Water, or \r\nin the ruines of houses, as Mice, and many sorts of Vermin.\r\n\r\n\nAmongst birds, \r\nthose are Saturnine, which have long necks, and harsh voices, as\r\n Cranes, Estriches, and Peacocks, which are dedicated to\r\n Saturn, and Juno. Also the scrich-Owle, the horn-Owle, the Bat, \r\nthe Lapwing, the Crow, the Quaile, which is the most envious bird of all.\r\n\r\n\nAmongst fishes, \r\nthe Eel, living apart from all other fish, \r\nthe Lamprey, the Dog-fish, which devours her young, \r\nalso the Tortoise, Oisters, Cockles, to which may be added Sea-spunges, \r\nand all such things as come of them. \r\n\r\n\r\n\r\n\r\n\n\n\n\n\r\nCHAPTER XXXI.\r\n\nHow Provinces, and Kingdoms are Distributed to Planets.\n\n\n\n\nTOP\nMacedonia, Thracia, Illyria, India, Ariana, Gordiana\r\n(many of which are countries in the lesser Asia) are under Saturn with Capricorn;\r\nbut with Aquarius under him are the Sauromantian country, Oxiana, Sogdiana, \r\nArabia, Phazania, Media, Ethiopia, which countries for the most part belong to\r\nthe more inward Asia. \r\n\r\n\r\n\n\n\n\n\r\nCHAPTER XLIV.\r\n\nThe Composition of Some Fumes Appropriated to the Planets.\n\n\n\n\n\nFor Saturn take the seed of black poppy, of henbane,\r\nthe root of mandrake, the loadstone and myrrh, and make them up with the brain of \r\na cat or the blood of a bat...\r\n\nTo Saturn are appropriated for fumes all odoriferous\r\nroots, as pepperwort root, etc., and the frankincense tree. CHAPTER XLVII.\r\n\nWhat Places are Suitable to Every Star\n\n\n\n\n\nBut amongst places that are appropriated to the stars, all \r\nstinking places, dark, underground, religious and mournful places, as churchyards, tombs,\r\nand houses not inhabited by men, and old, tottering, obscure, dreadful houses, \r\nand solitary dens, caves and pits, also fishponds, standing pools, fens and such like\r\nare appropriated to Saturn.  \r\n\n\n\n\n\n\nTOP\n\n\n\n\nHOME\n\n\n\r\n\r\nPlease Contact me with any Questions or Comments.\r\n\n\r\nCopyright 2003 Christopher Warnock, All Rights Reserved.\r\n\r\n\r\n\r\n\n\n"
sentences = sent_tokenize(raw)
keywords_list = ['Amongst', 'amongst', 'Animals', 'XXXI', 'XLIV']
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
saturn = {}
for k, v in tagged.iteritems() :
    saturn[k] = {}
    for sent in v :
        for word in sent :
            
            if word[0] == "Amongst" :
                saturn[k][sent[sent.index(word) + 1][0]] = []
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                except ValueError, e : 
                    pass
            elif word[0] == "amongst" :
                saturn[k][sent[sent.index(word) + 1][0]] = []
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                except ValueError, e:
                    pass
            elif word[0] == "Animals" :
                saturn[k]["Animals"] = []
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
            elif word[0] == "Saturn" :
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                    sent.remove(sent[sent.index(word) - 1])
                except ValueError, e:
                    pass

for sent in tagged[11] :
    for word in sent :
        if "Fumes" in word[0] :
            saturn[11]["Fumes"] = []
            tagged[11].remove(sent)
        elif "fumes" in word[0] :
            sent.remove(word)
for sent in tagged[10] :
    for word in sent :
        if "Provinces" in word[0] :
            saturn[10]["Provinces"] = []
            tagged[10].remove(sent)
cleaned = {}
for k, v in tagged.iteritems() :
    cleaned[k] = []
    for sent in v :
        for word in sent :
            if word[0] not in stopwords.words('english') :
                cleaned[k].append(word[0])
                
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


for k,v in cleaned.iteritems() :
    idx = list_duplicates_of(cleaned[k], ',')
    stt = -1
    stp=0
    for i in range(len(idx)) :
        stt+=1
        stp+=1
        try :
            saturn[k][saturn[k].keys()[0]].append(v[idx[stt]:idx[stp]])
        except IndexError,e:
            saturn[k][saturn[k].keys()[0]].append(v[idx[stp-1]:])

f = open('~/astrologie/saturn.json', 'w')
f.write(json.dumps(saturn, indent=1))
f.close()

        
