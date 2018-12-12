#!/usr/bin/env python
#coding:utf-8
import urllib2
import re
import random
import urllib2
#随机一个IP
def get_ip():
        a=random.randint(0,255)
        b=random.randint(0,255)
        c=random.randint(0,255)
        d=random.randint(0,255)
        ip=str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)
        return ip
#处理网络请求
def get_html(url):
        request=urllib2.Request(url)
        request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
        request.add_header('Accept-Language','zh-CN,zh;q=0.8')
        request.add_header('X-Forwarded-For',get_ip())
        request.add_header('Referer','http://91porn.com/index.php')
        response=urllib2.urlopen(request).read()
        return response
#获取视频连接
def get_links(url):
        html = get_html(url)
        pattern = re.compile('[a-zA-z]+://[^\s]*viewtype=basic&category=rf')
        links = pattern.findall(html)
        links = list(set(links))
        return links
#获取title与mp4
def get_title(links):
        for i in range(0,len(links)):
                url = links[i]
                html = get_html(url)
                with open('91.txt','a') as f:
                    pattern = re.compile('\<title\>[^\t]*\<\/title\>')
                    title = pattern.findall(html)[0].replace('<title>','').replace('</title>','').replace('\n','').replace('-Chinese homemade video','').replace(' ','')
                    print title
                    f.write(title)
                    try:
                        pattern = re.compile('[a-zA-z]+://[^\s]*?st=.*"')
                        mp4url = pattern.findall(html)[0].replace('"','')
                        print mp4url
                        f.write(mp4url)
                    except:
                        pass
def main():
    pages=int(input("骚年，你想看几页？"))
    for i in range(0,pages):
        url='http://91porn.com/v.php?category=rf&viewtype=basic&page='+str(i)
        links=get_links(url)
        get_title(links)
if __name__ == '__main__':
    main()
#author:榆木
#仅供个人学习之用，切勿用于其他用途