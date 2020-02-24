# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests, sys


"""
类说明:下载《笔趣看》网小说《一念永恒》
Parameters:
    无
Returns:
    无
Modify:
    2017-09-13
"""


class downloader(object):

    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.names = []  # 存放章节名
        self.urls = []  # 存放章节链接
        self.nums = 0  # 章节数

    """
    函数说明:获取下载链接
    Parameters:
        无
    Returns:
        无
    Modify:
        2017-09-13
    """

    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.content
        div_bf = BeautifulSoup(html, features="html.parser")
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]), features="html.parser")
        a = a_bf.find_all('a')
        self.nums = len(a[16:20])  # 剔除不必要的章节，并统计章节数
        for each in a[16:20]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    """
    函数说明:获取章节内容
    Parameters:
        target - 下载连接(string)
    Returns:
        texts - 章节内容(string)
    Modify:
        2017-09-13
    """

    def get_contents(self, target):
        req = requests.get(url=target)
        html = req.content
        bf = BeautifulSoup(html, features="html.parser")
        texts = bf.find_all('div', class_='showtxt')
        texts = texts[0].text.replace('\xa0' * 8, '\n\n')
        return texts

    """
    函数说明:将爬取的文章内容写入文件
    Parameters:
        name - 章节名称(string)
        path - 当前路径下,小说保存名称(string)
        text - 章节内容(string)
    Returns:
        无
    Modify:
        2017-09-13
    """

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == "__main__":
    # dl = downloader()
    # dl.get_download_url()
    # print('《一年永恒》开始下载：')
    # for i in range(dl.nums):
    #     dl.writer(dl.names[i], 'D:/一念永恒.txt', dl.get_contents(dl.urls[i]))
    #     sys.stdout.write("  已下载:%.3f%%" % float(i / dl.nums) + '\r')
    #     sys.stdout.flush()
    # print('《一年永恒》下载完成')

    server = 'http://www.biqukan.com/'
    target = 'http://www.biqukan.com/1_1094/'
    req = requests.get(url=target)
    # req.encoding = 'utf-8'
    # html = req.text
    html = req.content
    # html_doc = str(html, 'utf-8')
    print(html)
    div_bf = BeautifulSoup(html, features="html.parser")
    div = div_bf.find_all('div', class_='listmain')
    a_bf = BeautifulSoup(str(div[0]), features="html.parser")
    a = a_bf.find_all('a')
    for each in a[16:20]:
        print(each.string, server + each.get('href'))
'''
L[0:3],L[:3] 截取前3个元素。
L[1:3] 从1开始截取2个元素出来。
L[-1] 取倒数第一个元素出来。
L[-10] 取后10个数
L[10:20] 取前11-20个数
L[:10:2] 取前10个数，每两个取一个
L[::5] 所有数，每5个取一个
L[:] 原样复制一个list
tuple,字符串也可以进行切片操作
'''

