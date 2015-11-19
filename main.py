
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
        File2Paquet[filename]=random.randint(1,10)
        content=LireFichier(filename)
        tokens = Tokenize(content)
        ListesInverse = TermFrequency(tokens,ListesInverse,filename)
    print ListesInverse

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

def TermFrequency(tokens,ListesInverse,filename):
    ListesInverse=ListesInverse    
    diffwordcount=0
    for word in tokens:
            if not word in ListesInverse:
                ListesInverse[word] = {}
            if not filename in ListesInverse[word]:
                diffwordcount+=1
                ListesInverse[word][filename] = 0
            ListesInverse[word][filename]+=1
    for word in ListesInverse:
        if filename in ListesInverse[word]:
            ListesInverse[word][filename] = ListesInverse[word][filename]/float(diffwordcount)
    print "Term frequency done for "+filename+" Diffwords : "+str(diffwordcount)
    return ListesInverse

def InverseDocumentFrequency(keyword):
    res=0
    return res

def Ponderation(tokens):
    res={}
    return res



if __name__ == '__main__':
    Main()

