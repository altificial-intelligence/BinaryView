from clarifai.client import ClarifaiApi

class Classify:

    def __init__(self):
        self.clarifai = ClarifaiApi() # assumes environment variables are set.

    def classify(self, url):
        return self.clarifai.tag_image_urls(url)


def main():
    c = Classify()
    fileName = 'https://usatelections.files.wordpress.com/2015/06/xxx_a13_trump_2000_24.jpg?w=198&h=300'
    fileName2 = 'http://politicks.org/IMAGES/CANDIDATES/2016/PRESIDENT/Donald-Trump.gif'
    res = c.classify(fileName2)
    print res

if __name__ == '__main__':
    main()