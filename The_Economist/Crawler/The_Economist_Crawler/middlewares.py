        return s
        return s
    def process_spider_input(self, response, spider):
        # Called with the start requests of the spider, and works
        #   installed downloader middleware will be called
        s = cls()
        s = cls()
    def process_spider_exception(self, response, exception, spider):
        # Must return an iterable of Request, dict or Item objects.
    # scrapy acts as if the downloader middleware does not modify the
# -*- coding: utf-8 -*-
        # Called with the results returned from the Spider, after
# See documentation in:
    def process_request(self, request, spider):
    def spider_opened(self, spider):
    def spider_opened(self, spider):
        return None
        return None
        # - return a Request object: stops process_exception() chain
    # scrapy acts as if the spider middleware does not modify the
    def process_response(self, request, response, spider):
    def process_start_requests(self, start_requests, spider):
    def process_exception(self, request, exception, spider):
        # - or raise IgnoreRequest
            yield r
        # Should return either None or an iterable of Request, dict
    @classmethod
    @classmethod
        # middleware.
        # - return None: continue processing this request
        # similarly to the process_spider_output() method, except
        # - or return a Request object
    def from_crawler(cls, crawler):
    def from_crawler(cls, crawler):
    # Not all methods need to be defined. If a method is not defined,
    # Not all methods need to be defined. If a method is not defined,
        for r in start_requests:
from scrapy import signals
class TheEconomistCrawlerSpiderMiddleware:
        # Must return only requests (not items).
    # passed objects.
    # passed objects.
























        # (from other spider middleware) raises an exception.
        return response
        # Called for each response that goes through the spider
            yield i
        # middleware and into the spider.
        # - return a Response object: stops process_exception() chain
        # Called for each request that goes through the downloader
        # - or return a Response object
    def process_spider_output(self, response, result, spider):
# Define here the models for your spider middleware
        # Called when a spider or process_spider_input() method
        # - return a Response object
        # - or raise IgnoreRequest: process_exception() methods of
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
        # that it doesn’t have a response associated.
        # Called with the response returned from the downloader.
        # it has processed the response.
        # Should return None or raise an exception.
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        for i in result:
        # - return None: continue processing this exception
        # Called when a download handler or a process_request()
        # Must either:
        # Must either:
        pass
        pass
        # Must either;
class TheEconomistCrawlerDownloaderMiddleware:
        # This method is used by Scrapy to create your spiders.
        # This method is used by Scrapy to create your spiders.
        spider.logger.info('Spider opened: %s' % spider.name)
        spider.logger.info('Spider opened: %s' % spider.name)
#
        # (from other downloader middleware) raises an exception.
        # - return a Request object
        # or Item objects.
