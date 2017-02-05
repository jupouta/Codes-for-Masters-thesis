
import csv
from src.preprosessointi import getAgeDivision


def messages(ages):
    with open('/Users/jultsi/Google Drive/Gradu/Aineisto/0530529001478287869_0.csv', 'r') as messaage:
        # skips the first row i.e. the header
        next(messaage)
        sms = csv.reader(messaage, delimiter=",")

        messOld = []
        messYoung = []

        for row in sms:
            if int(row[2]) in ages['old']:
                messOld.append(row[4])
            elif int(row[2]) in ages['young']:
                print(row[4], row[2])
                messYoung.append(row[4])

        return messOld, messYoung


messages(getAgeDivision())