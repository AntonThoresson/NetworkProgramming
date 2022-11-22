import math as m
import random as r
import zlib as z
with open("text.txt","r") as file:
    txt = file.read()
byteArr = bytearray(txt, "utf-8")
print("number of bytes in byteArr: ", len(byteArr))
print("number of symbols in txt: ", len(txt))
# The difference is that in UTF-8 can some symbols contain more than one byte, eg "Å, Ä, Ö" and thats why txt is "shorter" than the byteArr

def makeHisto(byteArr):
    histo = [0] * 256
    for byte in byteArr:
        histo[byte] += 1
    # print(histo)
    return histo

makeHisto(byteArr)

def makeProb(histo):
    probDist = [0.0] * 256
    totalSumOfProbDist = 0
    for i in range(256):
        probDist[i] += histo[i]/len(byteArr)
        totalSumOfProbDist += probDist[i]
    return probDist


makeProb(makeHisto(byteArr))    


def entropi(prob):
    entropy = 0
    for i in range(len(prob)):
        if prob[i] == 0.0:
            continue
        entropy += prob[i] * -m.log2(prob[i])  
    print(round(entropy, 2))
    return entropy

entropi(makeProb(makeHisto(byteArr)))    

# it can be compressed to 4.6 byte/char
theCopy = byteArr.copy()
r.shuffle(theCopy)
theCopyCompressed = z.compress(theCopy)
byteArrCompressed = z.compress(byteArr)

def countSourceSymbols(compressedData):
    numberOfSymbols = 0
    for i in compressedData:
        numberOfSymbols += i
    return numberOfSymbols


print("theCopyCompress bytes: ", len(theCopyCompressed))
print("theCopyCompressed bits: ", len(theCopyCompressed)*8)
print("theCopyCompressed source symbols: ", countSourceSymbols(theCopyCompressed))
print("byteArrCompressed bytes: ", len(byteArrCompressed))
print("byteArrCompressed bites: ", len(byteArrCompressed)*8)
print("byteArrCompressed source symbols: ", countSourceSymbols(byteArrCompressed))
# theCopyCompress bytes:  19872
# byteArrCompressed bytes:  12864

# entropy = 4,6 - optimal encodning but doesnt make use of stat redundancy 

# theCopyCompressed = - 5,6 - not using optimal encoding since its higher than entropy as well as not making use of stat redundancy since its shuffled

# byteArrCompressed = 3,89 - optimal encoding and uses stat redundancy

t1 = """I hope this lab never ends because
it is so incredibly thrilling"""

t10 = t1*10

t1Byte = bytearray(t1, "utf-8")
print(len(t1Byte)) #64
t10Byte = bytearray(t10, "utf-8")
print(len(t10Byte)) #640



t1Compressed = z.compress(t1Byte)
print(len(t1Compressed)) #66
t10Compressed = z.compress(t10Byte)
print(len(t10Compressed)) #75

# No its not since the compress function recognizes that is the same text 10 times over
