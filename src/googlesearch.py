from googleapiclient.discovery import build
import pprint



def main():
    service = build("customsearch", "v1",
              developerKey="AIzaSyBfKuONYZkZ56UqyZ45OYK9exNAI8FBapc")

    res = service.cse().list(
        q='donald trump',
        cx='006736731268319443987:hdhdfnrz2om',
        safe='high',
        searchType='image',
        imgSize='medium',
        imgType='face',
        dateRestrict='y[2]',
        num=3
    ).execute()

    #pprint.pprint(res)

    if not 'items' in res:
        print 'No result !!\nres is: {}'.format(res)
    else:
        for item in res['items']:
            print('{}:\n\t{}'.format(item['title'], item['link']))

if __name__ == '__main__':
    main()