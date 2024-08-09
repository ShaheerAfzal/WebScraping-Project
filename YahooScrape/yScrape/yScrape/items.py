# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class stockItem(scrapy.Item):
    tickerName = scrapy.Field()

    cQtrNoAnlst = scrapy.Field()
    cQtrAvgEst = scrapy.Field()
    cQtrLowEst = scrapy.Field()
    cQtrHighEst = scrapy.Field()
    cQtrYearAgoEPS = scrapy.Field()

    nQtrNoAnlst = scrapy.Field()
    nQtrAvgEst = scrapy.Field()
    nQtrLowEst = scrapy.Field()
    nQtrHighEst = scrapy.Field()
    nQtrYearAgoEPS = scrapy.Field()

    cYearNoAnlst = scrapy.Field()
    cYearAvgEst = scrapy.Field()
    cYearLowEst = scrapy.Field()
    cYearHighEst = scrapy.Field()
    cYearYearAgoEPS = scrapy.Field()

    nYearNoAnlst = scrapy.Field()
    nYearAvgEst = scrapy.Field()
    nYearLowEst = scrapy.Field()
    nYearHighEst = scrapy.Field()
    nYearYearAgoEPS = scrapy.Field()


