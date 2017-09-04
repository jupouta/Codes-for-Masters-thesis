from processing import tokenize

listaa = ['Hey jvien de voir ton mp sur fb (waouh!) bref tjr partante pour ce soir? Bisous. <PRE_5>',
          'Haha! C\'est bon ca! Ben éclate toi bien! Du coup tu échapes à la fac pour faire de l\'animation. T\'as trouvé le bon plan. Lol. Félicitations! Bisous.',
          'Jsui en rdv. Je tapel juste après!<3',
          'Alors on se voit à 15h45. Ton lieu sera le mien <SUR_4>. Love.',
          'We r in Nooi. It\'s on the way to the tram. You can ask to the poeple front of the univ. Kiss',
          'Bon, de ce ke jai compris faut sinscrire aux grp. Dans lENT à scolarité.Moi jai mythologie le jeudi de 12h45à14h15 ya 1TD jusko 15.jché pa +. Biz']


def process_messages(target):
    result = []
    for message in target:
        # take a message, create an object, and start the tokenizing process
        tokenized = tokenize.Tokenized(message).process()
        result.append(tokenized)
    return result


def main():

    adult = open("/Users/jultsi/Google Drive/Gradu/Koodi/src/messOld.txt", "r")
    adultContents = adult.readlines()
    adult.close()

    processedAdult = process_messages(adultContents)

    young = open("/Users/jultsi/Google Drive/Gradu/Koodi/src/messYoung.txt", "r")
    youngContents = young.readlines()
    young.close()

    processedYoung = process_messages(youngContents)

    fileYoung = open("youngProcessed.txt", "w")
    fileYoung.writelines(processedYoung)
    fileYoung.close()

    fileAdult = open("adultProcessed.txt", "w")
    fileAdult.writelines(processedAdult)
    fileAdult.close()


if __name__ == '__main__':
    main()
