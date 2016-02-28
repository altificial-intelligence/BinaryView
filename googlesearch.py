from googleapiclient.discovery import build


class ImageSearch:

    def __init__(self):
        self.apiKey = "AIzaSyBfKuONYZkZ56UqyZ45OYK9exNAI8FBapc"
        self.searchEngineId = '006736731268319443987:hdhdfnrz2om'
        self.service = build("customsearch", "v1",
                             developerKey=self.apiKey)

    def getImages(self, query, numImages, imgType, dateRange):
        return self.service.cse().list(
                q=query,
                cx=self.searchEngineId,
                safe='high',
                searchType='image',
                imgSize='medium',
                imgType=imgType,
                dateRestrict=dateRange,
                num=numImages
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