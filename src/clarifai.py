from clarifai.client import ClarifaiApi

class Classify:

    def __init__(self):
        self.clarifai = ClarifaiApi() # assumes environment variables are set.

    def classify(self, url):
        return self.clarifai.tag_image_urls(url)


def main():
    c = Classify()
    res = c.classify('http://a3.files.biography.com/image/upload/c_fill,cs_srgb,dpr_1.0,g_face,h_300,q_80,w_300/MTE5NDg0MDU1MTUyNzIzNDcx.jpg')
    print res

if __name__ == '__main__':
    main()