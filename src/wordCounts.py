import googlesearch as gs
import clarifaiClassify as cl

def main():
    urls = gs.getUrls('bernie sanders', 10, 'face', 'y[1]')
    words = cl.classifyUrls(urls)
    print words

if __name__ == '__main__':
    main()

