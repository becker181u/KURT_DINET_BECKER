import nltk
import re
import xml.etree.ElementTree as et

#liste les EN commençant par D

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
        print(token.find('word').text)
        person = token.find('NER')
        if person.text == 'PERSON' :
            name = token.find('word').text
            print(name)
            trouve.append(token)

    for entite in trouve :  #boucle pour rassembler les noms et prénoms
        EN = entite
        id_entite1 = int(EN.attrib['id'])
        trouve.remove(entite)#pour etre sur la deuxieme entite on supprime la premiere
        for entite2 in trouve :
            id_entite2 = int(entite2.attrib['id'])
            if id_entite1+1 == id_entite2 :
                if EN.find('word').text[0] == 'D' or entite2.find('word').text[0] == 'D' :
                    persons.append(EN.find('word').text + ' ' + entite2.find('word').text)









print('Liste de personnes commençant par D')
for person in persons :
    print(person)







