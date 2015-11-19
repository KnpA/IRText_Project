# coding: utf8
import re

ListeInverse={};

def LireFichier(name):
    res=""
    return res

content = u"àéèêâôùû Test de découpage du texte lu, avec même des virgules et des caractères spéciaux et tout maggle ! TKT; c'est trop cool..."

# Découpage du fichier lu en tableau
def Tokenize(content):
    content = content.lower()
    content = re.sub(r'[^a-zA-Z\xe0\xe9\xe8\xea\xe2\xf4\xf9\xfb\' ]',r'',content)    
    res = content.split()
    return res  

def StopList(tokens):
    res=[]
    return res

def TermFrequency(tokens):
    res={}
    return res

def InverseDocumentFrequency(keyword):
    res=0
    return res

def Ponderation(tokens):
    res={}
    return res
		