# coding:utf-8
from base_cralwer import BaseCrawler
import time
from phone_generator import PhoneGenerator
import json
import random
import redis

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
        return response.content


if __name__ == '__main__':
    generator = PhoneGenerator()
    phones = generator.import_from_file('phone_sections.txt')
    for phone in phones:
        crawler = JDJR_CRAWLER()
        time.sleep(random.uniform(0.10,0.4))
        content = crawler.run(phone)
        try:
            data = json.loads(content)
            if data['success'] !=0:
                print phone
        except Exception as e:
            print 'error', phone
            print e
