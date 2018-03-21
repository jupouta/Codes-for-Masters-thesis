from preprosessointi import getAgeDivision
from extract_messages import getMessages
from extract_messages import countAverAmount
import statistics


def main():
    m1, m2, oc, yc, ac = getMessages(getAgeDivision())
    
    statOld = countAverAmount(oc)
    
    statYoung = countAverAmount(yc)
    
    statAll = countAverAmount(ac)
    
    print("Average # of messages among the old: {}".format(statOld))
    print("Average # of messages among the young: {}".format(statYoung))
    print("Average # of messages: {}".format(statAll))
    
    print("Max of message length: {}".format(max(ac.values())))
    print("Min of message length: {}".format(min(ac.values())))
    print("Median of message length: {}".format(statistics.median(ac.values())))
    
    old = open("messOld.txt", "w")

    for row in m1:
        old.write(row + "\n")

    old.close()

    young = open("messYoung.txt", "w")

    for row in m2:
        young.write(row + "\n")

    young.close()


if __name__ == '__main__':
    main()