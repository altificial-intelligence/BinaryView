import googlesearch as gs
import clarifaiClassify as cl

def classifyImages(query, numImgs, imgType, dateRange):
    urls = gs.getUrls(query, numImgs, imgType, dateRange)
    # get the first url, and put inside object!
    words = cl.classifyUrls(urls)
    return words

