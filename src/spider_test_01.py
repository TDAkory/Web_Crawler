import urllib3
import re
import urlparse3
from src.spider_tools_file import save_to_file
from urllib import robotparser

CRAWL_URL = 'http://example.webscraping.com'
FILE_NAME = 'example'


def download(url, file_name=FILE_NAME, user_agent='wswp', num_retries=2):
    print('Downloading: %s' % url)
    try:
        http = urllib3.PoolManager()
        headers = {'User-agent': user_agent}
        r = http.request('Get', url, headers)
        if num_retries > 0:
            if 500 <= r.status <= 600:
                return download(url, user_agent, num_retries-1)
    except Exception as e:
        print('Download error: %s' % e)
        r = None
    save_to_file(data=r, file=file_name)
    return r


def crawl_sitemap(url, file):
    sitemap = download(url, file)
    print(type(sitemap))
    links = re.findall('<loc>http://(.*?)</loc>', str(sitemap.data))
    for link in links:
        html = download(link, file)
    return html


if __name__ == '__main__':
    # data = crawl_sitemap(CRAWL_URL, FILE_NAME)
    data = download(url=CRAWL_URL, user_agent="wswp")
