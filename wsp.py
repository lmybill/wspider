#!/usr/bin/python
#coding=utf-8
import urllib
import time
import sys
import os
import re

#获取命令行传进来的参数
for i in range(1, len(sys.argv),2):
    print(sys.argv[i])
tinter=sys.argv[2]
url=sys.argv[4]
direct=sys.argv[6]

#获取系统时间
localtime=time.strftime("%Y%m%d%H%M", time.localtime(time.time()))

#创建文件夹
path=direct+'/'+localtime
if not os.path.exists(path):
    os.makedirs(path)
    imagepath=path+'/images'
    jspath=path+'/js'
    csspath=path+'/css'
    os.makedirs(imagepath)
    os.makedirs(jspath)
    os.makedirs(csspath)

#获取html
def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    filepath=path+'/main.html'
    urllib.urlretrieve(url,filepath)
    return html
html=getHtml(url)

#获取css
def getCss(html):
    regcss=r'href="(.+?\.css)"'
    cssre=re.compile(regcss)
    csslist=re.findall(regcss,html)
    for cssurl in csslist:
 
        filepath=csspath+'/'+cssurl.split('/')[-1]
        urllib.urlretrieve(cssurl, filepath)


#获取imgages
def getImg(html):
    reg=r'="(.+?\.jpg)"'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    for imgurl in imglist:
        filepath=imagepath+'/'+imgurl.split('/')[-1]
        urllib.urlretrieve(imgurl, filepath)


#获取Js
def getJs(html):
    regjs=r'src="(.+?\.js)"'
    jsre=re.compile(regjs)
    #print('abc')
    jslist=re.findall(jsre,html)
    #print(jslist)
    for jsurl in jslist:
        y='/js/'+jsurl.split('/')[-1]
        with open(path+'/main.html', "r+") as f:
            d=f.read()
            d=d.replace(jsurl, y)
            f.write(d)
        f.close()
       
        #html=html.replace(jsurl,r)
        #print(html)
        print(jsurl)
        filepath=jspath+'/'+jsurl.split('/')[-1]
        urllib.urlretrieve(jsurl, filepath)


getHtml(url)
getJs(html)
getCss(html)
getImg(html)


