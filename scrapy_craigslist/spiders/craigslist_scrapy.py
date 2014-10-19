__author__ = 'htm'

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy_craigslist.items import ScrapyCraigslistItem

class MySpider(CrawlSpider):
    name = "craigslist"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/apa?"]

    rules = (
        Rule(SgmlLinkExtractor(allow=("search/apa?s=d00&")), callback="parse_items_2", follow= True),
        Rule(SgmlLinkExtractor(allow=(r'sfbay.craigslist.org/search/')), callback="parse_items_1", follow= True),
        )

    def parse_items_1(self, response):
        items = []
        hxs = HtmlXPathSelector(response)
        print response.url
        titles = hxs.select("//div")
        for title in titles:
            item = ScrapyCraigslistItem()
            item ["title"] = title.select("//li/a/text()").extract()
            item ["link"] = title.select("//li/a/@href").extract()
            print ('**parse-items_1:', item["title"])
            items.append(item)
        return items

    # def parse_items_2(self, response):
    #     hxs = HtmlXPathSelector(response)
    #     titles = hxs.select("//p")
    #     items = []
    #     for title in titles:
    #         item = CraigslistSampleItem() #  need to change
    #         item ["title"] = title.select("a/text()").extract()
    #         item ["link"] = title.select("a/@href").extract()
    #         print ('**parse_items_2:', item["title"], item["link"])
    #         items.append(item)
    #     return items