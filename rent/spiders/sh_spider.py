import scrapy
import re
from scrapy.http import Request
from rent.items import RentItem

class ShFirstSpider(scrapy.Spider):
    name = "ShFirstSpider"
    allowed_domains = ["sh.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sh.lianjia.com/zufang/erp3500/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0]
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            s1 = s1.rstrip().split()[-1]
            s2 = each.xpath('div/p[2]/text()[6]').extract_first()
            s2 = s2.strip()
            item['区域'] = each.xpath('div/p[2]/a[1]/text()').extract_first()
            item['名称'] = temp[0][3:]
            item['房型'] = s1
            item['面积'] = s
            item['月租'] = each.xpath('div/span/em/text()').extract_first()
            item['板块名称'] = each.xpath('div/p[2]/a[2]/text()').extract_first()
            item['房子朝向'] = s2
            item['租赁方式'] = temp[0][0:2]
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum <= 95:
            url = f"https://sh.lianjia.com/zufang/pg{self.pagenum}erp3500/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class ShSecondSpider(scrapy.Spider):
    name = "ShSecondSpider"
    allowed_domains = ["sh.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sh.lianjia.com/zufang/brp3501erp4200/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0]
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            s1 = s1.rstrip().split()[-1]
            s2 = each.xpath('div/p[2]/text()[6]').extract_first()
            s2 = s2.strip()
            item['区域'] = each.xpath('div/p[2]/a[1]/text()').extract_first()
            item['名称'] = temp[0][3:]
            item['房型'] = s1
            item['面积'] = s
            item['月租'] = each.xpath('div/span/em/text()').extract_first()
            item['板块名称'] = each.xpath('div/p[2]/a[2]/text()').extract_first()
            item['房子朝向'] = s2
            item['租赁方式'] = temp[0][0:2]
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum <= 99:
            url = f"https://sh.lianjia.com/zufang/pg{self.pagenum}brp3501erp4200/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class ShThirdSpider(scrapy.Spider):
    name = "ShThirdSpider"
    allowed_domains = ["sh.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sh.lianjia.com/zufang/brp4201erp4700/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0]
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            s1 = s1.rstrip().split()[-1]
            s2 = each.xpath('div/p[2]/text()[6]').extract_first()
            s2 = s2.strip()
            item['区域'] = each.xpath('div/p[2]/a[1]/text()').extract_first()
            item['名称'] = temp[0][3:]
            item['房型'] = s1
            item['面积'] = s
            item['月租'] = each.xpath('div/span/em/text()').extract_first()
            item['板块名称'] = each.xpath('div/p[2]/a[2]/text()').extract_first()
            item['房子朝向'] = s2
            item['租赁方式'] = temp[0][0:2]
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum <= 87:
            url = f"https://sh.lianjia.com/zufang/pg{self.pagenum}brp4201erp4700/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class ShFourthSpider(scrapy.Spider):
    name = "ShFourthSpider"
    allowed_domains = ["sh.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sh.lianjia.com/zufang/brp4701erp5100/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0]
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            s1 = s1.rstrip().split()[-1]
            s2 = each.xpath('div/p[2]/text()[6]').extract_first()
            s2 = s2.strip()
            item['区域'] = each.xpath('div/p[2]/a[1]/text()').extract_first()
            item['名称'] = temp[0][3:]
            item['房型'] = s1
            item['面积'] = s
            item['月租'] = each.xpath('div/span/em/text()').extract_first()
            item['板块名称'] = each.xpath('div/p[2]/a[2]/text()').extract_first()
            item['房子朝向'] = s2
            item['租赁方式'] = temp[0][0:2]
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum <= 77:
            url = f"https://sh.lianjia.com/zufang/pg{self.pagenum}brp4701erp5100/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class ShFifthSpider(scrapy.Spider):
    name = "ShFifthSpider"
    allowed_domains = ["sh.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sh.lianjia.com/zufang/brp5101erp5500/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0]
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            s1 = s1.rstrip().split()[-1]
            s2 = each.xpath('div/p[2]/text()[6]').extract_first()
            s2 = s2.strip()
            item['区域'] = each.xpath('div/p[2]/a[1]/text()').extract_first()
            item['名称'] = temp[0][3:]
            item['房型'] = s1
            item['面积'] = s
            item['月租'] = each.xpath('div/span/em/text()').extract_first()
            item['板块名称'] = each.xpath('div/p[2]/a[2]/text()').extract_first()
            item['房子朝向'] = s2
            item['租赁方式'] = temp[0][0:2]
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum <= 90:
            url = f"https://sh.lianjia.com/zufang/pg{self.pagenum}brp5101erp5500/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class ShSixthSpider(scrapy.Spider):
    name = "ShSixthSpider"
    allowed_domains = ["sh.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sh.lianjia.com/zufang/brp5501erp6100/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0]
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            s1 = s1.rstrip().split()[-1]
            s2 = each.xpath('div/p[2]/text()[6]').extract_first()
            s2 = s2.strip()
            item['区域'] = each.xpath('div/p[2]/a[1]/text()').extract_first()
            item['名称'] = temp[0][3:]
            item['房型'] = s1
            item['面积'] = s
            item['月租'] = each.xpath('div/span/em/text()').extract_first()
            item['板块名称'] = each.xpath('div/p[2]/a[2]/text()').extract_first()
            item['房子朝向'] = s2
            item['租赁方式'] = temp[0][0:2]
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum <= 89:
            url = f"https://sh.lianjia.com/zufang/pg{self.pagenum}brp5501erp6100/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class ShSeventhSpider(scrapy.Spider):
    name = "ShSeventhSpider"
    allowed_domains = ["sh.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sh.lianjia.com/zufang/brp6101erp6800/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0]
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            s1 = s1.rstrip().split()[-1]
            s2 = each.xpath('div/p[2]/text()[6]').extract_first()
            s2 = s2.strip()
            item['区域'] = each.xpath('div/p[2]/a[1]/text()').extract_first()
            item['名称'] = temp[0][3:]
            item['房型'] = s1
            item['面积'] = s
            item['月租'] = each.xpath('div/span/em/text()').extract_first()
            item['板块名称'] = each.xpath('div/p[2]/a[2]/text()').extract_first()
            item['房子朝向'] = s2
            item['租赁方式'] = temp[0][0:2]
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum <= 98:
            url = f"https://sh.lianjia.com/zufang/pg{self.pagenum}brp6101erp6800/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class ShEighthSpider(scrapy.Spider):
    name = "ShEighthSpider"
    allowed_domains = ["sh.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sh.lianjia.com/zufang/brp6801erp7900/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0]
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            s1 = s1.rstrip().split()[-1]
            s2 = each.xpath('div/p[2]/text()[6]').extract_first()
            s2 = s2.strip()
            item['区域'] = each.xpath('div/p[2]/a[1]/text()').extract_first()
            item['名称'] = temp[0][3:]
            item['房型'] = s1
            item['面积'] = s
            item['月租'] = each.xpath('div/span/em/text()').extract_first()
            item['板块名称'] = each.xpath('div/p[2]/a[2]/text()').extract_first()
            item['房子朝向'] = s2
            item['租赁方式'] = temp[0][0:2]
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum <= 93:
            url = f"https://sh.lianjia.com/zufang/pg{self.pagenum}brp6801erp7900/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class ShNinthSpider(scrapy.Spider):
    name = "ShNinthSpider"
    allowed_domains = ["sh.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sh.lianjia.com/zufang/brp7901erp9900/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0]
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            s1 = s1.rstrip().split()[-1]
            s2 = each.xpath('div/p[2]/text()[6]').extract_first()
            s2 = s2.strip()
            item['区域'] = each.xpath('div/p[2]/a[1]/text()').extract_first()
            item['名称'] = temp[0][3:]
            item['房型'] = s1
            item['面积'] = s
            item['月租'] = each.xpath('div/span/em/text()').extract_first()
            item['板块名称'] = each.xpath('div/p[2]/a[2]/text()').extract_first()
            item['房子朝向'] = s2
            item['租赁方式'] = temp[0][0:2]
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum <= 98:
            url = f"https://sh.lianjia.com/zufang/pg{self.pagenum}brp7901erp9900/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class ShTenthSpider(scrapy.Spider):
    name = "ShTenthSpider"
    allowed_domains = ["sh.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sh.lianjia.com/zufang/brp9901erp14500/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0]
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            s1 = s1.rstrip().split()[-1]
            s2 = each.xpath('div/p[2]/text()[6]').extract_first()
            s2 = s2.strip()
            item['区域'] = each.xpath('div/p[2]/a[1]/text()').extract_first()
            item['名称'] = temp[0][3:]
            item['房型'] = s1
            item['面积'] = s
            item['月租'] = each.xpath('div/span/em/text()').extract_first()
            item['板块名称'] = each.xpath('div/p[2]/a[2]/text()').extract_first()
            item['房子朝向'] = s2
            item['租赁方式'] = temp[0][0:2]
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum <= 99:
            url = f"https://sh.lianjia.com/zufang/pg{self.pagenum}brp9901erp14500/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class ShEleventhSpider(scrapy.Spider):
    name = "ShEleventhSpider"
    allowed_domains = ["sh.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sh.lianjia.com/zufang/brp14501erp20000/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0]
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            s1 = s1.rstrip().split()[-1]
            s2 = each.xpath('div/p[2]/text()[6]').extract_first()
            s2 = s2.strip()
            item['区域'] = each.xpath('div/p[2]/a[1]/text()').extract_first()
            item['名称'] = temp[0][3:]
            item['房型'] = s1
            item['面积'] = s
            item['月租'] = each.xpath('div/span/em/text()').extract_first()
            item['板块名称'] = each.xpath('div/p[2]/a[2]/text()').extract_first()
            item['房子朝向'] = s2
            item['租赁方式'] = temp[0][0:2]
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum <= 52:
            url = f"https://sh.lianjia.com/zufang/pg{self.pagenum}brp14501erp20000/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class ShTwelfthSpider(scrapy.Spider):
    name = "ShTwelfthSpider"
    allowed_domains = ["sh.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://sh.lianjia.com/zufang/brp20001/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0]
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            s1 = s1.rstrip().split()[-1]
            s2 = each.xpath('div/p[2]/text()[6]').extract_first()
            s2 = s2.strip()
            item['区域'] = each.xpath('div/p[2]/a[1]/text()').extract_first()
            item['名称'] = temp[0][3:]
            item['房型'] = s1
            item['面积'] = s
            item['月租'] = each.xpath('div/span/em/text()').extract_first()
            item['板块名称'] = each.xpath('div/p[2]/a[2]/text()').extract_first()
            item['房子朝向'] = s2
            item['租赁方式'] = temp[0][0:2]
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum <= 54:
            url = f"https://sh.lianjia.com/zufang/pg{self.pagenum}brp20001/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)
