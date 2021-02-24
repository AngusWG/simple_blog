#!/usr/bin/python3
# encoding: utf-8 
# @Time    : 2020/11/27 14:57
# @author  : zza
# @Email   : 740713651@qq.com
# @File    : 自动更新.py

import os
import re
import urllib

import requests
import tqdm
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

_path = os.path.abspath(__file__)
_dir_name = os.path.dirname(_path)  # 单个文件 下载驱动


def init_driver():
    executable_name = "chromedriver.exe"

    _file_path = _path.replace(os.path.basename(__file__), executable_name)
    if not os.path.exists(_file_path):  # 无驱则需要下载
        # 本地项目 复制驱动

        url = "https://raw.githubusercontent.com/AngusWG/crawler_set/tree/master/driver/chromedriver.exe"
        proxies = {
            "http": "socks5://127.0.0.1:9999",
            "https": "socks5://127.0.0.1:9999"
        }
        r = requests.get(url, proxies=proxies)

        with open(_file_path, "wb") as code:
            content_size = int(r.headers['content-length'])  # 内容体总大小
            for data in tqdm(iterable=r.iter_content(1024), total=content_size, unit="k", desc="下载驱动"):
                code.write(data)

    user_cookies = "".join([os.path.expanduser('~'), r"\AppData\Local\Google\Chrome\User Data"])

    option = webdriver.ChromeOptions()
    option.add_argument("--user-data-dir={}".format(user_cookies))  # 设置成用户自己的数据目录
    option.add_argument('--no-sandbox')
    # option.add_argument('--headless')
    option.add_argument('--disable-dev-shm-usage')
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    try:
        driver = webdriver.Chrome(r"C:\Users\links\Desktop\chromedriver.exe", options=option)
        driver.implicitly_wait(5)
        return driver
    except WebDriverException as err:
        print("请先关掉所有的Chrome")
        print(err)
        exit(-2)


driver = init_driver()


def save_images(file_name):
    if "好物" not in file_name:
        return
    with open(file_name, "r", encoding='utf8') as f:
        content = f.read()

    path = r'./docs/images'
    images = re.findall(r'\((https://upload-images.jianshu.io.*)\)', content)
    for img_url in images:
        driver.get(img_url)
        img = driver.find_element_by_xpath('//img')
        src = img.get_attribute('src')
        # download the image
        image_name = img_url.split("?")[0].split("/")[-1]
        image_path = os.path.join(path, image_name)
        urllib.request.urlretrieve(src, image_path)
        content = content.replace(img_url, "..\\images\\" + image_name)
    content = re.sub("[^ ]{2}(\n)", lambda match: match.group().replace("\n", "  \n"), content)
    with open(file_name, "w", encoding="utf8")as f:
        f.write(content)


def main():
    for _dir in [
        r'.\docs\编程',
        r'.\docs\随笔',
        r'.\docs\项目',
        r'.\docs\Python',
    ]:
        for i in tqdm.tqdm(os.listdir(_dir)):
            file_name = os.path.join(_dir, i)
            save_images(file_name)


main()
driver.close()
