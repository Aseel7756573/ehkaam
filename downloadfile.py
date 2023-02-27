import cgi
import os
import urllib.request
from urllib.request import urlopen, urlretrieve
import time
class downloadfile ():
    link=""
    number=0
    def __init__(self,l,n):
        self.number=n
        self.link=l
    def getHeader(self):

        try:
            remotefile = urlopen(self.link)
            blah = remotefile.info()['Content-Disposition']
            value, params = cgi.parse_header(blah)

            filename = "files/image_" + str(self.number) + ".jpg"
            urlretrieve(self.link, filename)
        except Exception as e:
            try:
                remotefile = urlopen(self.link)
                blah = remotefile.info()['Content-Disposition']
                value, params = cgi.parse_header(blah)

                filename = "files/image_" + str(self.number) + ".jpg"
                urlretrieve(self.link,filename )
            except Exception as ex:
                print(ex.read())





