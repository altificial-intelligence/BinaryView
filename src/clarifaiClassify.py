from clarifai.client import ClarifaiApi


class Classify:

    def __init__(self):
        self.clarifai = ClarifaiApi() # assumes environment variables are set.
        self.wordsToCounts = {}

    def classify(self, url):
        try:
            return self.clarifai.tag_image_urls(url)
        except:
            print 'Error classifying image with Clarifai API'
            return {}

    # returns a list of classes
    def parseClassification(self, response):
        # if good response
        if bool(response):
            status = response['status_code']
            classes = response['results'][0]['result']['tag']['classes']
            # if type is gif, get the nested classes
            if any(isinstance(i, list) for i in classes):
                allClasses = []
                for sublist in classes:
                    for item in sublist:
                        allClasses.append(item)
                return allClasses
            else:
                return classes
        else:
            return []

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
            wordDict = {}
            # expected by jqcloud
            wordDict['text'] = str(word)
            wordDict['weight'] = count
            words.append(wordDict)
        return words


def classifyUrls(urls):
    c = Classify()
    c.classifyUrls(urls)
    return c.countWords()


