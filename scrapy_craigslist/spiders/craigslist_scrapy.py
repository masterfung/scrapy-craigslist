__author__ = 'htm'

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy_craigslist.items import ScrapyCraigslistItem

class MySpider(CrawlSpider):
    """
    This CrawlSpider will look into the specific city and pull out content for
    Title, Ad's URL, Post Date, Post Date Specific (i.e. datetime), Price,
    Room Details, and Locations. Please reference https://sites.google.com/site/clsiteinfo/city-site-code-sort
    for more on city codes and link.

    If you need to change the city code, please do so at the three locations below:
    allowed domains, start urls, and rules.

    Feel free to change the name of the spider to be more specific.

    """
    name = "craigslist"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/apa?"]

    rules = (
        Rule(SgmlLinkExtractor(allow=(r'sfbay.craigslist.org/search/')), callback="parse_items_1", follow= True,
             ),
        # Rule(SgmlLinkExtractor(allow=("search/apa?s=d00&")), callback="parse_items_2", follow= True),
        )

    def parse_items_1(self, response):
        """

        """
        items = []
        hxs = Selector(response)
        # print response.url
        contents = hxs.xpath("//div[@class='content']/*")
        for content in contents:
            item = ScrapyCraigslistItem()
            item ["title"] = content.xpath("//p/span/span/a/text()").extract()[0]
            k = content.xpath("//p/a/@href").extract()[0]
            item ['ad_url'] = 'http://sfbay.craigslist.org{}'.format(''.join(k))
            # item ["img_url"] = content.select("(//img//@src)").extract() # BAAAD
            item ["post_date"] = content.xpath("//p/span/span/time/text()").extract()[0]
            item ["post_date_specific"] = content.xpath("//p/span/span/time/@datetime").extract()[0]
            item ["price"] = content.xpath("//p/span/span[@class='l2']/span/text()").extract()[0]
            item ["room_details"] = content.xpath("//p/span/span[@class='l2']/text()").extract()[0].strip().replace('/', '')
            item ["location"] = content.xpath("//p/span/span[@class='l2']/span[@class='pnr']/small/text()").extract()[0]
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