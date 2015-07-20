#!/usr/bin/env python

import urllib
import time
import re
import os

# Configuration
user = '$USER'
urlString = "http://www.reddit.com/r/EarthPorn/top/?sort=top&t=day"  #Reddit page to check
folder ='/Users/' + user + '/Pictures/Backgrounds/'  #Folder to store images

def main():

    time.sleep(0) #Delay while internet connection is established on powerup

    deleteOldImages()

    [urlList,numImg] = grabLinks()

    imgName = 0
    numUrls = len(urlList)

    # Script will grab 2 urls for each image (how Reddit is set up, I think)
    for index in range(0,numUrls,2):
        url = urlList[index]
        fileName = "/Users/" + user + "/Pictures/Backgrounds/" + time.strftime("%m") + "_" + time.strftime("%d") + "_" + "%d.jpg" %imgName
        imgName += 1

        getImage(url,fileName)





def grabLinks():

    htmlSource = urllib.urlopen(urlString).read().decode("iso-8859-1")
    urlList = re.findall("http://i.imgur.com/\w+.jpg", htmlSource)
    numImg = len(urlList)

    return urlList,numImg



def getImage(imgUrl,fileName):

    image=urllib.URLopener()
    image.retrieve(imgUrl,fileName)  # download comicName at URL


def deleteOldImages():


    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e



if __name__ == "__main__":

    main()
