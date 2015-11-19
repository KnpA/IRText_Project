
import glob,random

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

def Tokenize(content):
    res=[]
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

        