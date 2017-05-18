# -*- coding: utf-8 -*-
import scrapy
import re


class AmazonSpider(scrapy.Spider):
    name = 'amazonSpider'
    start_urls = [
        'https://www.amazon.co.uk/dp/B018Y22V5C'
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@id="summaryStars"]'):
            yield {
                '1': quote.xpath('./a/text()[2]').extract_first().strip(),   # sumReviews
                '10': quote.xpath('//div[@id="avgRating"]/span/text()').extract_first().strip(),  # avgRating
                '9(1)': quote.xpath('//table[@id="histogramTable"]/tr/td[3]/a/text()').extract(),  # reviewStat
                '9(2)': quote.xpath('//table[@id="histogramTable"]/tr/td[3]/a/@title').extract(),  # reviewStatPercent
                '8': quote.xpath(
                    '//div[@class="a-section celwidget"]//span[@class="a-size-base a-text-bold"]/text()').extract_first(),  # topReview1
                '2': quote.xpath(
                    '//div[@class="a-section celwidget"]//span[@class="a-icon-alt"]/text()').extract_first(),  # topReview2
                '3': quote.xpath('//a[@class="noTextDecoration"]/text()').extract_first(),  # writer
                '4': quote.xpath('//div[@class="a-section celwidget"]/div[1]/span/span[2]/text()').extract_first().strip(),  # date
                '5': quote.xpath('//div[contains(@id,"revData-dpReviews")]/span[contains(@class,"state")]/text()').extract_first().strip(),  # purchase
                '6': quote.xpath('//div[contains(@id,"revData-dpReviews")]/div/text()').extract_first()
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))


#  https://www.amazon.co.uk/dp/B018Y22V5C
#  https://www.amazon.co.uk/dp/B01LEQV0AW
#  https://www.amazon.co.uk/dp/B000QCQ7T0
#  https://www.amazon.co.uk/dp/B018V5ZAB4
