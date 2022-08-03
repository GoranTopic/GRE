        # - or raise IgnoreRequest
        for r in start_requests:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
        # or Item objects.
        pass
        pass
    # passed objects.
    # passed objects.
        return s
        return s
        # Called with the start requests of the spider, and works
        # - or return a Request object
    def process_request(self, request, spider):
            yield i
    def process_spider_output(self, response, result, spider):
        # Must return only requests (not items).
    def from_crawler(cls, crawler):
    def from_crawler(cls, crawler):
        # (from other spider middleware) raises an exception.
    # scrapy acts as if the downloader middleware does not modify the
        # middleware.
        # Called when a download handler or a process_request()
        # Should return None or raise an exception.
# -*- coding: utf-8 -*-
        s = cls()
        s = cls()
        # - or raise IgnoreRequest: process_exception() methods of
        # This method is used by Scrapy to create your spiders.
        # This method is used by Scrapy to create your spiders.
        # - return a Response object
        # - or return a Response object
        # Called for each response that goes through the spider
        # Called when a spider or process_spider_input() method
    def process_response(self, request, response, spider):
























        # it has processed the response.
class TheEconomistCrawlerSpiderMiddleware:
    @classmethod
    @classmethod
from scrapy import signals
        # middleware and into the spider.
        # that it doesn’t have a response associated.
    def process_spider_exception(self, response, exception, spider):
    def process_spider_input(self, response, spider):
        # Must either:
        # Must either:
    def process_start_requests(self, start_requests, spider):
# Define here the models for your spider middleware
        for i in result:
        # - return None: continue processing this request
    # Not all methods need to be defined. If a method is not defined,
    # Not all methods need to be defined. If a method is not defined,
        return None
        return None
        # Must either;
        # - return a Request object
            yield r
        # - return None: continue processing this exception
#
        # - return a Response object: stops process_exception() chain
    # scrapy acts as if the spider middleware does not modify the
        # - return a Request object: stops process_exception() chain
        return response
        # (from other downloader middleware) raises an exception.
    def spider_opened(self, spider):
    def spider_opened(self, spider):
        # Called for each request that goes through the downloader
        # Should return either None or an iterable of Request, dict
    def process_exception(self, request, exception, spider):
        # similarly to the process_spider_output() method, except
class TheEconomistCrawlerDownloaderMiddleware:
        # Must return an iterable of Request, dict or Item objects.
        #   installed downloader middleware will be called
# See documentation in:
        # Called with the results returned from the Spider, after
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        spider.logger.info('Spider opened: %s' % spider.name)
        spider.logger.info('Spider opened: %s' % spider.name)
        # Called with the response returned from the downloader.
