# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 15:46:59 2017

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

url = 'http://renaissanceastrology.com/agrippavenus.html'
html = urllib.urlopen(url)
raw = BeautifulSoup(html).get_text()
raw= u"\n\n\n\n\nCornelius Agrippa on the Things Ruled by the Planet Venus\n\n\n\n\n\n\n\n\nSERVICES\n\n\nPAYMENT\n\n\nCOURSES\n\n\nBOOKS\n\n\nCONTACT\n\n\nSEARCH\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nChristopher Warnock, Esq.\n\n\n\n\n Agrippa on the Things Ruled by Venus\r\n\r\n\n\n\n\n\nHOME\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCornelius Agrippa on Saturn \n\n\n\n\nCornelius Agrippa on Jupiter \n\n\n\n\nCornelius Agrippa on Mars \n\n\n\n\nCornelius Agrippa on the Sun \n\n\n\n\nCornelius Agrippa on Venus \n\n\n\n\nCornelius Agrippa on Mercury \n\n\n\n\nCornelius Agrippa on the Moon \n\n\n\n\n\n\n\n\nLilly on Saturn \n\n\n\n\nLilly on  Jupiter \n\n\n\n\nLilly on  Mars \n\n\n\n\nLilly on the Sun \n\n\n\n\nLilly on  Venus \n\n\n\n\nLilly on  Mercury \n\n\n\n\nLilly on the Moon \n\n\n  Web Site Search\n\n\n\n\n\n\n\n\nWhat things are Venereal or\r\nunder the power of Venus\r\n\n\n\r\nfrom Cornelius Agrippa's Three Books of Occult Philosophy\n\n\n\nElements & Tastes\nMetals & Stones\nPlants & Trees\nFoods\nAnimals\nBirds\nFish\nRegions & Countries\nIncense\nPlaces\n\n\n\n\n\n\n\n\nBOOK ONE\n\n\n\r\nCHAPTER XXVIII.\r\n\n What things are under the power of Venus, and are called Venereall.\n\n\n\n\n\nThings  are under Venus,\r\namongst Elements, Aire, and Water. amongst humours,\r\nFlegm, with Blood, Spirit, and Seed. amongst tasts, those which are sweet, \r\nunctuous, and delectable.\r\n\r\n\nAmongst  Metals, \r\n\r\nSilver, and Brass, both yellow, and red. amongst Stones, the Berill, \r\nChrysolite, Emrald, Saphir, green Jasper, Corneola, the stone Aetites, the \r\nLazull stone, Corall, and all of a fair, various, white, and green Colour.\r\n\r\n\nAmongst\r\n  Plants and Trees, the Vervin, Violet, Maidenhaire, \r\nValerian, which by the Arabian is called Phu. also Thyme, the \r\ngum Ladanum, Amber-grise, Musk, Sanders, Coriander, and all sweet perfumes, \r\nand delightfull, \r\n\nAnd sweet fruits,  \r\nas sweet Pears, Figs, Pomegranats, \r\nwhich the Poets say was, in Cyprus, first sown by Venus. \r\nAlso the Rose of Lucifer was dedicated to her, also the Myrtle tree of Hesperus. \r\n\r\n\r\n\nMoreover all luxurious, delicious\r\n Animals, and of \r\na strong love, as Dogs, Conies, stinking Sheep, and \r\nGoats, both female, and male, which generates sooner then\r\n any other Animall, for they say that he couples after the \r\nseventh day of his being brought forth. also the Bull for \r\nhis disdain, and the Calf for his wantonness.\r\n\r\n\r\n\nAmongst birds, \r\nthe Swan, the Wagtail, the Swallow, the Pellican, the Burgander, \r\nwhich are very loving to their yong. Also the Crow, and Pigeon, \r\nwhich is dedicated to Venus, and the turtle dove, one whereof was Commanded \r\nto be offered at the purification, after bringing forth. \r\nThe Sparrow also was dedicated to Venus, which was Commanded\r\n in the Law to be used in the purification, after the Leprosie, a martiall disease, \r\nthen which nothing was of more force to resist it. Also the Egyptians \r\ncalled the Eagle Venus, because she is prone to Venery, \r\nfor after she hath been trod thirteen times a day, if \r\nthe Male call her, she runs to him again.\r\n\r\n\nAmongst fishes, \r\n\r\nthese are Venereall, the lustfull Pilchards, the letcherous Gilthead, \r\nthe Whiting for her love to her yong, Crab fighting for his Mate, and \r\nTithymallus for its fragrance, and sweet smell. \r\n\r\n\r\n\r\n\r\n\n\n\n\n\r\nCHAPTER XXXI.\r\n\nHow Provinces, and Kingdoms are Distributed to Planets.\n\n\n\n\nTOP\nVenus with Taurus governs the Isles Cyclades, the seas of\r\nLittle Asia, Cyprus, Parthia, Media, Persia, but with Libra she commands the \r\npeoples of the island Bractia, of Caspia, of Seres, of Thebais, of Oasis, and \r\nof Troglodys. \r\n\r\n\r\n\n\n\n\n\r\nCHAPTER XLIV.\r\n\nThe Composition of Some Fumes Appropriated to the Planets.\n\n\n\n\n\nFor Venus take musk, ambergris, lignum-aloes, red roses,\r\nand red coral and make them up with the brain of sparrows and the blood of pigeons.\r\n\nTo Venus flowers such as roses, violets, saffron and \r\nsuch like.\r\n\n\n\n\n\r\nCHAPTER XLVII.\r\n\nWhat Places are Suitable to Every Star\n\n\n\n\n\nTo Venus, pleasant fountains, green meadows, flourishing\r\ngardens, garnished beds, stews (and according to Orpheus) the sea, the seashore,\r\nbaths, dancing places and all places belonging to women. \r\n\n\n\n\n\n\nTOP\n\n\n\n\nHOME\n\n\n\r\n\r\nPlease Contact me with any Questions or Comments.\r\n\n\r\nCopyright 2003 Christopher Warnock, All Rights Reserved.\r\n\r\n\r\n\r\n\n\n"
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
del tagged[0]
tagged[12] = tagged[12][:-2]

venus = {}
for k, v in tagged.iteritems() :
    venus[k] = {}
    for sent in v :
        for word in sent :
            
            if word[0] == "Amongst" :
                venus[k][sent[sent.index(word) + 1][0]] = []
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                except ValueError, e : 
                    pass
            elif word[0] == "amongst" :
                venus[k][sent[sent.index(word) + 1][0]] = []
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                except ValueError, e:
                    pass
            elif word[0] == "Animals" :
                venus[k]["Animals"] = []
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
            elif word[0] == "venus" :
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                    sent.remove(sent[sent.index(word) - 1])
                except ValueError, e:
                    pass

for sent in tagged[11] :
    for word in sent :
        if "Fumes" in word[0] :
            venus[11]["Fumes"] = []
            tagged[11].remove(sent)
        elif "fumes" in word[0] :
            sent.remove(word)
for sent in tagged[10] :
    for word in sent :
        if "Provinces" in word[0] :
            venus[10]["Provinces"] = []
            tagged[10].remove(sent)
for sent in tagged[12] :
    for word in sent :
        if "Places" in word[0] :
            venus[12]["Places"] = []

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
            venus[k][venus[k].keys()[0]].append(v[idx[stt]:idx[stp]])
        except IndexError,e:
            venus[k][venus[k].keys()[0]].append(v[idx[stp-1]:])


f = open('~/astrologie/venus.json', 'w')
f.write(json.dumps(venus, indent=1))
f.close()


