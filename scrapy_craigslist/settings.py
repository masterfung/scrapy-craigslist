# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_craigslist project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_craigslist'

SPIDER_MODULES = ['scrapy_craigslist.spiders']
NEWSPIDER_MODULE = 'scrapy_craigslist.spiders'

# DUPEFILTER_DEBUG = True

# DUPEFILTER_CLASS = 'scrapy_craigslist.filters.NoDuplicateUrl'

ITEM_PIPELINES = {
    'scrapy_craigslist.pipelines.DuplicatesPipeline': 10,

}

USER_AGENT = "Mozilla/5.0 (Windows NT 5.1; rv:12.2.1) Gecko/20120616 Firefox/12.2.1 PaleMoon/12.2.1"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_craigslist (+http://www.yourdomain.com)'
