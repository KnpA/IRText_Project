
import glob,random,re,math

def Main():
    #lecture de tous les fichiers et constitution des paquets 
    ListesInverse={}
    File2Author = {}
    File2Paquet = {}
    DocCount=0
    for filename in glob.iglob('./txt/*.txt'):
        author = filename.split("\\")[1]
        author = author.split(".txt")[0]
        author = author[:-1]
        File2Author[filename]=author
        paquet = random.randint(1,10)
        File2Paquet[filename]=paquet
        content=LireFichier(filename)
        tokens = Tokenize(content)
        tokens = StopList(tokens)
        ListesInverse = TermFrequency(tokens,ListesInverse,filename)
        DocCount+=1
    InverseDocumentFrequency(ListesInverse, DocCount)
    #print ListesInverse

def LireFichier(filename):
    res=""
    for line in open(filename):
        res = res + line
    return res

# Découpage du fichier lu en tableau
def Tokenize(content):
    #content = unicode(content, 'iso-8859-1')
    content = content.lower()
    content = re.sub('[\-]{2,}', "", content)
    content = re.sub(r'[^a-zA-Z\xe0\xe9\xe8\xea\xe2\xf4\xf9\xfb\-\' ]',r'',content)
    res = content.split()
    return res
    
def StopList(tokens):
    sentence = tokens
    remove_list=LireFichier('stop_word.html')
    #remove_list=unicode(remove_list, 'iso-8859-1')
    remove_list=remove_list.split()

    res=[]
    for word in sentence:
        #if word in remove_list :
            #print word+' retiré'
        if word not in remove_list :
            res.append(word)

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
    for word in ListesInverse:#normalization
        if filename in ListesInverse[word]:
            ListesInverse[word][filename] = ListesInverse[word][filename]/float(diffwordcount)
    print "Term frequency done for "+filename+" Diffwords : "+str(diffwordcount)
    return ListesInverse

def InverseDocumentFrequency(ListesInverse, DocCount):
    ListesInverse=ListesInverse
    for word in ListesInverse:
        idf = math.log(DocCount/float(len(ListesInverse[word])))
        #print word + " : " + str(idf) 
        for filename in ListesInverse[word]:
            ListesInverse[word][filename]=idf*ListesInverse[word][filename]
    print "Inverse document frequency done"
    return ListesInverse

def Ponderation(tokens):
    res={}
    return res

if __name__ == '__main__':
    Main()
