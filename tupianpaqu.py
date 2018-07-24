from lxml import etree
import requests
import os


url = 'https://www.gexing.com/shaitu/221945.html'
r = requests.get(url)
r.encoding = 'utf-8'
# print(r.status_code)
s = etree.HTML(r.text)
result = s.xpath('//div/a/img/@src')

# 新建文件夹 并移动到文件夹内
os.mkdir("img")
os.chdir("img")


# 请求头， 图片不能直接访问网址，在图片文件中先检查元素分析refer需求

headers = {
    "Referer": "https://www.gexing.com/shaitu/221945.html"
}

for i in range(len(result)):
    # 剔除奇怪的网址， 不然请求不了
    if result[i][-3:] == 'jpg':
        r_img = requests.get(result[i], headers=headers)
        print(r_img.status_code)
        # 通过二进制将内容保存下来
        print(result[i][-3:])
        with open("img" + str(i+1) + ".jpg", "wb") as f:
            # 注意图片格式的内容提取用.content
            f.write(r_img.content)
