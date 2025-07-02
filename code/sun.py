# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 15:13:10 2017

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

url = 'http://renaissanceastrology.com/agrippasun.html'
html = urllib.urlopen(url)
raw = BeautifulSoup(html).get_text()
raw= u"\n\n\n\n\nCornelius Agrippa on the Things Ruled by the Sun\n\n\n\n\n\n\n\n\nSERVICES\n\n\nPAYMENT\n\n\nCOURSES\n\n\nBOOKS\n\n\nCONTACT\n\n\nSEARCH\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nChristopher Warnock, Esq.\n\n\n\n\n Agrippa on the Things Ruled by the Sun\r\n\r\n\n\n\n\n\nHOME\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCornelius Agrippa on Saturn \n\n\n\n\nCornelius Agrippa on Jupiter \n\n\n\n\nCornelius Agrippa on Mars \n\n\n\n\nCornelius Agrippa on the Sun \n\n\n\n\nCornelius Agrippa on Venus \n\n\n\n\nCornelius Agrippa on Mercury \n\n\n\n\nCornelius Agrippa on the Moon \n\n\n\n\n\n\n\n\nLilly on Saturn \n\n\n\n\nLilly on  Jupiter \n\n\n\n\nLilly on  Mars \n\n\n\n\nLilly on the Sun \n\n\n\n\nLilly on  Venus \n\n\n\n\nLilly on  Mercury \n\n\n\n\nLilly on the Moon \n\n\n  Web Site Search\n\n\n\n\n\n\n\n\nWhat things are Solar or\r\nunder the power of the Sun\r\n\n\n\r\nfrom Cornelius Agrippa's Three Books of Occult Philosophy\n\n\n\nElements & Tastes\nMetals & Stones\nPlants & Trees\nFoods\nAnimals\nBirds\nFish\nRegions & Countries\nIncense\nPlaces\n\n\n\n\n\n\n\n\nBOOK ONE\n\n\n\r\nCHAPTER XXIII.\r\n\n What things are under the power of the Sun, and are called Solary.\n\n\n\n\n\nThings under the power of the Sun are.\r\nAmongst Elements, the lucid flame. \r\nin the humours, the purer blood, and spirit of life. amongst tasts, that which is \r\nquick, mixed with sweetness.\r\n\r\n\nAmongst  Metals, \r\nGold by reason of its splendor, and its receiving that from the Sun which \r\nmakes it cordiall. And amongst stones, they which resemble the rayes of the \r\nSun by their golden sparklings, as doth the glittering stone Aetites which\r\n hath power against the Falling-sickness, and poisons. \r\n\r\n\nSo also the stone, \r\nwhich is called the eye of the Sun, being of a figure like to the Apple of\r\n the eye, from the middle whereof shines forth a ray, it comforts the brain,\r\n and strengthens the sight. So the Carbuncle which shines by night, hath a \r\nvertue against all aiery, and vaporous poison. \r\n\nSo the Chrysolite stone is\r\n of a light green colour, in which, when it is held against the Sun, there\r\n shines forth a golden Star. and this comforts those parts that serve for \r\nbreathing, & helps those that be Asthmaticall, and if it be bored through,\r\n and the hole filled with the Mane of an Asse, and bound to the left arme,\r\n it drives away idle imaginations, and melancholy fears, and puts away \r\nfoolishness.\r\n\nSo the stone called Iris, which is like Crystall in colour,\r\n being often found with six corners, when under some roof part of it is \r\nheld against the rayes of the Sun, and the other part is held in the shadow,\r\n it gathers the rayes of the Sun into it self, which, whilest it sends them \r\nforth, by way of reflection, makes a Rain-bow appear on the opposite wall.\r\n\nAlso the Stone Heliotropion green like the Jasper, \r\nor Emrald, beset with red specks, makes a man constant, renowned, and famous, \r\nalso it conduceth to long life. And the vertue of it indeed is most wonderfull upon \r\nthe beams of the Sun, which it is said to turn into blood, to appear of the \r\ncolour of blood, as if the Sun were eclypsed, viz. When it is joyned \r\nto the juice of a Hearb of the same name, and be put into a vessell of\r\n Water. \r\n\nThere is also another\r\n vertue of it more wonderfull, and that is upon \r\nthe eyes of men, whose sight it doth so dim, and dazel, that \r\nit doth not suffer him that carries it to see it, & this it doth not \r\ndo without the help of the Hearb of the same name, \r\nwhich also is called Heliotropium,  \r\nfollowing the Sun. These vertues doth Albertus Magnus, \r\nand William of Paris confirm in their writings. \r\n\r\n\nThe Hyacinth also \r\nhath a vertue from the Sun against poisons, \r\nand pestiferous vapours. it makes him that carries it to be safe,\r\n and acceptable. it conduceth also to riches, and wit, it strengthens \r\nthe heart. being held in the mouth, it doth wonderfully cheer up the mind. \r\n\nAlso there is \r\nthe stone Pyrophylus, of a red mixture, which Albertus Magnus \r\nsaith Aesculapius, makes mention of in one of his Epistles unto Octavius Augustus,\r\n saying, that there is a certain poison so wonderfull cold, which preserves the \r\nheart of man being taken out from burning, so that if for any time it be put \r\ninto the Fire, it is turned into a stone, and this is that stone which is called\r\n Pyrophylus, from the fire. It hath a wonderfull vertue against poison, and it \r\nmakes him that carries it, to be renowned and dreadfull to his enemies.\r\n \nBut above all, that stone is most Solary, \r\nwhich Apollonius is reported \r\nto have found, and which is called Pantaura, which draws other stones to \r\nit, as the Loadstone doth Iron, most powerfull against all poisons. it is \r\ncalled by some Pantherus, because it is spotted like the beast called the\r\n Panther. It is therefore also called Pantochras, because it contains all \r\ncolours. Aaron cals it Evanthum. There are also other Solary stones, as the \r\nTopazius, Chrysopassus, the Rubine, and Balagius. So also is Auripigmentum, \r\nand things of a golden colour, and very lucid. \r\n\r\n\r\n\nAmongst\r\n  Plants and Trees, those are Solary, which turn towards the \r\nSun, as the Marygold, and those which fold in their leaves when the \r\nSun is neer upon setting, but when it riseth unfold their leaves by\r\n little and little. The Lote-tree also is Solary, as is manifest \r\nby the figure of the fruit & leaves. \r\n\nSo also Piony, Sallendine, Balme, \r\nGinger, Gentian, Dittany, & Vervin, which is of use in prophecying, and expiations, \r\nas also driving away evill spirits. The Bay-tree also is consecrated to Phoebus, \r\nso is the Cedar, the Palm tree, the ash, the Ivie, and Vine, and whatsoever repell \r\npoisons, and lightnings, and those things which never fear the extremities \r\nof the Winter. \r\n\nSolary also are \r\nMint, Mastick, Zedoary, Saffron, Balsome, Amber, Musk, Yellow honey,\r\nLignum aloes, Cloves, Cinnamon, Calamus, Aromaticus, Pepper, Frankincense, \r\nsweet Marjoram, also Libanotis, which Orpheus cals the sweet perfume of the Sun.\r\n\r\n\r\n\nAmongst\r\n Animals, those are Solary which are magnanimous, couragious, \r\nambitious of victory, and renown. as the Lyon, King of beasts, \r\nthe Crocodile, the spotted Wolf, the Ram, the Boar, the Bull, \r\nKing of the herd, which was by the Egyptians at Heliopolis dedicated to the Sun,\r\n which they called Verites. and an Ox was consecrated to Apis in Memphi, and \r\nin Herminthus a Bull by the name of Pathis. \r\n\nThe Wolf also was consecrated to \r\nApollo, and Latona. Also the beast called Baboon is Solary, which twelve times \r\nin a day, viz. every hour barks, and in time of Equinoctium pisseth\r\n twelve times every hour. the same also it doth in the night, \r\nwhence the Egyptians did Engrave him upon their Fountains.\r\n\r\n\nAlso amongst birds, \r\n these are Solary, The Phoenix, being but one of that kind,\r\n and the Eagle, the Queen of birds, also the Vulture, the Swan, and those \r\nwhich sing at the rising Sun, and as it were call upon it to rise, as\r\n the Cock, Crow, also the Hawk, which because it in the Divinity \r\nof the Egyptians is an emblem of the spirit, and light, is by Porphyrius\r\n reckoned amongst the Solary birds. \r\n\nMoreover, all such things as have \r\nsome resemblance of the works of the Sun, as Worms shining in the night,\r\n and the Betle, which is a creature that lies under Cow-dung, \r\nalso according to Appious interpretation, such whose eyes are\r\n changed according to the course of the Sun, are accounted Solary, \r\nand those things which come of them.\r\n\r\n\nAnd amongst fish, \r\n\r\nthe Sea Calf is chiefly Solary, who doth resist lightning, \r\nalso shell fish, and the fish called Pulmo, both which shine\r\n in the night, and the fish called Stella\r\n for his parching heat, and the fish called Strombi, \r\nthat follow their King, and Margari, which also have a King, and \r\nbeing dryed, are hardened into a stone of a golden colour. \r\n\r\n\r\n\r\n\n\n\n\n\r\nCHAPTER XXXI.\r\n\nHow Provinces, and Kingdoms are Distributed to Planets.\n\n\n\n\nTOP\nThe Sun with Leo governs Italy, Apulia, Sicilia, \r\nPhencia, Chaldea and the Orchenians. \r\n\r\n\r\n\n\n\n\n\r\nCHAPTER XLIV.\r\n\nThe Composition of Some Fumes Appropriated to the Planets.\n\n\n\n\n\nWe make a suffumigation for the Sun in this manner,\r\nviz. of saffron, ambergris, musk, lignum-aloes, lignum-balsam, the fruit of the \r\nlaurel, cloves, myrrh, and frankincense, all of them being bruised, and mixed in \r\nsuch a proportion as may make a sweet odor, must be incorporated with the brain \r\nof an eagle, or the blood of a white cock, after the manner of pills or trochists.\r\n\r\nTo the Sun, all gums, frankincense, mastic, benjamin,\r\nstorax, laudanum, ambergris and musk.\r\n\n\n\n\n\r\nCHAPTER XLVII.\r\n\nWhat Places are Suitable to Every Star\n\n\n\n\n\nTo the Sun, light places, the serene air, kings' palaces,\r\nand princes' courts, pulpits, theaters, thrones and all kingly and magnificent places. \r\n\n\n\n\n\n\nTOP\n\n\n\n\nHOME\n\n\n\r\n\r\nPlease Contact me with any Questions or Comments.\r\n\n\r\nCopyright 2003 Christopher Warnock, All Rights Reserved.\r\n\r\n\r\n\r\n\n\n"

