from googleapiclient.discovery import build


class ImageSearch:

    def __init__(self):
        self.apiKey = "AIzaSyBfKuONYZkZ56UqyZ45OYK9exNAI8FBapc"
        self.searchEngineId = '006736731268319443987:hdhdfnrz2om'
        self.service = build("customsearch", "v1",
                             developerKey=self.apiKey)

    def getImages(self, query, numImages, imgType, dateRange):

        # ensure number of images is between 1,10 inclusive for google custom search api
        numImagesLimit = 1
        if numImages > 10:
            numImagesLimit = 10
        elif numImages <= 0:
            numImagesLimit = 1
        else:
            numImagesLimit = numImages

        return self.service.cse().list(
                q=query,
                cx=self.searchEngineId,
                safe='medium',
                searchType='image',
                imgSize='medium',
                imgType=imgType,
                dateRestrict=dateRange,
                num=numImagesLimit
        ).execute()

    def parseImages(self, response):
        urls = []
        if not 'items' in response:
            print 'No result !!\nres is: {}'.format(response)
        else:
            for item in response['items']:
                urls.append(item['link'])
        return urls


def getUrls(query, numLinks, imgType, dateRange):
    imgS = ImageSearch()
    return imgS.parseImages(imgS.getImages(query, numLinks, imgType, dateRange))