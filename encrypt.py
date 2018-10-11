# Making a slight change
import os
import datetime
fileLoc = 'federalistPapers.txt'
fileLoc2 = 'KJV.txt'
# dt =  datetime.datetime.now()
# DT=str(dt)
userInput = []
name = None
letters = []
key = []
keyD = []
toEncode = []
encoded = []
maxLet = []
# for future use
percentages = []
crackPercentages = []
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def main():
    os.system('clear')
    printLogo()
    print('\nHere is your current directory:\n')
    os.system('ls')
    name = input('\nPlease enter the "fileName.txt" (must be in same directory as test.py)\n')
    try:
        getFile(name)
    except:
        # print('Please enter a valid file name ending in .txt from your current directory')
        # print('Press 0 to QUIT')
        main()


def getFile(n):
    userInput.clear()
    with open(n) as fileObj:
        for line in fileObj:
            for ch in line:
                userInput.append(ch)

    letters.clear()
    percentages.clear()
    for x in userInput:
        if x.isalpha():
            letters.append(x.upper())

    theLen = len(letters)
    print('Total # of characters: ', theLen)

    for x in alphabet:
        letSum = 0
        for y in letters:
            if y == x:
                letSum += 1
        percentages.append(letSum/theLen)
    print(percentages)
    getDecision()


def getDecision():
    os.system('clear')
    # printLogo()
    decision = int(input('File has been loaded.\nEnter 0 to encrypt:\nEnter 1 to decrypt (known key):\nEnter 2 to try cracking an encrypted file:'))
    if decision == 0:
        encrypt()
        again()
    elif decision == 1:
        keyPass = input('\nEnter key used to encrypt this file:\n')
        keyPass=keyPass.upper()
        decrypt(keyPass)
        again()
    elif decision ==2:
        getKeyLen()
        again()
    else:
        print("Please enter 0 to encrypt or 1 to decrypt.")
        getDecision()

def again():
    # os.system('clear')
    # printLogo()
    toDo = int(input('Enter 0 to quit or 1 to load and encode/decode another file:'))
    if toDo == 0:
        os.system('clear')
        print('Goodbye!')
        return(0)
    elif toDo == 1:
        main()
    else:
        print('Please enter 0 to quit or 1 to load another file')
        again()




def encrypt():
    k = input('\nEnter desired encryption key (max length of 7 if you want to crack it later):\n')
    k=k.upper()
    print('The key is: ',k)
    kLen = len(k)
    kCount = 0
    dt =  datetime.datetime.now()
    DT=str(dt)
    fileName = ("encrypted_%s.txt"%DT)
    f = open(fileName, "x")
    for x in k:
        key.append(x)

    theChar=None
    theChar1=None
    for x in letters:
        if kCount<kLen:
            theChar = (((ord(x)-ord('A'))+(ord(k[kCount])-ord('A')))%26)
            f.write(chr((theChar+ord('A'))))
            kCount+=1
        elif kCount==kLen:
            kCount=0
            theChar1 = (((ord(x)-ord('A'))+(ord(k[kCount])-ord('A')))%26)
            f.write(chr((theChar1+ord('A'))))
            kCount+=1
    os.system('clear')
    print('The file has been saved in your working directory as: ', fileName)


def decrypt(s):
    kd = s
    # if s != None:
    #     kd=s
    # else:
    #     kd = input('\nEnter key used to encrypt this file:\n')
    #     kd=kd.upper()

    print('\n\nThe key is: ',kd)
    kLen = len(kd)
    kCount = 0
    dt =  datetime.datetime.now()
    DT=str(dt)
    fileName = ("decrypted_%s.txt"%DT)
    f = open(fileName, "x")
    for x in kd:
        keyD.append(x)

    theChar=None
    theChar1=None
    for x in letters:
        if kCount<kLen:
            theChar = (((ord(x)-ord('A'))-(ord(kd[kCount])-ord('A')))%26)
            f.write(chr((theChar+ord('A'))))
            kCount+=1
        elif kCount==kLen:
            kCount=0
            theChar1 = (((ord(x)-ord('A'))-(ord(kd[kCount])-ord('A')))%26)
            f.write(chr((theChar1+ord('A'))))
            kCount+=1
    # os.system('clear')
    print('\nThe file has been saved in your working directory as:\n',fileName,'\n')
    print('\n\nIf this was an attempt to crack a file, a log has been added to your working directory\n\n\n\n')



