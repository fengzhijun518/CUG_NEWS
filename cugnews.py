from lxml import etree
import requests

def cugspider(url):
    r = requests.get(url)
    r.encoding = "utf-8"

    htm = etree.HTML(r.text)
    result = htm.xpath('//li[@class="list_item"]/a')
    href = htm.xpath('//li[@class="list_item"]/a/@href')
    for item, hre in zip(result, href):
        #打印目前爬取的页面内容
        print(item.text)
        print("http://www.cug.edu.cn/" + hre[6:])

        # 保存新闻名字和网址
        with open(r'cug_news.txt', 'a') as file:
            file.write('新闻：\t')
            file.write(item.text)
            file.write('\n')
            file.write('网址：\t')
            file.write("http://www.cug.edu.cn/" + hre[6:])
            file.write('\n')
        download_news("http://www.cug.edu.cn/" + hre[6:])

def download_news(url):
    r = requests.get(url)
    r.encoding = "utf-8"
    with open(url[-9:-4] + '.txt', 'a', encoding='utf-8') as file:
        htm = etree.HTML(r.text)
        result = htm.xpath('//div/h1')
        for item in result:
            file.write(item.text)
            # print(item.text)
        result2 = htm.xpath('//div/p/span')
        for item1 in result2:
            if item1.text != None:
                file.write(item1.text)
                # print(item1.text)
        result3 = htm.xpath('//div/p')
        for item in result3:
            if item.text != None:
                file.write(item.text)
                # print(item.text)

url_list = []
url = 'http://www.cug.edu.cn/index/ddyw.htm'
for i in range(1,173):
    url = 'http://www.cug.edu.cn/index/ddyw/' + str(i) + '.htm'
    url_list.append(url)
for item in url_list:
    cugspider(item)
