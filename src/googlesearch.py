from googleapiclient.discovery import build
import pprint

def main():
    service = build("customsearch", "v1",
              developerKey="AIzaSyBfKuONYZkZ56UqyZ45OYK9exNAI8FBapc")
    res = service.cse().list(
        q='lectures',
        cx='017576662512468239146:omuauf_lfve',
    ).execute()
    pprint.pprint(res)

if __name__ == '__main__':
    main()