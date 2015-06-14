import sys
import glob
import re

class WordCounting:
    def __init__(self, path):
        self.__path = path
        self.__alphaNumericRegex = re.compile('[\W_]+')

    def count_words(self):
        result = dict()
        files = glob.glob(self.__path)

        for file in files:
            self.__parse_file(file, result)

        return result

    def __parse_file(self, file, result):
        with open(file, "r") as stream:
            for line in stream:
                self.__parse_line(line, result)

    # idea is clean each word from not alphanumeric characters
    # and insert them into a dictionary
    def __parse_line(self, line, result):
        words = line.split(" ")

        for word in words:
            cleanWord = self.__alphaNumericRegex.sub('', word.lower().strip())

            if cleanWord == '':
                continue

            if cleanWord not in result:
                result[cleanWord] = 0

            result[cleanWord] += 1

    def save_to_file(self, file, result):
        orderedResult = sorted(result.keys())

        with open(file, "w") as stream:
            for item in orderedResult:
                print(item.ljust(15), str(result[item]).rjust(10), sep="", file=stream)

if __name__ == '__main__':
    wc = WordCounting("../wc_input/*.txt")
    res = wc.count_words()
    wc.save_to_file("../wc_output/wc_result.txt", res)
    sys.exit(0)

