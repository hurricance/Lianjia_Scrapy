import scrapy
import re
from scrapy.http import Request
from rent.items import RentItem

class GlFirstSpider(scrapy.Spider):
    name = "GlFirstSpider"
    allowed_domains = ["gl.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gl.lianjia.com/zufang/erp1400/"]
    pagenum = 1
    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
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
            url = f"https://gl.lianjia.com/zufang/pg{self.pagenum}erp1400/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)

class GlSecondSpider(scrapy.Spider):
    name = "GlSecondSpider"
    allowed_domains = ["gl.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gl.lianjia.com/zufang/brp1401/"]
    pagenum = 1

    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('//*[@id="content"]/div[1]/div[1]/div'):
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
            url = f"https://gl.lianjia.com/zufang/pg{self.pagenum}brp1401/#contentList/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)