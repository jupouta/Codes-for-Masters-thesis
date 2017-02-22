# Divides the messages into two groups: young and old

import csv
from src.preprosessointi import getAgeDivision


def messages(ages):
    with open('/Users/jultsi/Google Drive/Gradu/Aineisto/0530529001478287869_0.csv', 'r') as message:
        # skips the first row i.e. the header
        next(message)
        sms = csv.reader(message, delimiter=",")

        messOld = []
        messYoung = []

        for row in sms:
            if int(row[2]) in ages['old']:
                messOld.append(row[4])
            elif int(row[2]) in ages['young']:
                messYoung.append(row[4])

        return messOld, messYoung


messages(getAgeDivision())