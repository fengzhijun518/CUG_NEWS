from lxml import etree
import requests


def zhongtu(url, depth_control):
    depth_control += 1
    r = requests.get(url)
    # print(r.status_code)

    r.encoding = "utf-8"

    s = etree.HTML(r.text)

    result1 = s.xpath('//li/a')
    result2 = s.xpath('//li/span')
    result3 = s.xpath('//li/a/@href')
    for item, i, href in zip(result1, result2, result3):
        print(i.text, item.text, href)
        with open('zhongtu.txt', 'a', encoding='utf-8') as file:
            for it in range(depth_control):
                file.write('    ')
            file.write(i.text + ' ' + item.text)
            # file.write('\t' + item.text)
            # file.write(href)
            file.write('\n')
        zhongtu(href, depth_control)


if __name__ == '__main__':
    url = 'http://www.ztflh.com/?c=17417'
    zhongtu(url, 1)
