import scrapy
import pandas as pd
from yScrape.items import stockItem
tickers = pd.read_csv("D:\\Downloads\\nasdaq_screener_1723022708864.csv")
class YscraperSpider(scrapy.Spider):
    name = "yScraper"
    allowed_domains = ["finance.yahoo.com"]
    start_urls = ["https://finance.yahoo.com/quote"]
    def parse(self, response):
        #tickers = pd.read_csv("D:\\Downloads\\nasdaq_screener_1723022708864.csv")
        global tickerName
        for i in tickers['Symbol']:

            stockURL = 'https://finance.yahoo.com/quote/' + str(i) + '/analysis/'

            tickerName = i
            # else:
            #     bookURL = 'https://books.toscrape.com/catalogue/' + relativeURL
            yield response.follow(stockURL, callback=self.parseStockPage, meta={
                'tickerName': i,
                "proxy": "http://scrapeops:12c6c1f6-3283-4cf3-a7ab-344f652ae005@residential-proxy.scrapeops.io:8181"})

        # nPage = response.css('li.next a ::attr(href)').get()
        # if nPage is not None:
        #     if 'catalogue/' in nPage:
        #         nPageURL = 'https://books.toscrape.com/' + nPage
        #     else:
        #         nPageURL = 'https://books.toscrape.com/catalogue/' + nPage
        #     yield response.follow(nPageURL, callback=self.parse, meta={
        #         "proxy": "http://scrapeops:12c6c1f6-3283-4cf3-a7ab-344f652ae005@residential-proxy.scrapeops.io:8181"})


    def parseStockPage(self, response):
        tickerName = response.meta['tickerName']


        table = response.css("table .yf-17yshpm")
        tRows = table.css("tr")
        NoAnlst = tRows[1].css("td")
        AvgEst = tRows[2].css("td")
        LowEst = tRows[3].css("td")
        HighEst = tRows[4].css("td")
        YearAgoEPS = tRows[5].css("td")

        stock_item = stockItem()
        stock_item['tickerName'] = tickerName

        stock_item['cQtrNoAnlst'] = NoAnlst[1].css("td::text").get()
        stock_item['cQtrAvgEst'] = AvgEst[1].css("td::text").get()
        stock_item['cQtrLowEst'] = LowEst[1].css('td ::text').get()
        stock_item['cQtrHighEst'] = HighEst[1].css('td ::text').get()
        stock_item['cQtrYearAgoEPS'] = YearAgoEPS[1].css('td ::text').get()

        stock_item['nQtrNoAnlst'] = NoAnlst[2].css('td ::text').get()
        stock_item['nQtrAvgEst'] = AvgEst[2].css('td ::text').get()
        stock_item['nQtrLowEst'] = LowEst[2].css('td ::text').get()
        stock_item['nQtrHighEst'] = HighEst[2].css("td::text").get()
        stock_item['nQtrYearAgoEPS'] = YearAgoEPS[2].css("td::text").get()

        stock_item['cYearNoAnlst'] = NoAnlst[3].css("td::text").get()
        stock_item['cYearAvgEst'] = AvgEst[3].css('td ::text').get()
        stock_item['cYearLowEst'] = LowEst[3].css('td ::text').get()
        stock_item['cYearHighEst'] = HighEst[3].css('td ::text').get()
        stock_item['cYearYearAgoEPS'] = YearAgoEPS[3].css('td ::text').get()

        stock_item['nYearNoAnlst'] = NoAnlst[4].css('td ::text').get()
        stock_item['nYearAvgEst'] = AvgEst[4].css('td ::text').get()
        stock_item['nYearLowEst'] = LowEst[4].css("td::text").get()
        stock_item['nYearHighEst'] = HighEst[4].css('td ::text').get()
        stock_item['nYearYearAgoEPS'] = YearAgoEPS[4].css('td ::text').get()

        yield stock_item


