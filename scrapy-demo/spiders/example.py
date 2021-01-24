import scrapy
import html2text
from scrapy import item
from items import TutorialItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://voltag.ru/catalog/list/?q=69-8213']
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    def parse(self, response):
        description_div = response.xpath('//*[@id="center"]/div[2]/div')
        h = html2text.HTML2Text()
        h.ignore_links = True

        description = h.handle(description_div.get())

        item = TutorialItem()
        item['site'] = 'voltag.ru',
        item['sku'] = '69-8213',
        item['description'] = description
        yield item
