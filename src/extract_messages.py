# Divides the messages into two groups: young and old

import csv


def getMessages(ages):
    with open('/Users/jultsi/Google Drive/Gradu/Aineisto/0530529001478287869_0.csv', 'r') as les_sms:
        # skips the first row i.e. the header
        next(les_sms)
        sms = csv.reader(les_sms, delimiter=",")

        messOld = []
        messYoung = []

        # If id in old/young, add to 'messOld'/'messYoung'
        for row in sms:
            if int(row[2]) in ages['old']:
                messOld.append(row[4])
            elif int(row[2]) in ages['young']:
                messYoung.append(row[4])

        return messOld, messYoung