#coding=utf8

__author__ = 'DixonShen'

from scrapy.contrib.spiders import BaseSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from CLPictures.items import ClpicturesItem
import re
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.http.cookies import CookieJar

class CLPictures(BaseSpider):
    name = 'caoliu'
    allowed_doamins = ''
    start_urls = []
    for i in range(900,1000):
        temp = 'http://jandan.net/ooxx/page-' + str(i) + '#comments'
        start_urls.append(temp)
    # rules = (Rule(SgmlLinkExtractor(allow=('/htm_data/\d*/\d*/\d*.html')),callback='parse_pic',follow=True),)

    def parse(self, response):
        urlItem = ClpicturesItem()
        sel = Selector(response)
        for inp in sel.xpath('//img'):
            pic_url = inp.xpath('./@src').extract()
            print pic_url
            urlItem['image_urls'] = pic_url
            yield urlItem
