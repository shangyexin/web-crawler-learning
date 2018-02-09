#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author : yasin
# @time   : 2018/2/7 18:54
# @File   : regex_practice.py

import re
import requests

# 最常规的匹配
def demo():
    content = "hello 123 4567 World_This is a regex Demo"
    result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$', content)
    print(result)
    print(result.group())
    print(result.span())

# 泛匹配
def demo2():
    content = "hello 123 4567 World_This is a regex Demo"
    result = re.match("^hello.*Demo$", content)
    print(result)
    print(result.group())
    print(result.span())

# 匹配目标
# 通过re.group()获得结果后，如果正则表达式中有括号，则re.group(1)获取的就是第一个括号中匹配的结果
def demo3():
    content = "hello 1234567 World_This is a regex Demo"
    result = re.match('^hello\s(\d+)\sWorld.*Demo$', content)
    print(result)
    print(result.group())
    print(result.group(1))
    print(result.span())

# 贪婪匹配
def demo4():
    content = "hello 1234567 World_This is a regex Demo"
    result = re.match('^hello.*(\d+).*Demo', content)
    print(result)
    print(result.group(1))

# 匹配模式
def demo5():
    content = """hello 123456 world_this 
    my name is leijun"""
    result = re.match('^he.*?(\d+).*?leijun$', content, re.S)
    print(result)
    print(result.group())
    print(result.group(1))

# 转义
def demo6():
    content = "price is $5.00"
    result = re.match('price is \$5\.00', content)
    print(result)
    print(result.group())

# re.search
def demo7():
    content = "extra things hello 123455 world_this is a Re Extra things"
    result = re.search("hello.*?(\d+).*?Re", content)
    print(result)
    print(result.group())
    print(result.group(1))

# 匹配演练
def demo8():
    html = '''<div id="songs-list">
        <h2 class="title">经典老歌</h2>
        <p class="introduction">
            经典老歌列表
        </p>
        <ul id="list" class="list-group">
            <li data-view="2">一路上有你</li>
            <li data-view="7">
                <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
            </li>
            <li data-view="4" class="active">
                <a href="/3.mp3" singer="齐秦">往事随风</a>
            </li>
            <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
            <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
            <li data-view="5">
                <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
            </li>
        </ul>
    </div>'''

    result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
    print(result)
    print(result.groups())
    print(result.group(1))
    print(result.group(2))

# re.findall
def demo9():
    html = '''<div id="songs-list">
        <h2 class="title">经典老歌</h2>
        <p class="introduction">
            经典老歌列表
        </p>
        <ul id="list" class="list-group">
            <li data-view="2">一路上有你</li>
            <li data-view="7">
                <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
            </li>
            <li data-view="4" class="active">
                <a href="/3.mp3" singer="齐秦">往事随风</a>
            </li>
            <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
            <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
            <li data-view="5">
                <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
            </li>
        </ul>
    </div>'''

    results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
    print(results)
    print(type(results))
    for result in results:
        print(result)
        print(result[0], result[1], result[2])

# re.sub
def demo10():
    content = "Extra things hello 123455 World_this is a regex Demo extra things"

    content = re.sub('(\d+)', r'\1 7890', content)
    print(content)

# re.compile
def demo11():
    content = """hello 12345 world_this
    123 fan
    """
    pattern = re.compile("hello.*fan", re.S)

    result = re.match(pattern, content)
    print(result)
    print(result.group())

def demo12():
    content = requests.get('https://book.douban.com/').text
    print(content)
    # pattern = re.compile(
    #     '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',
    #     re.S)
    # results = re.findall(pattern, content)
    # print(results)
    #
    # for result in results:
    #     url, name, author, date = result
    #     author = re.sub('\s', '', author)
    #     date = re.sub('\s', '', date)
    #     print(url, name, author, date)

if __name__ == '__main__':
    # demo()
    # demo2()
    # demo3()
    # demo4()
    # demo5()
    # demo6()
    # demo7()
    # demo8()
    # demo9()
    # demo10()
    # demo11()
    demo12()