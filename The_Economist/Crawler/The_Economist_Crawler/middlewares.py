        # - return a Response object
        # Called for each request that goes through the downloader
    def process_request(self, request, spider):
        # it has processed the response.
        # - or raise IgnoreRequest: process_exception() methods of
        # similarly to the process_spider_output() method, except
        return s
        return s
        # - return None: continue processing this request
    def process_start_requests(self, start_requests, spider):
        # Called with the results returned from the Spider, after
            yield r
class TheEconomistCrawlerDownloaderMiddleware:
        # - return a Request object
        for r in start_requests:
    # passed objects.
    # passed objects.
        # or Item objects.
class TheEconomistCrawlerSpiderMiddleware:
        # Should return either None or an iterable of Request, dict
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
    # scrapy acts as if the spider middleware does not modify the
        # Called with the start requests of the spider, and works
        pass
        pass
#
        spider.logger.info('Spider opened: %s' % spider.name)
        spider.logger.info('Spider opened: %s' % spider.name)
        # - or raise IgnoreRequest
        # (from other spider middleware) raises an exception.
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        s = cls()
        s = cls()
    def process_spider_exception(self, response, exception, spider):
        return response
        # - or return a Response object
from scrapy import signals
        # - return None: continue processing this exception
        # Must return only requests (not items).
        # Should return None or raise an exception.
        # that it doesn’t have a response associated.
        # (from other downloader middleware) raises an exception.
        # middleware.
        # - return a Request object: stops process_exception() chain
    @classmethod
    @classmethod
        for i in result:
        # Called with the response returned from the downloader.
        # Must either;
    def process_exception(self, request, exception, spider):
    # scrapy acts as if the downloader middleware does not modify the
    def spider_opened(self, spider):
    def spider_opened(self, spider):
    def process_spider_input(self, response, spider):
























        # Must either:
        # Must either:
    def from_crawler(cls, crawler):
    def from_crawler(cls, crawler):
# -*- coding: utf-8 -*-
        # middleware and into the spider.
        # Called for each response that goes through the spider
        # - or return a Request object
    def process_response(self, request, response, spider):
    # Not all methods need to be defined. If a method is not defined,
    # Not all methods need to be defined. If a method is not defined,
        # Called when a download handler or a process_request()
        return None
        return None
# See documentation in:
# Define here the models for your spider middleware
        # Must return an iterable of Request, dict or Item objects.
            yield i
        # This method is used by Scrapy to create your spiders.
        # This method is used by Scrapy to create your spiders.
    def process_spider_output(self, response, result, spider):
        # Called when a spider or process_spider_input() method
        #   installed downloader middleware will be called
        # - return a Response object: stops process_exception() chain
