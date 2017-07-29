from src.preprosessointi import getAgeDivision
from src.extract_messages import messages


def main():
    m1, m2 = messages(getAgeDivision())

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