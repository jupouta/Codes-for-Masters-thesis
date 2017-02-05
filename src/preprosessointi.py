# this file changes the QUESTIONNAIRE DATA to a different form in order the code to work
# it also combines the ids with the ages

import csv


def getAgeDivision():
    with open('/Users/jultsi/Google Drive/Gradu/Aineisto/reponses_questionnaire.csv', 'r', encoding='latin-1') as quest:
        # skips the first row i.e. the header
        next(quest)
        questionnaire = csv.reader(quest, delimiter=";")

        ages = {}

        # ages with their corresponding ids
        for row in questionnaire:
            if row[3] not in ages:
                ages[int(row[3])] = row[2]

        filteredAges = {}

        # changes from string to int
        # deletes ids with no age given
        for id in ages.keys():
            data = ages[id]
            if data:
                filteredAges[id] = int(data)

        ids = {'old': [], 'young': []}

        # only the old and young ids
        for id in filteredAges:
            if (filteredAges[id] <= 55) and (filteredAges[id] >= 30):
                ids['old'] += [id]
            elif (filteredAges[id] <= 21) and (filteredAges[id] >= 10):
                ids['young'] += [id]

        return ids