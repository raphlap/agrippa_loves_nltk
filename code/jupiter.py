# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:53:25 2017

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

url = 'http://renaissanceastrology.com/agrippajupiter.html'
html = urllib.urlopen(url)
raw = BeautifulSoup(html).get_text()
raw= "\n\n\n\n\nCornelius Agrippa on the Things Ruled by the Planet Jupiter\n\n\n\n\n\n\n\n\nSERVICES\n\n\nPAYMENT\n\n\nCOURSES\n\n\nBOOKS\n\n\nCONTACT\n\n\nSEARCH\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nChristopher Warnock, Esq.\n\n\n\n\n Agrippa on the Things Ruled by Jupiter\r\n\r\n\n\n\n\n\nHOME\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCornelius Agrippa on Saturn \n\n\n\n\nCornelius Agrippa on Jupiter \n\n\n\n\nCornelius Agrippa on Mars \n\n\n\n\nCornelius Agrippa on the Sun \n\n\n\n\nCornelius Agrippa on Venus \n\n\n\n\nCornelius Agrippa on Mercury \n\n\n\n\nCornelius Agrippa on the Moon \n\n\n\n\n\n\n\n\nLilly on Saturn \n\n\n\n\nLilly on  Jupiter \n\n\n\n\nLilly on  Mars \n\n\n\n\nLilly on the Sun \n\n\n\n\nLilly on  Venus \n\n\n\n\nLilly on  Mercury \n\n\n\n\nLilly on the Moon \n\n\n  Web Site Search\n\n\n\n\n\n\n\n\nWhat things are Jovial or\r\nunder the power of Jupiter\r\n\n\n\r\nfrom Cornelius Agrippa's Three Books of Occult Philosophy\n\n\n\nElements & Tastes\nMetals & Stones\nPlants & Trees\nFoods\nAnimals\nBirds\nFish\nRegions & Countries\nIncense\nPlaces\n\n\n\n\n\n\n\n\nBOOK ONE\n\n\n\r\nCHAPTER XXVI.\r\n\n What things are under the power of Jupiter, and are called Jovial.\n\n\n\n\n\nThings under Jupiter, \r\namongst Elements, are the Aire.\r\n amongst humors, blood, and the spirit of life, also all\r\n things which respect the encrease, nourishment, and vegetation of the life. \r\nAmongst tasts such as are sweet, and pleasant. \r\n\r\n\nAmongst  Metals, Tin, Silver, \r\nand Gold, by reason of their temperateness. Amongst stones, the Hyacinth, Beril, \r\nSaphir, the Emrald, green Jasper, and aiery colours. \r\n\r\n\nAmongst\r\n  Plants and Trees, Sea-green, Garden Basil, Bugloss, Mace, \r\nSpike, Mints, Mastick, Elicampane, the Violet, Darnell, Henbane, \r\nthe Poplar tree, and those which are called lucky trees, as the Oak, the tree aesculus \r\nwhich is like an Oak but much bigger, the Holm tree, the Beech tree, the Hasle tree, \r\nthe Service tree, the white Fig tree, the Pear tree, the Apple tree, the Vine, \r\nthe Plum tree, the Ash, the Dog-tree, and the Olive tree, and also Oile. \r\n\r\n\nAlso all manner of  Corn, \r\nas Barley, Wheat, also Raisins,\r\n Licorish , Sugar, and \r\nall such things whose sweetness is manifest, and subtile, partaking somewhat of \r\nan astringent, and sharp tast, as are Nuts, Almonds, Pine-apples, Filberds, \r\nPistake Nuts, roots of Peony, Mirabolaus, Rhubarb, and Manna, \r\nOrpheus adds Storax. \r\n\r\n\nAmongst  Animals such as have some stateliness, and wisdom in them, \r\nand those which are mild, well trained up, and of good dispositions, \r\nas the Hart and Elephant, and those which are gentle, as Sheep and Lambs. \r\n\r\n\nAmongst birds, \r\nthose that are of a temperate complexion, as Hens, \r\ntogether with the Yolk of their Eggs. Also the Partridge, the Pheasant, \r\nthe Swallow, the Pellican, the Cuckow, the Stork, birds \r\ngiven to a kind of devotion which are Emblemes of gratitude. \r\nThe Eagle is dedicated to Jupiter, she is the Ensigne of Emperours,\r\n and an Embleme of Justice, and Clemency. \r\n\r\n\nAmongst fish, \r\nthe Dolphin, the fish called Anchia , the Sheath fish, \r\nby reason of his devoutness. \r\n\r\n\r\n\r\n\n\n\n\n\r\nCHAPTER XXXI.\r\n\nHow Provinces, and Kingdoms are Distributed to Planets.\n\n\n\n\nTOP\nUnder Jupiter with Sagittarius are Tuscana. Celtica, Spain\r\nand Happy Arabia. under him with Pisces are Lycia, Lydia, Cilicia, Phamphylia, \r\nPaphlagonia, Nasamonia and Libya. \r\n\r\n\r\n\n\n\n\n\r\nCHAPTER XLIV.\r\n\nThe Composition of Some Fumes Appropriated to the Planets.\n\n\n\n\n\nFor Jupiter take the seed of ash, lignum aloes, storax,\r\nthe gum benjamin, the lazule stone, the tops of the feathers of a peacock, \r\nand incorporate them with the blood of a stork, or a swallow and the brain of a hart...\r\n\nTo Jupiter, odoriferous fruits, such as nutmegs, cloves.\r\n\n\n\n\n\r\nCHAPTER XLVII.\r\n\nWhat Places are Suitable to Every Star\n\n\n\n\n\nUnto Jupiter are ascribed all privileged places,\r\nconsistories of noble men, tribunals, chairs, places for exercises, schools and\r\nall beautiful, and clean places, scattered or sprinkled with divers odors. \r\n\n\n\n\n\n\nTOP\n\n\n\n\nHOME\n\n\n\r\n\r\nPlease Contact me with any Questions or Comments.\r\n\n\r\nCopyright 2003 Christopher Warnock, All Rights Reserved.\r\n\r\n\r\n\r\n\n\n"


