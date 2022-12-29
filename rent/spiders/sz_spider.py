from scrapy.http import Request
from rent.spiders.template import Template

class Sz1stSpider(Template):
    name = "Sz1stSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/erp1300/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 71:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}erp1300/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz2ndSpider(Template):
    name = "Sz2ndSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp1301erp1399/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 100:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp1301erp1399/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz3rdSpider(Template):
    name = "Sz3rdSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp1400erp1500/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 91:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp1400erp1500/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz4thSpider(Template):
    name = "Sz4thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp1501erp1600/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 98:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp1501erp1600/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz5thSpider(Template):
    name = "Sz5thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp1601erp1799/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 100:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp1601erp1799/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz6thSpider(Template):
    name = "Sz6thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp1800erp1999/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 98:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp1800erp1999/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz7thSpider(Template):
    name = "Sz7thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp2000erp2200/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 100:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp2000erp2200/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz8thSpider(Template):
    name = "Sz8thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp2201erp2500/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 98:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp2201erp2500/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz9thSpider(Template):
    name = "Sz9thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp2501erp2800/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 100:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp2501erp2800/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz10thSpider(Template):
    name = "Sz10thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp2801erp3400/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 100:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp2801erp3400/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz11thSpider(Template):
    name = "Sz11thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp3401erp3900/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 100:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp3401erp3900/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz12thSpider(Template):
    name = "Sz12thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp3901erp4400/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 100:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp3901erp4400/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz13thSpider(Template):
    name = "Sz13thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp4401erp4999/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 100:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp4401erp4999/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz14thSpider(Template):
    name = "Sz14thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp5000erp5400/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 100:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp5000erp5400/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz15thSpider(Template):
    name = "Sz15thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp5401erp5999/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 100:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp5401erp5999/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz16thSpider(Template):
    name = "Sz16thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp6000erp6499/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 79:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp6000erp6499/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz17thSpider(Template):
    name = "Sz17thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp6500erp6999/"]
    pagenum = 1

    def handle(self, response):     
        if self.pagenum <= 85:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp6500erp6999/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz18thSpider(Template):
    name = "Sz18thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp7000erp7700/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 100:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp7000erp7700/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz19thSpider(Template):
    name = "Sz19thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp7701erp8999/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 100:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp7701erp8999/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz20thSpider(Template):
    name = "Sz20thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp9000erp11000/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 98:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp9000erp11000/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz21thSpider(Template):
    name = "Sz21thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp11001erp18000/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 100:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp11001erp18000/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

class Sz22thSpider(Template):
    name = "Sz22thSpider"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sz.lianjia.com/zufang/brp18001/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 71:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}brp18001/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)
