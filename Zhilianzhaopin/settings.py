# -*- coding: utf-8 -*-

# Scrapy settings for Zhilianzhaopin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Zhilianzhaopin'

SPIDER_MODULES = ['Zhilianzhaopin.spiders']
NEWSPIDER_MODULE = 'Zhilianzhaopin.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Zhilianzhaopin (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept':'*/*',
#'accept-Encoding': 'gzip, deflate'
    'accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'dywea=95841923.2852533780639615000.1524642091.1524642091.1524642091.1; dywec=95841923; dywez=95841923.1524642091.1.1.dywecsr=google.com.hk|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/; adfbid=0; adfbid2=0; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1524642092; __utma=269921210.38320306.1524642093.1524642093.1524642093.1; __utmc=269921210; __utmz=269921210.1524642093.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); JSSearchModel=0; LastCity%5Fid=544; LastCity=%e5%b1%b1%e4%b8%9c; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; dyweb=95841923.16.9.1524642429723; __utmb=269921210.16.9.1524642429726; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1524642514; LastSearchHistory=%7b%22Id%22%3a%22274d307f-bdff-414e-a961-58c08eab1909%22%2c%22Name%22%3a%22%e5%b1%b1%e4%b8%9c+%2b+%e8%bd%af%e4%bb%b6%2f%e4%ba%92%e8%81%94%e7%bd%91%e5%bc%80%e5%8f%91%2f%e7%b3%bb%e7%bb%9f%e9%9b%86%e6%88%90+%2b+%e8%bd%af%e4%bb%b6%e5%b7%a5%e7%a8%8b...%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d544%26bj%3d160000%26sj%3d045%26sg%3de749ffdf17d7456491ea6103f078f5f8%26p%3d2%22%2c%22SaveTime%22%3a%22%5c%2fDate(1524643985149%2b0800)%5c%2f%22%7d',
    #'Host': 'cdata.ganji.com',
    'referer': 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=544&bj=160000&sj=045&sg=e749ffdf17d7456491ea6103f078f5f8&p=1',
    'user-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Zhilianzhaopin.middlewares.ZhilianzhaopinSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Zhilianzhaopin.middlewares.ZhilianzhaopinDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Zhilianzhaopin.pipelines.ZhilianzhaopinPipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
