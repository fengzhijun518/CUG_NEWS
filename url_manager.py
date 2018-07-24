class UrlManager:
    'url管理类'

    # 构造函数初始化set集合
    def __init__(self):
        self.new_urls = set()  # 待爬取的url
        self.old_urls = set()  # 已爬取的url

    # 向管理器中添加一个新的url
    def add_new_url(self, root_url):
        if (root_url is None):
            return
        if (root_url not in self.new_urls and root_url not in self.old_urls):
            # 既不在待爬取的url也不在已爬取的url中，是一个全新的url，因此将其添加到new_urls
            self.new_urls.add(root_url)

            # 向管理器中添加批量新的url

    def add_new_urls(self, urls):
        if (urls is None or len(urls) == 0):
            return
        for url in urls:
            self.add_new_url(url)  # 调用add_new_url()

    # 判断是否有新的待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0
        # 获取一个待爬取的url

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url