from bs4 import BeautifulSoup
import re
from urllib import parse


class HtmlParser:
    # page_url 基本url 需拼接部分
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 匹配 /item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6
        links = soup.find_all('a', href=re.compile(r'/item/\w+'))
        for link in links:
            new_url = link["href"]
            # 例如page_url=http://baike.baidu.com/item/Python new_url=/item/史记·2016?fr=navbar
            # 则使用parse.urljoin(page_url,new_url)后 new_full_url = http://baike.baidu.com/item/史记·2016?fr=navbar
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        red_data = {}
        red_data['url'] = page_url
        # title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')  # 获取标题内容
        # red_data['title'] = title_node.get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="dataItem")
        red_data['summary'] = summary_node.get_text()
        return red_data

        # new_url路径 html_context界面内容

    def parse(self, page_url, html_context):
        if (page_url is None or html_context is None):
            return
            # python3缺省的编码是unicode, 再在from_encoding设置为utf8, 会被忽视掉，去掉【from_encoding = "utf-8"】这一个好了
        soup = BeautifulSoup(html_context, "html.parser")
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data