import nltk
import re
import xml.etree.ElementTree as et

tree = et.parse('test.txt.xml')
root = tree.getroot()

persons = []    #liste de tous les noms et prénoms commençant par D
sentences_trouve = [] #liste des phrases ayant une EN commençant par D

sentences=root.findall('sentences/sentence')

print("boucle sentence")
for sentence in sentences : #boucle sur toutes les phrases
    tokens=sentence.findall('tokens/token')
    trouve = [] #liste de toutes les entités nommées étant une personne
    for token in tokens :   #boucle sur les tokens des phrases
        if token.find('NER').text == 'PERSON' :
            if token.find('word').text[0] == 'D' :
                persons.append(token.find('word').text)
                sentences_trouve.append(sentence)

for sentence in sentences_trouve :
    tokens = sentences_trouve.findall('tokens/token')
    









print('Liste de personnes commençant par D')
for person in persons :
    print(person)







