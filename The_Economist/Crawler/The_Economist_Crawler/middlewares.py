#
        # that it doesn’t have a response associated.
        # Called when a spider or process_spider_input() method
    def process_response(self, request, response, spider):
        # - return None: continue processing this exception
        # (from other spider middleware) raises an exception.
        # - return a Request object: stops process_exception() chain
        # it has processed the response.
        for r in start_requests:
            yield r
        # Should return None or raise an exception.
    # scrapy acts as if the spider middleware does not modify the
        # Must return an iterable of Request, dict or Item objects.
    def spider_opened(self, spider):
    def spider_opened(self, spider):
class TheEconomistCrawlerSpiderMiddleware:
        # Called for each request that goes through the downloader
        # This method is used by Scrapy to create your spiders.
        # This method is used by Scrapy to create your spiders.
        return s
        return s
    def process_exception(self, request, exception, spider):
    def process_request(self, request, spider):
    def from_crawler(cls, crawler):
    def from_crawler(cls, crawler):
        # - or raise IgnoreRequest
        # Called when a download handler or a process_request()
from scrapy import signals
        # Called with the response returned from the downloader.
    def process_spider_output(self, response, result, spider):
        # Must either:
        # Must either:
        return None
        return None
        # - return a Response object
    @classmethod
    @classmethod
        # or Item objects.
        # Must either;
        s = cls()
        s = cls()
        # middleware and into the spider.
        # - return a Response object: stops process_exception() chain
    def process_spider_input(self, response, spider):
    def process_spider_exception(self, response, exception, spider):
        # Called for each response that goes through the spider
        for i in result:
class TheEconomistCrawlerDownloaderMiddleware:
        # (from other downloader middleware) raises an exception.
        # - or raise IgnoreRequest: process_exception() methods of
        # - return None: continue processing this request
        #   installed downloader middleware will be called
        # Must return only requests (not items).
        return response
        pass
        pass
# -*- coding: utf-8 -*-
        # - or return a Response object
# See documentation in:
        spider.logger.info('Spider opened: %s' % spider.name)
        spider.logger.info('Spider opened: %s' % spider.name)
        # - or return a Request object
            yield i
        # similarly to the process_spider_output() method, except
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        # Called with the results returned from the Spider, after
        # - return a Request object
    # Not all methods need to be defined. If a method is not defined,
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
        # middleware.
























# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
    def process_start_requests(self, start_requests, spider):
# Define here the models for your spider middleware
    # passed objects.
    # passed objects.
        # Should return either None or an iterable of Request, dict
        # Called with the start requests of the spider, and works