def getKeyLen():
    os.system('clear')
    printLogo()
    print('Finding the key length, please be patient...')
    keyLen = [1,2,3,4,5,6,7]
    lenOfKey = None
    splitLetters = []
    matches = 0
    crackPercentages.clear()
    splitLetters.clear()
    count=1
    tic = 0
    done = False
    dt =  datetime.datetime.now()
    DT=str(dt)
    fileName = ("keyLenAttempts_%s.txt"%DT)
    f = open(fileName, "x")

    while done == False:
        for x in keyLen:
            toWrite = '\n\n\nAttempting to crack with key length of '
            f.write(toWrite)
            f.write(str(x))
            # f.write(toWrite)
            f.write('\n')
            num = 0
            splitLetters.append([])
            for h in range(x):
                splitLetters[h].clear()
            for i in letters:
                splitLetters[num].append(i)
                if num < x-1:
                    num += 1
                else:
                    num = 0
            crackPercentages.clear()
            tic = 0
            for y in range(len(splitLetters)):
                crackPercentages.clear()
                for c in alphabet:
                    letterSum = 0
                    for j in splitLetters[y]:
                        if j == c:
                            letterSum+=1
                    crackPercentages.append(letterSum/len(splitLetters[y]))
                f.write('\n')
                # toWrite2 = 'The statistics for a key length of ',x,' are: ',crackPercentages
                f.write(str(crackPercentages))
                # f.write('\n\n\n')
                if check(crackPercentages) != True:
                    maxLet.clear()
                    f.write('\n\nFAIL - highest % found was ')
                    f.write(str(max(crackPercentages)))
                    f.write('\n')
                    continue
                elif check(crackPercentages)==True:
                    maxLet.append(alphabet[crackPercentages.index(max(crackPercentages))])
                    f.write('\n\nSTATISTICS MATCH - highest % found was ')
                    f.write(str(max(crackPercentages)))
                    f.write('\n')
                    tic += 1
            if tic == x:
                # os.system('clear')
                print('\n\nThe key length is ',x)
                f.write('\nKEY LENGTH FOUND:')
                f.write(str(x))
                f.write('\nPassing key length to function crack()')
                done = True
                crack(x)
                break


def check(a):
    if max(crackPercentages) > .125:
        return (True)
    else:
        return(False)



def crack(x):
    theKeyLen = x
    theKey = []
    counter = 0
    forCrack = []

    print('\n\nCracking the key...')
    for i in range(theKeyLen):
        keyVal = (alphabet.index(maxLet[i])-alphabet.index('E'))%26
        k = alphabet[keyVal]
        theKey.append(alphabet[keyVal])
    decrypt("".join(theKey))





def printLogo():
    print("""╦  ┌─┐┬ ┬┌┬┐┌─┐  ╦  ╦┬┌─┐┌─┐┌┐┌┌─┐┬─┐┌─┐  ╔═╗┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
║  │ │└┬┘ ││└─┐  ╚╗╔╝││ ┬├┤ │││├┤ ├┬┘├┤   ║  ├┬┘├─┤│  ├┴┐├┤ ├┬┘
╩═╝└─┘ ┴ ─┴┘└─┘   ╚╝ ┴└─┘└─┘┘└┘└─┘┴└─└─┘  ╚═╝┴└─┴ ┴└─┘┴ ┴└─┘┴└─
""")



if __name__== "__main__":
    main()
