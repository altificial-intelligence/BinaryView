from clarifai.client import ClarifaiApi
import os

class Classify:

    def __init__(self):
        self.clarifai = ClarifaiApi() # assumes environment variables are set.

    def classify(self, url):
        return self.clarifai.tag_image_urls(url)

    def parseClassification(self, response):
        return response['results'][0]['result']['tag']['classes'][0]

def main():


    fileName = 'https://usatelections.files.wordpress.com/2015/06/xxx_a13_trump_2000_24.jpg?w=198&h=300'
    fileName2 = 'http://politicks.org/IMAGES/CANDIDATES/2016/PRESIDENT/Donald-Trump.gif'
    # c = Classify()
    # classes = c.parseClassification(c.classify(fileName2))
    # classes =  res['results'][0]['result']['tag']['classes'][0]
    """
    for className in classes:
        print className
    """

if __name__ == '__main__':
    main()