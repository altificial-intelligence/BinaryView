from googleapiclient.discovery import build

class ImageSearch:

    def __init__(self):
        self.apiKey = "AIzaSyBfKuONYZkZ56UqyZ45OYK9exNAI8FBapc"
        self.searchEngineId = '006736731268319443987:hdhdfnrz2om'
        self.service = build("customsearch", "v1",
                             developerKey=self.apiKey)

    def getImages(self, query, numImages):
        return self.service.cse().list(
                q=query,
                cx=self.searchEngineId,
                safe='high',
                searchType='image',
                imgSize='medium',
                imgType='face',
                dateRestrict='y[2]',
                num=numImages
        ).execute()

    def parseImages(self, response):
        if not 'items' in response:
            print 'No result !!\nres is: {}'.format(response)
        else:
            for item in response['items']:
                print('{}:\n\t{}'.format(item['title'], item['link']))



def main():
    imgS = ImageSearch()
    imgS.parseImages(imgS.getImages('donald trump', 2))



if __name__ == '__main__':
    main()