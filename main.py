
import glob,random,re,math



def Main():
    #lecture de tous les fichiers et constitution des paquets 
    ListesInverse={}
    File2Author = {}
    NbPaquet = 10
    File2Paquet = {}
    Paquet2File = {}
    File2Norme = {}
    Word2IDF = {}
    DocCount=0
    for filename in glob.iglob('./txt/*.txt'):
        author = filename.split("\\")[1]
        author = author.split(".txt")[0]
        author = author[:-1]
        File2Author[filename]=author
        paquet = random.randint(1,NbPaquet)
        File2Paquet[filename]=paquet
        if not paquet in Paquet2File:
            Paquet2File[paquet] = []
        Paquet2File[paquet].append(filename)
        content=LireFichier(filename)
        tokens = Tokenize(content)
        #tokens = StopList(tokens)
        ListesInverse = TermFrequency(tokens,ListesInverse,filename)
        DocCount+=1
    Word2IDF = InverseDocumentFrequency(ListesInverse, DocCount)
    File2Norme = Norme(ListesInverse,Word2IDF)
    #validation croisee par calcul du cosinus
    for i in range(NbPaquet):
        OK, pasOK = 0, 0       
        t_moy = []
        for filename in Paquet2File[i+1]:
            Scores = {}            
            content=LireFichier(filename)
            tokens = Tokenize(content)
            #tokens = StopList(tokens)
            words = {}
            for word in tokens:
                words[word]=1
            #print("Removed doblons")            
            for word in words:
                for comp_doc in File2Author:
                    if comp_doc not in Paquet2File[i+1]:                            
                        if comp_doc in ListesInverse[word]:
                            if comp_doc not in Scores:
                                Scores[comp_doc]=0
                            #calcul du cosinus
                            cos = ((ListesInverse[word][filename] * Word2IDF[word] ) * (ListesInverse[word][comp_doc] * Word2IDF[word]) ) 
                            cos = cos / float( math.sqrt(File2Norme[comp_doc]))
                            Scores[comp_doc]+= cos
                                
            Winner = None
            for doc in Scores:
                if not Winner:
                    Winner = doc
                if Scores[doc] > Scores[Winner]:
                    Winner = doc
            if File2Author[Winner] == File2Author[filename]:
                OK += 1
                print "OK, wanted " + File2Author[Winner]
            else:
                pasOK += 1
                print "KO, wanted " + File2Author[filename] + " , got " + File2Author[Winner]
            prec = OK / float(OK + pasOK)
            
            print "Just tested " + filename
        t_moy.append(prec)
        print "Just tested paquet" + str(i+1) + " with prec = "+ str(prec)
    pmoy= sum(t_moy)/float(len(t_moy))
    print "Average precision for all paquets :" + str(pmoy)

def LireFichier(filename):
    res=""
    for line in open(filename):
        res = res + line
    return res

# Decoupage du fichier lu en tableau
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
            #print word+' retire'
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
    Word2IDF = {}
    for word in ListesInverse:
        Word2IDF[word] = math.log(DocCount/float(len(ListesInverse[word])))
    print "Inverse document frequency done"
    return Word2IDF

def Norme(ListesInverse,Word2IDF):
    File2Norme={}
    for word in ListesInverse:
        for filename in ListesInverse[word]:
            if not filename in File2Norme:
                File2Norme[filename] = 0
            File2Norme[filename] += (ListesInverse[word][filename] * Word2IDF[word]) ** 2
    #print File2Norme
    return File2Norme

if __name__ == '__main__':
    Main()
