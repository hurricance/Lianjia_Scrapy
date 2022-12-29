import scrapy
import re
from scrapy.http import Request
from rent.items import RentItem

class BjFirstSpider(scrapy.Spider):
    name = "BjFirstSpider"
    allowed_domains = ["bj.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://bj.lianjia.com/zufang/erp3800/"] # 起始网址
    pagenum = 1 # 用于翻页
    def parse(self, response):
        self.pagenum += 1 
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div'):
            #用xpath来解析html，div标签中的数据，就是我们需要的数据。
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0] # 使用正则表达式, 提取里面的数字
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            s1 = s1.rstrip().split()[-1] # 用于获取房型信息
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

        if self.pagenum <= 96: 
            url = f"https://bj.lianjia.com/zufang/pg{self.pagenum}erp3800/#contentList/" #下一页的地址
            url = response.urljoin(url)
            yield Request(url, callback=self.parse) # 对下一页发出请求, 并使用parse函数对响应进行处理

class BjSecondSpider(scrapy.Spider):
    name = "BjSecondSpider"
    allowed_domains = ["bj.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://bj.lianjia.com/zufang/brp3801erp4500/"]
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

        if self.pagenum <= 88:
            url = f"https://bj.lianjia.com/zufang/pg{self.pagenum}brp3801erp4500/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class BjThirdSpider(scrapy.Spider):
    name = "BjThirdSpider"
    allowed_domains = ["bj.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://bj.lianjia.com/zufang/brp4501erp5100/"]
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

        if self.pagenum <= 84:
            url = f"https://bj.lianjia.com/zufang/pg{self.pagenum}brp4501erp5100/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class BjFourthSpider(scrapy.Spider):
    name = "BjFourthSpider"
    allowed_domains = ["bj.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://bj.lianjia.com/zufang/brp5101erp5600/"]
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

        if self.pagenum <= 97:
            url = f"https://bj.lianjia.com/zufang/pg{self.pagenum}brp5101erp5600/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class BjFifthSpider(scrapy.Spider):
    name = "BjFifthSpider"
    allowed_domains = ["bj.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://bj.lianjia.com/zufang/brp5601erp6100/"]
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
            url = f"https://bj.lianjia.com/zufang/pg{self.pagenum}brp5601erp6100/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class BjSixthSpider(scrapy.Spider):
    name = "BjSixthSpider"
    allowed_domains = ["bj.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://bj.lianjia.com/zufang/brp6101erp6600/"]
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

        if self.pagenum <= 100:
            url = f"https://bj.lianjia.com/zufang/pg{self.pagenum}brp6101erp6600/#contentList/"
            url = response.urljoin(url)                         
            yield Request(url, callback=self.parse)

class BjSeventhSpider(scrapy.Spider):
    name = "BjSeventhSpider"
    allowed_domains = ["bj.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://bj.lianjia.com/zufang/brp6601erp7200/"]
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

        if self.pagenum <= 91:
            url = f"https://bj.lianjia.com/zufang/pg{self.pagenum}brp6601erp7200/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class BjEighthSpider(scrapy.Spider):
    name = "BjEighthSpider"
    allowed_domains = ["bj.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://bj.lianjia.com/zufang/brp7201erp7900/"]
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

        if self.pagenum <= 82:
            url = f"https://bj.lianjia.com/zufang/pg{self.pagenum}brp7201erp7900/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class BjNinthSpider(scrapy.Spider):
    name = "BjNinthSpider"
    allowed_domains = ["bj.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://bj.lianjia.com/zufang/brp7901erp8900/"]
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

        if self.pagenum <= 86:
            url = f"https://bj.lianjia.com/zufang/pg{self.pagenum}brp7901erp8900/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class BjTenthSpider(scrapy.Spider):
    name = "BjTenthSpider"
    allowed_domains = ["bj.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://bj.lianjia.com/zufang/brp8901erp11000/"]
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
            url = f"https://bj.lianjia.com/zufang/pg{self.pagenum}brp8901erp11000/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class BjEleventhSpider(scrapy.Spider):
    name = "BjEleventhSpider"
    allowed_domains = ["bj.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://bj.lianjia.com/zufang/brp11001erp16000/"]
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
            url = f"https://bj.lianjia.com/zufang/pg{self.pagenum}brp11001erp16000/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class BjTwelfthSpider(scrapy.Spider):
    name = "BjTwelfthSpider"
    allowed_domains = ["bj.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://bj.lianjia.com/zufang/brp16001/"]
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
            url = f"https://bj.lianjia.com/zufang/pg{self.pagenum}brp16001/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)
