
# coding: utf8
import glob,random,re

def Main():
    #lecture de tous les fichiers et constitution des paquets 
    ListesInverse={}
    File2Author = {}
    File2Paquet = {}
    for filename in glob.iglob('./txt/*.txt'):
        author = filename.split("\\")[1]
        author = author.split(".txt")[0]
        author = author[:-1]
        File2Author[filename]=author
        File2Paquet[filename]=random.randint(1,11)
        content=LireFichier(filename)
        tokens = Tokenize(content)
        
    print File2Paquet

def LireFichier(filename):
    res=""
    for line in open(filename):
        res = res + line
    return res

content = u"àéèêâôùû a-t-il Test de découpage du texte lu, avec même des virgules et des caractères spéciaux et tout maggle ! TKT; c'est trop cool..."

# Découpage du fichier lu en tableau
def Tokenize(content):
    content = content.lower()
    content = re.sub('[\-{2,}]', "", content)
    content = re.sub(r'[^a-zA-Z\xe0\xe9\xe8\xea\xe2\xf4\xf9\xfb\-\' ]',r'',content)    
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



if __name__ == '__main__':
    Main()

