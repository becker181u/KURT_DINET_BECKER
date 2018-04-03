import nltk
from xml.etree import ElementTree

tree= ElementTree.parse('./source.txt.xml')
root= tree.getroot()
exemples=root.findall('exemple');
for each in exemples :
    attribut=exemples.attrib['att1']



