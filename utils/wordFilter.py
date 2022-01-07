

def getFiveLetterWords(iFile, oFile):
    wordList5 = []
    wordList = []
    with open(iFile, "r") as f:
        for x in f:
            x = x.strip()
            wordList.append(x)
            if len(x) == 5:
                wordList5.append(x)

    print(len(wordList5))
    print(len(wordList))

    with open(oFile, "w") as w:
        w.write("\n".join(wordList5))
        w.write("\n")


getFiveLetterWords("words1K.txt", "easyList.txt")
getFiveLetterWords("words10k.txt", "mediumList.txt")
getFiveLetterWords("wordsFull.txt", "hardList.txt")
