
import requests
import os,sys


class RegistryHandler():

    def __init__(self,registryName):
        self.ver='v2'
        self.url=registryName

    @property
    def listImages(self):
        return "http://%s/%s/_catalog" % (self.url,self.ver,)

    def imageTagsReq(self,image):
        return "http://%s/%s/%s/tags/list" % (self.url, self.ver,image,)

    def images(self):
        url=self.listImages
        print("Debug - quering : ",url)
        tmp=requests.get(url)
        print(tmp)
        j= tmp.json()
        print(j)
        return j.get('repositories',[])

    def getImageTags(self,image):
        url=self.imageTagsReq(image)
        print('url is' , url)
        tmp=requests.get(self.imageTagsReq(image))
        print("Return responce" ,tmp )
        print(tmp.status_code)
        if tmp.status_code == 200:
            j=tmp.json().get('tags',[])
            print(j)
            return j
        else:
            raise ValueError('response status is %s' % tmp.status_code)

def buildImage(image,folder):
    pwd=os.path.curdir
    os.chdir(folder)
    out=os.popen('docker build -t %s .' % image,sys.stdout)
    print(out)
    os.chdir(pwd)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Missing parameters")
        exit(-1)
    registry=sys.argv[0]
    image=sys.argv[1]
    print("image" , image)
    print("registry" , registry)
    exit(0)
    tmp = RegistryHandler('172.29.37.222:5080')
    print("quring")
    res=tmp.images()
    print("Response:" , res)
    tres=tmp.getImageTags(res[-1])
    print("res of " , res[-1] , " .." , tres)