#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from PIL import Image
import random
#获取文件个数
class MyFileInfo:
    #初始化
    def __init__(self):
        self.listFile=[]
    #获取目录下文件个数
    def totalfile(self,dir):
        count=0
        for file in os.listdir(dir):
            #print(file)
            if os.path.isfile(os.path.join(dir,file)):
                count+=1
                #print(file)
                self.listFile.append(file)
            elif os.path.isdir(os.path.join(dir,file)):
                pass
                #count+=totalfile(os.path.join(dir,file))
        return count
    #获取文件（图片）名
    def getFilesName(self):
        return self.listFile

    #根据下标返回图片和图片内容
    def getImageAndText(self,index):
        picName= self.listFile;
        str= picName[index];
        #print('str==>',str)
        img =Image.open("D:\AI\pythonPack\pic4\%s" % str)
        text=str.split('.')[0]
        if (str.split('.')[1] == 'png'):
            bg = Image.new("RGB", img.size, (255, 255, 255))
            # bg.paste(ims, ims);
            img, text = bg, str.split('.')[0]
        return img,text

    #通过随机值的方法获取27张图片的任意一张，并返回图片和内容
    def range32Pic(self):
        index = random.randint(0, 26)
        #print(index)
        picName = self.listFile;
        str = picName[index];
        img = Image.open("D:\AI\pythonPack\pic4\%s" % str)
        text = str.split('.')[0]
        if (str.split('.')[1] == 'png'):
            bg = Image.new("RGB", img.size, (255, 255, 255))
            # bg.paste(ims, ims);
            img, text = bg, str.split('.')[0]

        return img, text



if __name__ == "__main__":
    myfile=MyFileInfo()
    num = myfile.totalfile("D:\AI\pythonPack\pic4")
    print(num)
    print(myfile.getFilesName())
    print(myfile.listFile)
    print(myfile.range32Pic())
    x= random.randint(1,27)
    for j in range(27):
        print(myfile.range32Pic())