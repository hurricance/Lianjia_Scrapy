import scrapy
import re
from scrapy.http import Request
from rent.items import RentItem

class Template(scrapy.Spider):
    name = "Template"
    allowed_domains = ["sz.lianjia.com"] #允许爬取的网站域名
    start_urls = ["https://gz.lianjia.com/zufang/erp1300/"]
    pagenum = 1

    def handle(self, response):
        if self.pagenum <= 71:
            url = f"https://sz.lianjia.com/zufang/pg{self.pagenum}erp1300/#contentList/"
            url = response.urljoin(url)
            return Request(url, callback=self.parse)

    def parse(self, response): #解析爬取的内容
        self.pagenum += 1
        item = RentItem() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div[1]/div[*]'):
            test = each.xpath('a[1]/p/text()').extract_first()
            if test != None:
                continue
            test = each.xpath('a[2]/p/text()').extract_first()
            if test != None:
                continue
            s1 = each.xpath('div/p[2]/text()[7]').extract_first()
            if s1 == None:
                continue
            s1 = s1.strip()
            temp = each.xpath('div/p[1]/a/text()').extract_first().strip().split()
            s = each.xpath('div/p[2]/text()[5]').extract_first()
            s = re.findall(r"\d+\.?\d*",s)[0]
            s2 = each.xpath('div/p[2]/text()[6]').extract_first().strip()
            item['区域'] = each.xpath('div/p[2]/a[1]/text()').extract_first()
            item['名称'] = temp[0][3:]
            item['房型'] = s1
            item['面积'] = s
            item['月租'] = each.xpath('div/span/em/text()').extract_first()
            item['板块名称'] = each.xpath('div/p[2]/a[2]/text()').extract_first()
            item['房子朝向'] = s2
            item['租赁方式'] = temp[0][0:2]
            yield(item) #返回item数据给到pipelines模块
        yield self.handle(response)
        