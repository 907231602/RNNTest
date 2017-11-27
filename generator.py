import captcha
from vocab import Vocab
import numpy as np
from GetPicInfo import *

def JrttCaptchaGenerator(batch_size, path):
    # to determine dimensions
    cap = captcha.JrttCaptcha()
    #img, text = cap.get_captcha()
    img, text = cap.get_myImage()
    shape = np.asarray(img).shape
    #print('shape',shape)
    vocab = Vocab()
    #print('hhhh')
    while (1):
        X = np.empty((batch_size, shape[0], shape[1], shape[2]))
        #Y = np.empty((batch_size, len(text) * vocab.size))
        Y = np.empty((batch_size, len(text) * vocab.size))
        #print('y===',Y)
        myFile = MyFileInfo()
        fileNum = myFile.totalfile("D:\AI\pythonPack\pic4");
        #for j in range(batch_size):
        for j in range(batch_size):
            #img, text = cap.get_captcha()
            #img, text = cap.get_myImage()
            img, text =myFile.range32Pic()
            #print('j=',j)
            #img, text = myFile.getImageAndText(j)
            #img.save(path + text + ".jpg")
            X[j] = np.array(img) / 255
            Y[j] = vocab.text_to_one_hot(text)
            #print("--->>>",X[j],Y[j])
        #print("x",X,'y',Y)
        yield X, Y