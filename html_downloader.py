# <span style="font-size:12px;">
from urllib import request  
from urllib.parse import quote
import string
class HtmlDownLoader:
    '下载页面内容'
    def downloade(self,new_url):
        if(new_url is None):
            return None
        #解决请求路径中含义中文或特殊字符
        url_ = quote(new_url, safe=string.printable);
        response = request.urlopen(url_)
        if(response.getcode()!=200):
            return None #请求失败
        html = response.read()
        return html.decode("utf8")