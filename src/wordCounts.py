import clarifaiClassify as cl
import googlesearch as gs


def classifyImages(query, numImgs, imgType, dateRange):
    urls = gs.getUrls(query, numImgs, imgType, dateRange)
    # get the first url, and put inside object!
    words = cl.classifyUrls(urls)
    return words

