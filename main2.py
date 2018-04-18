import nltk
import re
import xml.etree.ElementTree as et

#croquis pour trouver les EN en rapport avec un meurtre

tree = et.parse('test.txt.xml')
root = tree.getroot()

persons = []    #liste de tous les noms et prénoms commençant par D
sentences_trouve = [] #liste des phrases ayant une EN commençant par D
sentences_approuved = [] #liste des phrases ayant un EN commençant par D et avec un mot de la liste word
person_killer = [] #liste des meurtriers
person_victime = [] #liste des victimes
sentence_killer = [] #liste comprenant un killer
sentence_victime = [] #liste comprenant une victime

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


print('---------------boucle sentences_trouve----------------') #liste des phrases ayant une EN commençant par D


for sentence in sentences_trouve :
    tokens = sentence.findall('tokens/token')
    for token in tokens :
        if token.find('lemma').text in word :
            sentences_approuved.append(sentence)


print('---------------boucle sentences_approuved---------------') #liste des phrases ayant un EN commençant par D et avec un mot de la liste word



for sentence in sentences_approuved :
    tokens = sentence.findall('tokens/token')
    person_trouve = False
    id = 0
    entite_current = sentence.find('tokens/token') #initialise au premier token
    for token in tokens :
        if person_trouve == True :
            for token_bis in tokens:
                if token_bis.find('lemma').text == 'be':  # cas victime be killed
                    for token_ter in tokens:
                        if int(token_ter.attrib['id']) + 1 == int(token_bis.attrib['id']):
                            if token_ter.find('lemma').text in word:
                                #entite_current est une victime
                                person_victime.append(entite_current)
                                sentence_victime.append(sentence)

                else:
                    if token_bis.find('lemma').text in word:  # cas murder kill
                        #entite_current est un meurtrier
                        person_killer.append(entite_current)
                        sentence_killer.append(sentence)
            person_trouve = False

        else :
            if token.find('NER').text == 'PERSON'  and token.find('word').text[0] == 'D':
                entite_current = token
                id = int(token.attrib['id'])
                person_trouve = True
            else:
                if token.find('lemma').text in word and person_trouve == False : #si le premier mot trouvé est dans la liste word
                    for token_bis in tokens :
                        if int(token_bis.attrib['id']) == int(token.attrib['id'])-1 and token_bis.find('lemma') == 'be' : #cas où << be killed by murder >>
                            for token_ter in tokens :
                                if int(token_ter.attrib['id']) > int(token.attrib['id']) and token_ter.find('NER').text =='PERSON' and token.find('word').text[0] == 'D': #mot après le verbe et une personne en D
                                    person_killer.append(token)
                                    sentence_killer.append(sentence)
                        else :
                            for token_bis in tokens : #cas où <<kill  victim >>
                                if int(token_ter.attrib['id']) > int(token.attrib['id']) and token_ter.find('NER').text =='PERSON' and token.find('word').text[0] == 'D': #mot après le verbe et une personne en D
                                    person_victime.append(token)
                                    sentence_victime.append(sentence)


print('-------------Liste des meurtriers--------')
for killer in person_killer :
    print(killer.find('word').text)

print('-------------Liste des victimes----------')
for victime in person_victime :
    print(victime.find('word').text)
