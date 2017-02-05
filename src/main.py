from src.preprosessointi import getAgeDivision
from src.extract_messages import messages


def main():
    jee = messages(getAgeDivision())

    old = open("messOld.txt", "w")
    for o in jee[0]:
        old.writelines(o)
    old.close()

    young = open("messYoung.txt", "w")
    for y in jee[1]:
        young.writelines(y)
    young.close()


if __name__ == '__main__':
    main()