sentences = sent_tokenize(raw)

keywords_list = ['Amongst', 'amongst', 'Animals', 'XXXI', 'XLIV', 'XLVII']
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
jupiter = {}
for k, v in tagged.iteritems() :
    jupiter[k] = {}
    for sent in v :
        for word in sent :
            
            if word[0] == "Amongst" :
                jupiter[k][sent[sent.index(word) + 1][0]] = []
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                except ValueError, e : 
                    pass
            elif word[0] == "amongst" :
                jupiter[k][sent[sent.index(word) + 1][0]] = []
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                except ValueError, e:
                    pass
            elif word[0] == "Animals" :
                jupiter[k]["Animals"] = []
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
            elif word[0] == "jupiter" :
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                    sent.remove(sent[sent.index(word) - 1])
                except ValueError, e:
                    pass

for sent in tagged[11] :
    for word in sent :
        if "Fumes" in word[0] :
            jupiter[11]["Fumes"] = []
            tagged[11].remove(sent)
        elif "fumes" in word[0] :
            sent.remove(word)
for sent in tagged[10] :
    for word in sent :
        if "Provinces" in word[0] :
            jupiter[10]["Provinces"] = []
            tagged[10].remove(sent)
for sent in tagged[12] :
    for word in sent :
        if "Places" in word[0] :
            jupiter[12]["Places"] = []
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
            jupiter[k][jupiter[k].keys()[0]].append(v[idx[stt]:idx[stp]])
        except IndexError,e:
            jupiter[k][jupiter[k].keys()[0]].append(v[idx[stp-1]:])

f = open('~/astrologie/jupiter.json', 'w')
f.write(json.dumps(jupiter, indent=1))
f.close()

        
