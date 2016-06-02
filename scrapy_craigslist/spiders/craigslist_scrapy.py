__author__ = 'Tsung Hung'

from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
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

    Feel free to change the name of the spider to something more specific.

    """
    name = 'craigslist'
    allowed_domains = ['sfbay.craigslist.org']
    start_urls = ['https://sfbay.craigslist.org/search/apa?']

    # rules = (
    #     # Scrape all pages of results, not just the first page.
    #     Rule(LinkExtractor(
    #         allow = (r'.*/search/apa\?s\=\d+.*'),
    #         deny = (r'.*format\=rss.*')
    #     ), callback='parse_items_1', follow=True),
    #
    #     # Extract all data from each results page.
    #     Rule(LinkExtractor(allow=(r'.*/apa/.*\.html$')), callback='parse_items_1'),
    # )

    rules = (
        Rule(LxmlLinkExtractor(
            allow=(r'sfbay.craigslist.org/search/apa.*'),
            # allow=(r'.*/search/apa\?s\=\d+.*'),
            deny = (r'.*format\=rss.*')
        ),
            callback="parse_items_1",
            follow= True,
             ),
        # Rule(LxmlLinkExtractor(allow=("search/apa?s=d00&")), callback="parse_items_2", follow= True),
        )


# allow=(r'sfbay.craigslist.org/search')

    def parse_items_1(self, response):
        """
        This function takes teh content from contents and map them according to the
        items from items.py. If the key exists in content, then Scrapy will aggregate
        the rest of the items and combine them.

        Each content will have "[0]" to indicate the first listing from the array.
        """
        self.logger.info('You are now crawling: %s', response.url)
        items = []
        hxs = Selector(response)
        # print response.url
        contents = hxs.xpath("//div[@class='rows']/*")
        for content in contents:
            item = ScrapyCraigslistItem()
            item ["title"] = content.xpath("//p/span/span/a/span/text()").extract()[0]
            k = content.xpath("//p/a/@href").extract()[0]
            item ['ad_url'] = 'https://sfbay.craigslist.org{}'.format(''.join(k))
            item ["post_date"] = content.xpath("//p/span/span/time/text()").extract()[0]
            item ["post_date_specific"] = content.xpath("//p/span/span/time/@datetime").extract()[0]
            item ["price"] = content.xpath("//p/span/span[@class='l2']/span/text()").extract()[0]
            item ["location"] = content.xpath("//p/span/span[@class='l2']/span[@class='pnr']/small/text()").extract()[0].strip()
            # print ('**parse-items_1:', item["title"])
            items.append(item)
        return items
