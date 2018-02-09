#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author : yasin
# @time   : 2018/2/8 19:18
# @File   : selenium_pratice.py

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def demo1():
    from selenium import webdriver

    browser = webdriver.Chrome()

    browser.get("http://www.baidu.com")
    print(browser.page_source)
    browser.close()

# 单个元素查找
def demo2():
    browser = webdriver.Chrome()

    browser.get("http://www.taobao.com")
    input_first = browser.find_element_by_id("q")
    input_second = browser.find_element_by_css_selector("#q")
    input_third = browser.find_element_by_xpath('//*[@id="q"]')
    print(input_first)
    print(input_second)
    print(input_third)
    browser.close()

def demo3():
    browser = webdriver.Chrome()

    browser.get("http://www.taobao.com")
    input_first = browser.find_element(By.ID, "q")
    print(input_first)
    browser.close()

# 对于获取的元素调用交互方法
def demo4():

    browser = webdriver.Chrome()
    browser.get("http://www.taobao.com")
    input_str = browser.find_element_by_id('q')
    input_str.send_keys("ipad")
    time.sleep(1)
    input_str.clear()
    input_str.send_keys("MakBook pro")
    button = browser.find_element_by_class_name('btn-search')
    button.click()

# 将动作附加到动作链中串行执行
def demo5():
    from selenium.webdriver import ActionChains

    browser = webdriver.Chrome()

    url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()

# 执行JavaScript
def demo6():
    browser = webdriver.Chrome()
    browser.get("http://www.zhihu.com/explore")
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')

# 获取元素属性
def demo7():
    browser = webdriver.Chrome()
    url = 'https://www.zhihu.com/explore'
    browser.get(url)
    logo = browser.find_element_by_id('zh-top-link-logo')
    print(logo)
    print(logo.get_attribute('class'))

# 获取文本值
def demo8():
    browser = webdriver.Chrome()
    url = 'https://www.zhihu.com/explore'
    browser.get(url)
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input.text)

# Frame
def demo9():
    import time
    from selenium.common.exceptions import NoSuchElementException

    browser = webdriver.Chrome()
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    print(source)
    try:
        logo = browser.find_element_by_class_name('logo')
    except NoSuchElementException:
        print('NO LOGO')
    browser.switch_to.parent_frame()
    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)

# 隐式等待
def demo10():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get('https://www.zhihu.com/explore')
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input)

# 显示等待
def demo11():
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com/')
    wait = WebDriverWait(browser, 10)
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(input, button)

# 浏览器的前进和后退
def demo12():
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com/')
    browser.get('https://www.taobao.com/')
    browser.get('https://www.python.org/')
    browser.back()
    time.sleep(1)
    browser.forward()
    browser.close()

# cookie操作
def demo13():
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    print(browser.get_cookies())
    browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'zhaofan'})
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())

# 选项卡管理
def demo14():
    browser = webdriver.Chrome()
    browser.get('https://www.baidu.com')
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to_window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    time.sleep(1)
    browser.switch_to_window(browser.window_handles[0])
    browser.get('https://python.org')

# 异常处理
def demo15():
    from selenium.common.exceptions import TimeoutException, NoSuchElementException

    browser = webdriver.Chrome()
    try:
        browser.get('https://www.baidu.com')
    except TimeoutException:
        print('Time Out')
    try:
        browser.find_element_by_id('hello')
    except NoSuchElementException:
        print('No Element')
    finally:
        browser.close()

if __name__ == '__main__':
    # demo1()
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
    # demo12()
    # demo13()
    # demo14()
    demo15()