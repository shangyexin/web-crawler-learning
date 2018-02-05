#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author : yasin
# @time   : 2018/2/5 10:06
# @File   : urllib_practice1.py

import socket
import urllib.request
import urllib.parse
import urllib.error

# data参数的使用
def demo1():
    data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')
    print(data)
    response = urllib.request.urlopen('http://httpbin.org/post', data=data)
    print(response.read())

# timeout参数的使用
def demo2():
    try:
        response = urllib.request.urlopen('http://httpbin.org/', timeout=0.1)
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('TIME OUT')

# 设置Headers
# 有很多网站为了防止程序爬虫爬网站造成网站瘫痪，会需要携带一些headers头部信息才能访问，最长见的有user-agent参数
# 写一个简单的例子：
def demo3():
    request = urllib.request.Request('https://python.org')
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))

# 给请求添加头部信息，从而定制自己请求网站是时的头部信息
def demo4():
    url = 'http://httpbin.org/post'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'HOST': 'httpbin.org'
    }
    dict = {
        'name': 'zhaofan'
    }
    data = bytes(urllib.parse.urlencode(dict), encoding='utf-8')
    req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))

# 添加请求头的第二种方式
def demo5():
    url = 'http://httpbin.org/post'
    dict = {
        'name': 'Germey'
    }
    data = bytes(urllib.parse.urlencode(dict), encoding='utf8')
    req = urllib.request.Request(url=url, data=data, method='POST')
    req.add_header( 'User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    response = urllib.request.urlopen(req)
    print(response.read().decode('utf-8'))

# 代理,ProxyHandler
# 通过rulllib.request.ProxyHandler()可以设置代理,网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，
# 它会禁止你的访问,所以这个时候需要通过设置代理来爬取数据
def demo6():
    proxy_handler = urllib.request.ProxyHandler({
        'http': 'http://127.0.0.1:9743',
        'https': 'https://127.0.0.1:9743'
    })
    opener = urllib.request.build_opener(proxy_handler)
    response = opener.open('http://httpbin.org/get')
    print(response.read())

# cookie,HTTPCookiProcessor
# cookie中保存中我们常见的登录信息，有时候爬取网站需要携带cookie信息访问,这里用到了http.cookijar，
# 用于获取cookie以及存储cookie
def demo_cookie():
    import http.cookiejar
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print(item.name + "=" + item.value)

# 同时cookie可以写入到文件中保存，有两种方式http.cookiejar.MozillaCookieJar和http.cookiejar.LWPCookieJar()
def demo_cookie2():
    import http.cookiejar
    filename = 'cookie.txt'
    cookie = http.cookiejar.LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)

# 同样的如果想要通过获取文件中的cookie获取的话可以通过load方式，当然用哪种方式写入的，就用哪种方式读取。
def demo_cookie3():
    import http.cookiejar
    cookie = http.cookiejar.LWPCookieJar()
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    print(response.read().decode('utf-8'))

# 异常处理
def demo_error():
    try:
        response = urllib.request.urlopen("http://pythonsite.com/1111.html")
    except urllib.error.HTTPError as e:
        print('HTTPError')
        print(e.reason)
        print(e.code)
        print(e.headers)
    except urllib.error.URLError as e:
        print('URLError')
        print(e.reason)
    else:
        print("reqeust successfully")

# HTTPError里有三个属性：code,reason,headers，即抓异常的时候可以获得code,reson，headers三个信息，例子如下：
def demo_error2():
    try:
        response = urllib.request.urlopen("http://www.pythonsite.com/", timeout=0.001)
    except urllib.error.URLError as e:
        print(type(e.reason))
        if isinstance(e.reason, socket.timeout):
            print("time out")

def demo_parse():
    from urllib.parse import urlparse
    result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
    print(result)

def demo_unparse():
    from urllib.parse import urlunparse
    data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=123', 'commit']
    print(urlunparse(data))

def demo_urljoin():
    from urllib.parse import urljoin
    print(urljoin('http://www.baidu.com', 'FAQ.html'))
    print(urljoin('http://www.baidu.com', 'https://pythonsite.com/FAQ.html'))
    print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html'))
    print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html?question=2'))
    print(urljoin('http://www.baidu.com?wd=abc', 'https://pythonsite.com/index.php'))
    print(urljoin('http://www.baidu.com', '?category=2#comment'))
    print(urljoin('www.baidu.com', '?category=2#comment'))
    print(urljoin('www.baidu.com#comment', '?category=2'))

def demo_urlencode():
    from urllib.parse import urlencode
    params = {
        "name":"zhaofan",
        "age":23
    }
    base_url = "http://www.baidu.com?"
    url = base_url + urlencode(params)
    print(url)

if __name__ == '__main__':
    # demo1()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    # demo6()
    # demo_cookie()
    # demo_cookie2()
    # demo_cookie3()
    # demo_error()
    # demo_error2()
    # demo_parse()
    # demo_unparse()
    # demo_urljoin()
    demo_urlencode()
