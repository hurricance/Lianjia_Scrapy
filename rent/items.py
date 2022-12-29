# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    面积 = scrapy.Field() # 面积
    房型 = scrapy.Field() # 房型
    月租 = scrapy.Field() # 价格
    租赁方式 = scrapy.Field() # 租赁方式
    板块名称 = scrapy.Field() # 板块名称
    房子朝向 = scrapy.Field() # 房间朝向
    名称 = scrapy.Field() # 名称
    区域 = scrapy.Field() # 区域
