from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt
import random as rand

def randForm(case):
    if(case == 0):
        num = rand.randrange(0,10)
    else:
        num = rand.randrange(10,18)
    return "{:03d}".format(num)

def draw(t,person):
    t = str(str(t)+"\n").splitlines()
    textNumLines = len(t)
    temp = ""
    for l in range(1,len(t)):
        temp+=t[l]+"|"
    t = temp[:-1]
    images = []
    for l in t:
        off = 0
        if(l==" "):
           images.append([0,1,0,0,0])
        elif(l=="|"):
            h=0
            for i in images:
                if(i[1]==0):
                    if(i[0].size[1]>h):
                        h=i[0].size[1]
            images.append([0,2,h,0,1])
        else:
            if(l=="\"" or l=="“" or l=="”"):
                l="quote"
                off = 25
            elif(l=="~"):
                off = 5
            elif(l=="*"):
                l="star"
                off = 22
            elif(l=="^"):
                off = 22
            elif(l=="<"):
                l="less"
                off=2
            elif(l==">"):
                l="more"
                off=2
            elif(l=="\\"):
                l="bSlash"
            elif(l=="'" or l=="’" or l=="‘"):
                l="squote"
                off = 25
            elif(l==":"):
                l="colon"
            elif(l=="?"):
                l="qmark"
            elif(l=="—" or l=="°"):
                l="-"
            elif(l=="€" or l=="é" or l=="¢"):
                l="e"
            elif(l=="="):
                off = 10
            elif(l=="-"):
                l=="-"
                off = 13
            elif(l=="_"):
                l="-"
            elif(l=="+"):
                off = 2
            elif(l=="g" or l=="q"):
                off = -15
            elif(l=="y" or l=="p"):
                off = -7

            if(str(l).islower()):
                im = Image.open("----PATH_TO_HANDWRITING----\\"+person+"\\"+l+randForm(1)+".png")
                images.append([im,0,0,off,0])
            else:
                im = Image.open("----PATH_TO_HANDWRITING----\\"+person+"\\"+l+randForm(0)+".png")
                images.append([im,0,0,off,0])

    #
    space = 25
    lSpace = 5
    lineSpace = 50
    #

    w=0
    h=0
    hOff=0
    lines=1
    for i in images:
        if(i[1]==0):
            #w+=i[0].size[0]+lSpace
            if(i[0].size[1]>h):
                totalHeight=i[0].size[1]
        else:
            w+=space
        if(i[1]==2):
            lines+=1
    hOff = totalHeight

    inds = []
    wids = []
    temps = []
    buffC = 0
    for i in range(len(images)):
        if(images[i][4]==1):
            inds.append(i)
    for im in range(0,inds[0]):
        if(images[im][1]==1):
            buffC += int(space*.7)
        if(images[im][1]==0):
            wids.append(images[im][0].size[0]+lSpace+4)
    temp = 0
    for x in wids:
        temp+=x
    temps.append(temp+buffC)
    buffC = 0
    if(textNumLines>1):
        for i in range(1,len(inds),1):
            wids = []
            for im in range(inds[i-1],inds[i]):
                if(images[im][1]==1):
                    buffC += int(space*.7)
                if(images[im][1]==0):
                    wids.append(images[im][0].size[0]+lSpace+4)
            temp = 0
            for x in wids:
                temp+=x
            temps.append(temp+buffC)
            buffC = 0
    maxWid = 0
    for t in temps:
        if(t>maxWid):
            maxWid=t


    imF = Image.new('RGBA', (maxWid+buffC,(totalHeight+lineSpace)*lines+20),(255,255,255,0))
    # pixdata = imF.load()
    # width = imF.size[0]
    c=0
    for i in images:
        if(i[1]==2):
            totalHeight+=hOff+lineSpace+rand.randrange(-5,5)
            c=0
        elif(i[1]==0):
            # for y in range(4,6,1):
            #     for x in range(width):
            #         pixdata[x,h+y] = (129,164,222,50)
            imF.paste(i[0], (c+10,(totalHeight-i[0].size[1]-i[3]+((lSpace+hOff)*3)+rand.randrange(-5,5))))
            c+=i[0].size[0]+lSpace+rand.randrange(-2,2)
        elif(i[1]==1):
            c+=space+rand.randrange(-2,2)

    imF.putalpha(255)
    imF.save("----PATH_FOR_TEMPORARY_IMAGE----")

    imF.show()

draw("""
Long Data
""","TESTAUTOCROP")

# draw(pytesseract.image_to_string(Image.open("C:\\Users\\lmgab\\PycharmProjects\\tensorenv\\handwriting\\dubapp.jpg")))







