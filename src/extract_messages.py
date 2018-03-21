# Divides the messages into two groups: young and old

import csv


def getMessages(ages):
    with open('/Users/jultsi/Google Drive/Gradu/Aineisto/0530529001478287869_0.csv', 'r') as les_sms:
        # skips the first row i.e. the header
        next(les_sms)
        sms = csv.reader(les_sms, delimiter=",")

        messOld = []
        messYoung = []
        
        oldCount = {}
        youngCount = {}
        
        allCount = {}

        # If id in old/young, add to 'messOld'/'messYoung'
        for row in sms:
            
            if int(row[2]) in ages['old']:
                messOld.append(row[4])
                
                if row[2] not in oldCount:
                    oldCount[row[2]] = 1
                else:
                    oldCount[row[2]] += 1
            elif int(row[2]) in ages['young']:
                messYoung.append(row[4])
                
                if row[2] not in youngCount:
                    youngCount[row[2]] = 1
                else:
                    youngCount[row[2]] += 1
            try:
                allCount[row[2]] += 1
            except KeyError:
                allCount[row[2]] = 1
                

        return messOld, messYoung, oldCount, youngCount, allCount

def countAverAmount(dic):
    
    count = 0
    
    for val in dic.values():
        count += val

    return count / len(dic.keys())