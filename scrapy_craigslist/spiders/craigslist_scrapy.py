__author__ = 'htm'

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy_craigslist.items import ScrapyCraigslistItem

class MySpider(CrawlSpider):
    """

    """
    name = "craigslist"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/apa?"]

    rules = (
        Rule(SgmlLinkExtractor(allow=(r'sfbay.craigslist.org/search/')), callback="parse_items_1", follow= True),
        Rule(SgmlLinkExtractor(allow=("search/apa?s=d00&")), callback="parse_items_2", follow= True),
        )

    def parse_items_1(self, response):
        """

        """
        items = []
        hxs = HtmlXPathSelector(response)
        # print response.url
        contents = hxs.select("//div[@class='content']/*")
        for content in contents:
            item = ScrapyCraigslistItem()
            item ["title"] = content.select("//p/span/span/a/text()").extract()[0]
            item ["ad_url"] = content.select("//p/a/@href").extract()[0]
            # item ["img_url"] = content.select("(//p/a[@class='i'])").extract()[0] # BAAAD
            item ["post_date"] = content.select("//p/span/span/time/text()").extract()[0]
            item ["post_date_specific"] = content.select("//p/span/span/time/@datetime").extract()[0]
            item ["price"] = content.select("//p/span/span[@class='l2']/span/text()").extract()[0]
            item ["room_details"] = content.select("//p/span/span[@class='l2']/text()").extract()[0].strip().replace('/', '')
            item ["location"] = content.select("//p/span/span[@class='l2']/span[@class='pnr']/small/text()").extract()[0]
            # print ('**parse-items_1:', item["title"])
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