from googleapiclient.discovery import build
import argparse


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

    def saveFile(self, fileName, urls):
        file = open(fileName, "w")
        for url in urls:
            file.write(url + "\n")
        file.close()

    def saveLinks(self, query, numLinks, imgType, dateRange, fileName):
        self.saveFile(fileName, self.parseImages(self.getImages(query, numLinks, imgType, dateRange)))


def parseCommands():
    parser = argparse.ArgumentParser(prog='Image Search.')
    subparsers = parser.add_subparsers(dest='getUrls', help='Get URLs of images based on query.')
    parser_query = subparsers.add_parser('saveUrls', help='Save URLs to text file.')
    parser_query.add_argument('query', help='The query.')
    parser_query.add_argument('numLinks', help='Number of URLs.')
    parser_query.add_argument('imgType', help='The image type.')
    parser_query.add_argument('dateRange', help='The date range.')
    parser_query.add_argument('fileName', help='The text file name.')
    parser_query.set_defaults(getUrls=getUrlsByQuery)
    args = parser.parse_args()
    args.getUrls(args)

def getUrlsByQuery(args):
    imgS = ImageSearch()
    imgS.saveLinks(args.query, args.numLinks, args.imgType, args.dateRange, args.fileName)

def main():
    parseCommands()


if __name__ == '__main__':
    main()