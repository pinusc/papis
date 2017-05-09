import re
import papis.downloaders.base


class Get(papis.downloaders.base.Downloader):
    def __init__(self, url):
        papis.downloaders.base.Downloader.__init__(self, url)

    @classmethod
    def match(cls, url):
        if re.match(r"^http.*\.pdf$", url):
            return Get(url)
        else:
            return False

    def getDocumentUrl(self):
        print("doc begin")
        print("doc end")
        return self.getUrl()
