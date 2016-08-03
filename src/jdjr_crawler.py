# coding:utf-8
from base_cralwer import BaseCrawler
import time

"""
京东金融
"""


class JDJR_CRAWLER(BaseCrawler):
    def __init__(self):
        super(JDJR_CRAWLER, self).__init__()

    def run(self, phone):
        url = 'https://reg.jd.com/validateuser/isMobileEngaged?phone=%s&mobile=%s&_=%s' % (
        "+0086%s" % str(phone), "+0086%s" % str(phone), str(long(time.time() * 100)))
        before_url = 'https://reg.jd.com/reg/person?ReturnUrl=http%3A%2F%2Fwww.jd.com'
        self.request.get(before_url)
        response = self.request.get(url)
        print response.content


if __name__ == '__main__':
    crawler = JDJR_CRAWLER()
    crawler.run(17090111542)
