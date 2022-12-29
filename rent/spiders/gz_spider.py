import scrapy
import re
from scrapy.http import Request
from rent.items import RentItem

class GzFirstSpider(scrapy.Spider):
    name = "GzFirstSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/erp1200/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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

        if self.pagenum <= 76:
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}erp1200/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzSecondSpider(scrapy.Spider):
    name = "GzSecondSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp1201erp1400/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp1201erp1400/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzThirdSpider(scrapy.Spider):
    name = "GzThirdSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp1401erp1500/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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

        if self.pagenum <= 69:
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp1401erp1500/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzFourthSpider(scrapy.Spider):
    name = "GzFourthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp1501erp1700/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp1501erp1700/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzFifthSpider(scrapy.Spider):
    name = "GzFifthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp1701erp1800/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp1701erp1800/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzSixthSpider(scrapy.Spider):
    name = "GzSixthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp1801erp1999/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容                          
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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

        if self.pagenum <= 36:
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp1801erp1999/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzSeventhSpider(scrapy.Spider):
    name = "GzSeventhSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp2000erp2000/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp2000erp2000/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzEighthSpider(scrapy.Spider):
    name = "GzEighthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp2001erp2199/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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

        if self.pagenum <= 64:
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp2001erp2199/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzNinthSpider(scrapy.Spider):
    name = "GzNinthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp2200erp2299/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp2200erp2299/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzTenthSpider(scrapy.Spider):
    name = "GzTenthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp2300erp2399/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp2300erp2399/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzEleventhSpider(scrapy.Spider):
    name = "GzEleventhSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp2400erp2499/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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

        if self.pagenum <= 41:
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp2400erp2499/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzTwelfthSpider(scrapy.Spider):
    name = "GzTwelfthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp2500erp2500/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp2500erp2500/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzThirteenthSpider(scrapy.Spider):
    name = "GzThirteenthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp2501erp2600/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp2501erp2600/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzFourteenthSpider(scrapy.Spider):
    name = "GzFourteenthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp2601erp2799/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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

        if self.pagenum <= 56:
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp2601erp2799/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzFifteenthSpider(scrapy.Spider):
    name = "GzFifteenthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp2800erp2899/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp2800erp2899/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzSixteenthSpider(scrapy.Spider):
    name = "GzSixteenthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp2900erp2999/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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

        if self.pagenum <= 37:
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp2900erp2999/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzSeventeenthSpider(scrapy.Spider):
    name = "GzSeventeenthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp3000erp3000/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp3000erp3000/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzEighteenthSpider(scrapy.Spider):
    name = "GzEighteenthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp3001erp3200/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp3001erp3200/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzNinteenthSpider(scrapy.Spider):
    name = "GzNinteenthSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp3201erp3499/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp3201erp3499/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GzTwentiethSpider(scrapy.Spider):
    name = "GzTwentiethSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp3500erp3500/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp3500erp3500/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class Gz21thSpider(scrapy.Spider):
    name = "Gz21thSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp3501erp3799/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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

        if self.pagenum <= 85:
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp3501erp3799/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class Gz22thSpider(scrapy.Spider):
    name = "Gz22thSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp3800erp3900/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp3800erp3900/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class Gz23thSpider(scrapy.Spider):
    name = "Gz23thSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp3901erp4000/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp3901erp4000/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class Gz24thSpider(scrapy.Spider):
    name = "Gz24thSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp4001erp4300/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp4001erp4300/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class Gz25thSpider(scrapy.Spider):
    name = "Gz25thSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp4301erp4500/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp4301erp4500/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class Gz26thSpider(scrapy.Spider):
    name = "Gz26thSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp4501erp4900/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp4501erp4900/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class Gz27thSpider(scrapy.Spider):
    name = "Gz27thSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp4901erp5100/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp4901erp5100/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class Gz28thSpider(scrapy.Spider):
    name = "Gz28thSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp5101erp5500/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp5101erp5500/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class Gz29thSpider(scrapy.Spider):
    name = "Gz29thSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp5501erp6000/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp5501erp6000/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class Gz30thSpider(scrapy.Spider):
    name = "Gz30thSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp6001erp6900/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp6001erp6900/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class Gz31thSpider(scrapy.Spider):
    name = "Gz31thSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp6901erp8200/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp6901erp8200/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class Gz32thSpider(scrapy.Spider):
    name = "Gz32thSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp8201erp12000/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp8201erp12000/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class Gz33thSpider(scrapy.Spider):
    name = "Gz33thSpider"
    allowed_domains = ["gz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/brp12001/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()   
            if s1 == None:         
                continue
            s1 = s1.rstrip().split()[-1]
            temp = each.xpath('div/p[1]/a/text()').extract_first().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first().strip()
            if s == '':
                continue
            s = re.findall(r"\d+\.?\d*",s)[0]
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
            url = f"https://gz.lianjia.com/zufang/pg{self.pagenum}brp12001/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)
