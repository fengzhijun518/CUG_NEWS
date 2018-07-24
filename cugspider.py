import requests
from lxml import etree

from pyquery import PyQuery

r = requests.get("http://www.cug.edu.cn")
r.encoding = "utf-8"
# print(r.status_code)
htm = etree.HTML(r.text)
# result = htm.xpath('//li/a/@href')
# result1 = htm.xpath('//li/a')
# for item, item1 in zip(result, result1):
#     print(item)
#     print(item1.text)

# result3 = htm.xpath('//li/a[@target="_blank"]')
# for item in result3:
#     print(item.text)

# result3 = htm.xpath('//li/a/@target')
# for item in result3:
#     print(item)

# result3 = htm.xpath('//li/@class')
# for item in result3:
#     print(item)

# result3 = htm.xpath('//div/@id')
# for item in result3:
#     print(item)


# jpy = PyQuery(r.text)
# a_list = jpy("ul.navList > li:nth-child(1) a")
# for item in a_list:
#     print(item.text)

result4 = htm.xpath('//li/a/@href')
for item in result4:
    print(item[4:])
# result4 = htm.xpath('//li[@class="l11"]/a/text()')
# print(result4)