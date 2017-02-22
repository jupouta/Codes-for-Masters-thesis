from src.preprosessointi import getAgeDivision
from src.extract_messages import messages


def main():
    m = messages(getAgeDivision())

    old = open("messOld.txt", "w")
    for o in m[0]:
        old.writelines(o + " ")
    old.close()

    young = open("messYoung.txt", "w")
    for y in m[1]:
        young.writelines(y + " ")
    young.close()


if __name__ == '__main__':
    main()