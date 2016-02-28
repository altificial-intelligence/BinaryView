import src.clarifaiClassify as cl
from src import googleSearch as gs


def classifyImages(query, numImgs, imgType, dateRange):
    urls = gs.getUrls(query, numImgs, imgType, dateRange)
    # get the first url, and put inside object!
    words = cl.classifyUrls(urls)
    return words

