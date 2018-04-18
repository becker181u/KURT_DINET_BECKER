import nltk
import re
import xml.etree.ElementTree as et

#croquis pour trouver les EN en rapport avec un meurtre

tree = et.parse('test.txt.xml')
root = tree.getroot()

persons = []    #liste de tous les noms et prénoms commençant par D
sentences_trouve = [] #liste des phrases ayant une EN commençant par D
sentences_approuved = [] #liste des phrases ayant un EN commençant par D et avec un mot de la liste word

sentences=root.findall('sentences/sentence')

word = ['kill', 'murder', 'assassinate', 'drown', 'execute', 'get', 'poison', 'massacre', 'slaughter', 'slay'] #liste des mots pouvant apparenter à un meurtre

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
    tokens = sentence.findall('tokens/token')
    for token in tokens :
        if token.find('lemma').text in word :
            sentences_approuved.append(sentence)






print('Liste des sentence_approuved')
for sentence in sentences_approuved :
    tokens = sentence.findall('tokens/token')
    for token in tokens :
        print(token.find('word').text)







