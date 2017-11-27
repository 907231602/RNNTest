s = 'B0A1' #你好

#45217
#63486
'''
for kk in range(45217,63486):
    #print(str(hex(kk))[2:6])
    s=str(hex(kk))[2:6]
    bi = []
    for i in range(len(s) // 2):
        bi = bi + [int(s[i * 2:i * 2 + 2], 16), ]
    bs = bytearray(bi)
    print(bytes(bs).decode('gb2312'))
'''
bi=[]
for i in range(len(s)//2):
    bi = bi + [int(s[i*2:i*2+2],16), ]
bs = bytearray(bi)
print(bytes(bs).decode('gb2312') )#你好