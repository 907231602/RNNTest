#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs
import random
def getText():
    str=''
    with codecs.open("text256.txt",encoding='utf-8') as fp:
        data = fp.read()
        str+=data
        kk=set(str)
        kk.remove('\n')
        kk.remove('\r')
        print(''.join(kk))
    return ''.join(kk)

def get62Text():
    str=getText();
    str2= random.sample(str, 62)
    return ''.join(str2)

def get256Text():
    return getText();

def get62ExampleText():
    #解服多护件品推图览下确心预册签荐待成馈
    return '权级圾升页心品钱图抄易机认客码私件荐有旗网集成确红存盘邮博首册制推号办箱手立密添签精垃加功特送标理造下待注证人助文即地黄址中'
    #return '开策相绒对试重隐内维易课收助天内账级图你博十草见受公例登虚荐服通反并文意码密内认有册二览圾确同关心视获阅网即历录地代忧免全馈'

if __name__=='__main__':
    print(getText())