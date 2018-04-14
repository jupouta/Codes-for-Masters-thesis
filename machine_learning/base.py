
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
import re

# read the adult data into a table
def process_corpus():

    dataAdult = pd.read_table("~/Google Drive/Gradu/Koodi/processing/adultProcessed.txt",
                         encoding='utf-8', names=["message", "label"], sep="\\r\\t", engine='python')
    adultLabel = ["A"] * len(dataAdult)
    dataAdult["label"] = adultLabel
    # read the young data into a table
    
    dataYoung = pd.read_table("~/Google Drive/Gradu/Koodi/processing/youngProcessed.txt",
                              encoding='utf-8', names=["message", "label"], sep="\\r\\t", engine="python")
    youngLabel = ["Y"] * len(dataYoung)
    dataYoung["label"] = youngLabel
    # combine the two tables
    frames = [dataAdult, dataYoung]
    
    resultData = pd.concat(frames, ignore_index=True)
    
    # shuffle the data to have an equal amount of both of the groups
    resultData = shuffle(resultData)
    
    # labels to category
    resultData["label"] = resultData["label"].astype('category')
    resultData["message"] = resultData["message"].values.astype('U')
    
    
    # deletes stopwords
    def stopsOff(mess):
    
        mess = mess.split(" ")
        
        mess = [x for x in mess if x not in
                ["je", "de", "et", "tu", "pas", "est", "la", "le", "que", "on", "en", "mais"]]
    
        return " ".join(mess)

    
    
    # general ones
    def countingBinary(mess, word):
        
        mess = mess.split(" ")
        
        for m in mess:
            if word in m:
                return 1
        
        return 0
    
    def countingWords(mess, word):
        
        mess = mess.split(" ")
        
        count = 0
        
        for m in mess:
            if m == word:
                count += 1
        
        return count
    
    def countLists(mess, lists):
        
        mess = mess.split(" ")
        
        count = 0
        
        for m in mess:
            if m in lists:
                count += 1
        
        return count
    
    # caractères
    def countRepetition(mess):
        
        pattern1 = r"((\S)\2{2,})"
        
        if re.search(pattern1, mess):
            return 1
        else:
            return 0
    
    def countChar(mess):
        
        mess = mess.split(" ")
        
        totalLen = 0
        
        for m in mess:
            totalLen += len(m)
        
        if totalLen == 0:
            totalLen = 1
        
        return np.log(totalLen)
    
    def countWord(mess):
    
        mess = mess.split(" ")
        
        length = len(mess)
        
        if length == 0:
            length = 1
        
        return np.log(length)
    
    def countDiacr(mess):
        
        diacritics = ["à", "â", "æ", "ç", "é", "è", "ê", "ë", "ï", "î", "ô", "œ", "ù", "û", "ü", "ÿ"]
        
        count = 0
        
        for m in mess:
            if m in diacritics:
                count += 1
        
        return count
    
    def countingKs(mess):
        
        mess = mess.split(" ")
        
        count = 0
        
        for m in mess:
            if "k" in m:
                count += 1
        
        return count
       
    def countApostr(mess):
        
        count = 0
        
        patt = r"[a-z]+'\s[bcdfgjklmnpqrstvwxz][a-z]+"
        
        if re.search(patt, mess):
            count += 1
        
        return count
    
    # SMS
    def countSmileys(mess):
        
        mess = mess.split(" ")
        
        count = 0
        
        eyes, noses, mouths = r":;8BX=<\^", r"-~'", r")(/\|DdPp3\^"
        pattern1 = "([%s][%s]?[%s]+)" % tuple(map(re.escape, [eyes, noses, mouths])) 
        
        for m in mess:
            if re.match(pattern1, m): 
                count += 1
        
        return count
    
    def countNumbers(mess):
        
        mess = mess.split(" ")
        
        count = 0
        
        pattern1 = r"([a-z]\d|\d[a-z]|[a-z]\d[a-z])"
        
        for m in mess:
            if re.search(pattern1, m):
                count += 1
                
        return count
    
    
    
    def numbersOff(mess):
        
        mess_arr = mess.split(" ")
        
        
        # number tokens OR time tokens e.g. 12h or 12h30
        pattern1 = r"\b[0-9]+\b|\b[0-9]{1,2}h\b|\b[0-9]{1,2}h[0-9]{2}\b"
        mess_arr = [x for x in mess_arr if not re.match(pattern1, x)]
        
        
        return " ".join(mess_arr)

    
    
    cons = ["b", "c", "d", "f", "g", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    
    jeuneWords = ["école", "écoles", "cours", "jeune", "jeunes", "ado", "ados", "devoirs"]
    adulteWords = ["travail", "travaux", "famille", "familles", "maison", "maisons", "vieux", "vieille",
                       "vieil", "vieilles", "fils", "fille", "filles", "mère", "mères", "père", "pères",
                       "maman", "papa"]
    abrevs = ["pr", "tt", "ds", "qd", "bcp", "stp", "svp", "pcq", "ss", "rdv"]
    sms = ["coucou", "bisous", "lol", "mdr", "tvb", "tlm", "ptdr", "jtm", "asap", "jtd", "jtad"]
    
    jes = ["j'", "me", "m'", "moi"]
    
    
    
    resultData["smileycount"] = resultData.message.apply(countSmileys)
    resultData["jeunecount"] = resultData.message.apply(countLists, lists=jeuneWords)
    resultData["adultecount"] = resultData.message.apply(countLists, lists=adulteWords)
    resultData["abrevcount"] = resultData.message.apply(countLists, lists=abrevs)
    resultData["smscount"] = resultData.message.apply(countLists, lists=sms)
    resultData["numcount"] = resultData.message.apply(countNumbers)
   
    resultData["nouscount"] = resultData.message.apply(countingWords, word="nous")
    resultData["jecount"] = resultData.message.apply(countLists, lists=jes)
    resultData["tropcount"] = resultData.message.apply(countingWords, word="trop")
    
    resultData["apostrcount"] = resultData.message.apply(countApostr)

    originalRes = resultData.copy()
    resultData.message = resultData.message.apply(stopsOff)
    
    resultData["repetcount"] = resultData.message.apply(countRepetition)
    resultData["messlength"] = resultData.message.apply(countWord)
    resultData["charlength"] = resultData.message.apply(countChar)
    resultData["diacrcount"] = resultData.message.apply(countDiacr)
    resultData["kcount"] = resultData.message.apply(countingKs)
    resultData["conscount"] = resultData.message.apply(countLists, lists=cons)

    
    resultData.message = resultData.message.apply(numbersOff)
    
    return resultData, originalRes