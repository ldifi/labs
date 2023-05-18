import re


def writeFile(x):
    listLeft = []
    listRight = []

    synList = open("synonyms.txt", "r+")
    for info in synList:
        k, v = info.split("-")
        k = k.strip()
        v = v.strip()
        listLeft.append(k)
        k = k.lower()
        if k == x:
            print(v)
            answer = input('Would you like add a new synonym? Y/N\n')
            answerLower = answer.lower()
            if answerLower == 'y':
                newSyn = str(input('Enter new synonym:\n'))
                v = v + '; ' + newSyn

        listRight.append(v)

    synDict = dict(zip(listLeft, listRight))
    synString = str(synDict)

    synRegEx = re.sub('(, )', r'\n', synString, flags=re.M)
    synRegEx1 = re.sub(r"[{'}]", r'', synRegEx, flags=re.M)
    synRegEx2 = re.sub(r"[:]", r' -', synRegEx1, flags=re.M)

    synList.seek(0)
    synList.write(synRegEx2)
    synList.truncate()
    synList.close()


def checkWord(word):
    listLeft = []

    synList = open("synonyms.txt", "r")
    for info in synList:
        k, v = info.split("-")
        k = k.strip()
        v = v.strip()
        k = k.lower()
        listLeft.append(k)

    if word not in listLeft:
        print('Word not found\nType a number to exit')
    else:
        writeFile(word)


def main():
    x = True

    while x == True:
        wordCheck = (input('Select a word:\n'))

        if not wordCheck.isdigit():
            word = wordCheck.lower()
            checkWord(word)
        else:
            x = False


main()