sentences = sent_tokenize(raw)

keywords_list = ['Amongst', 'amongst', 'humours', 'XXXI', 'XLIV', 'XLVII']
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

sun = {}
for k, v in tagged.iteritems() :
    sun[k] = {}
    for sent in v :
        for word in sent :
            
            if word[0] == "Amongst" :
                sun[k][sent[sent.index(word) + 1][0]] = []
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                except ValueError, e : 
                    pass
            elif word[0] == "amongst" :
                sun[k][sent[sent.index(word) + 1][0]] = []
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                except ValueError, e:
                    pass
                except ValueError, e:
                    pass
            elif "CHAPTER" in word[0] :
                v.remove(sent)
            elif word[0] == "TOP" :
                try :
                    sent.remove(word)
                except ValueError, e:
                    pass
            elif word[0] == "sun" :
                try :
                    sent.remove(word)
                    sent.remove(sent[sent.index(word) + 1])
                    sent.remove(sent[sent.index(word) - 1])
                except ValueError, e:
                    pass

for sent in tagged[10] :
    for word in sent :
        if "Fumes" in word[0] :
            sun[10]["Fumes"] = []
            tagged[10].remove(sent)
        elif "fumes" in word[0] :
            sent.remove(word)
for sent in tagged[9] :
    for word in sent :
        if "Provinces" in word[0] :
            sun[9]["Provinces"] = []
            tagged[9].remove(sent)
for sent in tagged[11] :
    for word in sent :
        if "Places" in word[0] :
            sun[11]["Places"] = []
for sent in tagged[1] :
    for word in sent :
        if "humours" in word[0] :
            sun[1]["humours"] = []
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
            sun[k][sun[k].keys()[0]].append(v[idx[stt]:idx[stp]])
        except IndexError,e:
            sun[k][sun[k].keys()[0]].append(v[idx[stp-1]:])


f = open('~/astrologie/sun.json', 'w')
f.write(json.dumps(sun, indent=1))
f.close()


