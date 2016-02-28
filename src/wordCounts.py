import googlesearch as gs
import clarifaiClassify as cl

def classifyImages(query, numImgs, imgType, dateRange):
    urls = gs.getUrls(query, numImgs, imgType, dateRange)
    words = cl.classifyUrls(urls)
    return words

