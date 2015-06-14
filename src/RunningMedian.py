import sys
import glob
import re

class RunningMedian:
    def __init__(self, path):
        self.__path = path
        self.__alphaNumericRegex = re.compile('[\W_]+')

    def cound_median(self):
        files = glob.glob(self.__path)
        countOfWords = []

        for file in files:
            countOfWords.extend(self.__parse_file(file))

        medians = self.__getCumulativeMedian(countOfWords)
        return medians

    def __parse_file(self, file):
        countOfWords = []
        with open(file, "r") as stream:
            for line in stream:
                cleanWords = self.__parse_line(line)
                countOfWords.append(len(cleanWords))
        return countOfWords

    def __parse_line(self, line):
        words = line.split(" ")
        cleanWords = []

        for word in words:
            cleanWord = self.__alphaNumericRegex.sub('', word.lower().strip())

            if cleanWord == '':
                continue

            cleanWords.append(cleanWord)
        return cleanWords

    # idea is to add a new item in a sorted array honoring position of items
    # and then calculate the median
    # thus reducing calculation complexity
    def __getCumulativeMedian(self, countOfWords):
        medians = []
        sortedList = []

        x = range(len(countOfWords))
        for i in x:
            self.__paste(sortedList, countOfWords[i])
            md = self.__getMedian(sortedList)
            medians.append(md)

        return medians

    # regular median calculation routine
    def __getMedian(self, array):
        if len(array) % 2 == 0:
            middle = len(array) // 2
            return (array[middle] + array[middle - 1]) / 2
        else:
            return float(array[round(len(array) // 2)])

    # paste item in a sorted array respecting ordering via binary search
    def __paste(self, array, item):
        min = 0
        max = len(array)
        m = 0

        while max - min > 0:
            m = (min + max) // 2
            if array[m] > item:
              max = m
            else:
              min = m + 1

        array.insert(max, item)

    def save_to_file(self, file, result):
        with open(file, "w") as stream:
            for item in result:
                print(item, file=stream)

if __name__ == '__main__':
    wc = RunningMedian("../wc_input/*.txt")
    res = wc.cound_median()
    wc.save_to_file("../wc_output/med_result.txt", res)
    sys.exit(0)

