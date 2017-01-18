# this file changes the QUESTIONNAIRE DATA to a different form in order the code to work
# also some simple statistics

import csv
import statistics

# opens the file
with open('/Users/jultsi/Google Drive/Gradu/csv_reponses_questionnaire.csv', 'r', encoding='latin-1') as quest:
    next(quest)     # should skip the first row i.e. the header
    questionnaire = csv.reader(quest, delimiter=";")

    ages = []

    # only the ages
    for row in questionnaire:
        ages.append(row[2])

    # changes from string to int
    new_ages = []
    for age in ages:
        if age != '':
            new_ages.append(int(age))

    count_old = 0
    count_young = 0

    # jatka tekemällä histogrammi

    for a in new_ages:
        if a > 40:                  # over 30: 71; over 40: 39
            count_old += 1
        elif a < 21:                # under 21: 197
            count_young += 1

    print(count_old)
    print(count_young)

    # print(new_ages)
    # print(len(new_ages))

    # statistics of the ages
    # print(statistics.median(new_ages))
    # print(statistics.mean(new_ages))

