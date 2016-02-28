from clarifai.client import ClarifaiApi


class Classify:

    def __init__(self):
        self.clarifai = ClarifaiApi() # assumes environment variables are set.
        self.wordsToCounts = {}

    def classify(self, url):
        return self.clarifai.tag_image_urls(url)

    # returns a list of classes
    def parseClassification(self, response):
        status = response['status_code']
        if status != "OK":
            print 'Error classifying using Clarifai API'
            return ""
        else:
            return response['results'][0]['result']['tag']['classes']

    def classifyUrls(self, urls):
        for url in urls:
            classes = self.parseClassification(self.classify(url))
            for className in classes:
                if className not in self.wordsToCounts:
                    self.wordsToCounts[className] = 1
                else:
                    self.wordsToCounts[className] += 1

    def countWords(self):
        words = []
        for word in self.wordsToCounts:
            count = self.wordsToCounts[word]
            for x in range(0, count):
                words.append(word)
        return words


def classifyUrls(urls):
    c = Classify()
    c.classifyUrls(urls)
    return c.countWords()


