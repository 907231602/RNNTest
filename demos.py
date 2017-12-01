#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from GetPicInfo import *
from PIL import Image

#获取文件夹下图片的名字和图片信息
myFile=MyFileInfo()
fileNum=myFile.totalfile("D:\AI\pythonPack\pic128");
fileName=myFile.listFile;
while(fileNum):
    namePop=fileName.pop();
    ims = Image.open("D:\AI\pythonPack\pic\%s" % namePop);
    img,text=ims,namePop.split('.')[0]
    if (namePop.split('.')[1] == 'png'):
        bg = Image.new("RGB", ims.size, (255, 255, 255))
        #bg.paste(ims, ims);
        img, text = bg, namePop.split('.')[0]
        bg.close()
    fileNum-=1;
    #print('-->',img,text)
    print(text)

'''
myFile=MyFileInfo()
fileNum=myFile.totalfile("D:\AI\pythonPack\pic");
fileName=myFile.listFile;
for j in range(fileNum):
    img ,text=myFile.getImageAndText(j)
    #ims = Image.open("D:\AI\pythonPack\pic\%s" % namePop);
    # img,text=ims,namePop.split('.')[0]
    # if (namePop.split('.')[1] == 'png'):
    #     bg = Image.new("RGB", ims.size, (255, 255, 255))
    #     #bg.paste(ims, ims);
    #     img, text = bg, namePop.split('.')[0]
    #     bg.close()
    # fileNum-=1;
    print('-->',img,text)
'''




