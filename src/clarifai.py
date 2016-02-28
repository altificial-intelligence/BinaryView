from clarifai.client import ClarifaiApi
import os
import argparse


class WordCount:

    def __init__(self):
        self.wordsToCounts = {}


class Classify:

    def __init__(self):
        self.clarifai = ClarifaiApi() # assumes environment variables are set.
        # dictionary of filenames to wordCount objects
        self.filesToWordcounts = {}

    def reset(self):
        self.filesToWordcounts = {}

    def classify(self, url):
        return self.clarifai.tag_image_urls(url)

    # returns a list of classes
    def parseClassification(self, response):
        return response['results'][0]['result']['tag']['classes']

    def getFiles(self, directory):
        files = []
        for file in os.listdir(directory):
            if file.endswith(".txt"):
                files.append(file)
        return files

    def readFile(self, fileName):
        lines = []
        with open(fileName, 'r') as fileHandler:
            for line in fileHandler:
                lines.append(line.strip("\n"))
        return lines

    def readFiles(self, directory):
        files = self.getFiles(directory)
        for fileName in files:
            if fileName not in self.filesToWordcounts:
                self.filesToWordcounts[fileName] = WordCount()
            urls = self.readFile(directory + fileName)
            for url in urls:
                classes = self.parseClassification(self.classify(url))
                for className in classes:
                    if className not in self.filesToWordcounts[fileName].wordsToCounts:
                        self.filesToWordcounts[fileName].wordsToCounts[className] = 1
                    else:
                        self.filesToWordcounts[fileName].wordsToCounts[className] += 1

    def saveFile(self, fileName, lines):
        file = open(fileName, "w")
        for line in lines:
            file.write(line + " ")
        file.close()

    def saveWordCounts(self, directory):
        for fileName in self.filesToWordcounts:
            fileWords = []
            for className in self.filesToWordcounts[fileName].wordsToCounts:
                count = self.filesToWordcounts[fileName].wordsToCounts[className]
                for x in range(0, count):
                    fileWords.append(className)
            self.saveFile(directory + fileName, fileWords)


def classify(urls):



def parseCommands():
    parser = argparse.ArgumentParser(prog='Classify AI.')
    subparsers = parser.add_subparsers(dest='classifyUrls', help='')
    parser_classify = subparsers.add_parser('classify', help='Classify the list of URLs for each file.')
    parser_classify.add_argument('inputDir', help='The input directory of files of URLs.')
    parser_classify.add_argument('outputDir', help='The output directory for classified word tags.')
    parser_classify.set_defaults(classifyUrls=classifyUrlsByFile)
    args = parser.parse_args()
    args.classifyUrls(args)

def classifyUrlsByFile(args):
    c = Classify()
    c.readFiles(args.inputDir)
    c.saveWordCounts(args.outputDir)
    c.reset()

def main():
    parseCommands()

if __name__ == '__main__':
    main()