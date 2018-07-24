from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

htmlEmt = etree.HTML(text)
result = etree.tostring(htmlEmt)
# print(result.decode('utf-8'))


# 获取所有的li标签
result = htmlEmt.xpath('//li')
print(result)


# 获取li标签下的所有class
result = htmlEmt.xpath('//li/@class')
print(result)

# 获取li标签下href为 link1的a标签
result = htmlEmt.xpath('//li/a[@href="link1.html"]')
print(result[0])
print(result[0].text)
# 获取所有的href
# result = htmlEmt.xpath('//li/a[@href]')
# print(result)
# for item in result:
#     print(item.text)
#

result = htmlEmt.xpath('//li//span')
print(result[0])
print(result[0].text)

result = htmlEmt.xpath('//li/a//@class')
print(result)

# 输出最后一个
result = htmlEmt.xpath('//li[last()]/a/@href')
print(result)

# 获取class为bold的标签名
result = htmlEmt.xpath('//*[@class="bold"]')
print(result[0].tag)
print(result[0].text)






# 如果text是一个文件的话这样读取
# htmlEmt = etree.parse(text.xml)
#
# result = etree.tostring(htmlEmt, pretty_print=True)
# print(result)