from processing import tokenize


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
    for line in processedYoung:
        if line:
            fileYoung.write(line.lower() + "\n")
    fileYoung.close()

    fileAdult = open("adultProcessed.txt", "w")
    for line in processedAdult:
        if line:
            fileAdult.write(line.lower() + "\n")
    fileAdult.close()


if __name__ == '__main__':
    main()
