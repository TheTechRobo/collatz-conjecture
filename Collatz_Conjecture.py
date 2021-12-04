#Collatz Conjecture Program
#Created by Lewis Watson

from time import time
import json

BANNED_NUMBERS = list()

class Number:
    def __init__(self, number):
        self.number = number
        self.originNumber = number
        self.verifyNumber(self.number)
    def verifyNumber(self, number):
        try:
            self.originNumber = int(number)
            self.number = int(number)
            if self.number in BANNED_NUMBERS:
                raise ValueError("number cannot be banned")
        except (ValueError, TypeError):
            raise # too lazy to unindent lmao
    iterateCount = 0
    alreadyDone = list()
    def iterate(self):
        while True:
            if self.number < 2**68 or self.number in BANNED_NUMBERS:
                self.writeCsv(Yes=True)
                break
            #input(self.originNumber)
            if (self.number % 2) == 0:
                self.number = self.number // 2
            else:
                self.number = (self.number * 3) + 1
            self.iterateCount += 1
            BANNED_NUMBERS.append(self.number)
            self.writeCsv()
    def writeCsv(self, Yes=False):
        if Yes is True:
            with open("Collatzthetechrobo%s.CSV" % self.originNumber, "a+") as csv: csv.write("Done: banned number %s" % self.number)
            return "SEP"
        with open("Collatzthetechrobo%s.CSV" % self.originNumber, "a+") as csv:
            csv.write(str(self.iterateCount) + "," + str(self.number) + "," + str(time()) + "\n")
    def writeJson(self):
        with open("Collatzthetechrobo.JSON", "w+") as file:
            deeta = json.dumps(
                    {
                        BANNED_WORDS
                    }
            )
            file.write(deeta)

if __name__ == "__main__":
    nbum = 2 ** 68
    while True:
        num = Number(nbum)
        num.iterate()
        nbum += 1
        if nbum % 100 == 0: print("kinda sus ngl (num", nbum, ")")
