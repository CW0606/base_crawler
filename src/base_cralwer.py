# coding:utf-8
from unittest import TestCase
import os
import time
import requests

"""
基础爬虫：
    验证码破解
    IP代理
"""


class BaseCrawler(object):
    MSG_KEY = 'msg'
    STATUS_KEY = 'status'
    IMAGE_FILE_PATH = 'image_file_path'
    VERIFY_IMAGE = 'verify_image'
    IS_OK = 2000
    FILE_NOT_EXISTS = 1008
    FILE_SAVE_FAIL = 1007
    IMAGE_IS_NONE = 1006
    GET_CODE_FAIL = 1005
    verify_IMAGE_IS_NONE = 1004
    DATA_TYPE_ERROR = 1003
    URL_IS_WRONG = 1002
    URL_IS_NONE = 1001
    SESSION_IS_NONE = 1000

    def __init__(self):
        self.request = requests.Session()
        self.request.headers.update({
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US, en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:39.0) Gecko/20100101 Firefox/39.0'
        })

    def _get_verify_code(self, session, url, data, method='GET'):
        if method == 'POST':
            response = session.post(url=url, data=data)
        else:
            response = session.get(url=url, params=data)
        if response.status_code == 200:
            return response.content

    def get_verify_code(self, session, url, data, method='GET'):
        """
        获取图片验证码，做参数验证
        :param session:
        :param url:
        :param data:
        :param method:
        :return:
        {
            status:状态码，
            msg:消息内容
            verify_image:验证码图片
        }
        """
        if session is None:
            return {
                BaseCrawler.STATUS_KEY: BaseCrawler.SESSION_IS_NONE,
                BaseCrawler.MSG_KEY: 'session is none'
            }
        if url is None:
            return {
                BaseCrawler.STATUS_KEY: BaseCrawler.URL_IS_NONE,
                BaseCrawler.MSG_KEY: 'url is none !!'
            }
        if 'http://' not in url and 'https://' not in url:  # 后期需要加入url 正则验证
            return {
                BaseCrawler.STATUS_KEY: BaseCrawler.URL_IS_WRONG,
                BaseCrawler.MSG_KEY: 'url is wrong!!'
            }
        if data is not None and type(data) != 'dict':
            return {
                BaseCrawler.STATUS_KEY: BaseCrawler.DATA_TYPE_ERROR,
                BaseCrawler.MSG_KEY: 'data type error!!'
            }
        try:
            verify_image = self._get_verify_code(session=session, url=url,
                                                 data=data, method=method)
            if verify_image is None:
                return {
                    BaseCrawler.STATUS_KEY: BaseCrawler.verify_IMAGE_IS_NONE,
                    BaseCrawler.MSG_KEY: 'verify_image is none'
                }
            else:
                return {
                    BaseCrawler.STATUS_KEY: BaseCrawler.IS_OK,
                    BaseCrawler.MSG_KEY: 'get success!!',
                    BaseCrawler.VERIFY_IMAGE: verify_image
                }
        except Exception as e:
            return {
                BaseCrawler.STATUS_KEY: BaseCrawler.GET_CODE_FAIL,
                BaseCrawler.MSG_KEY: str(e)
            }

    def _save_verify_code(self, image):
        dir_path = 'image/'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_name = '%d.png' % long(time.time())
        file_path = dir_path + file_name
        with open(file_path, 'w') as f:
            f.write(image)
        return file_path

    def save_verify_code(self, image):
        """
        保存验证码，返回验证码文件路径
        :param image:
        :return:
        """
        if image is None:
            return {
                BaseCrawler.STATUS_KEY: BaseCrawler.IMAGE_IS_NONE,
                BaseCrawler.MSG_KEY: 'image is none!!'
            }
        try:
            result = self._save_verify_code(image)
            if result is None:
                return {
                    BaseCrawler.STATUS_KEY: BaseCrawler.FILE_SAVE_FAIL,
                    BaseCrawler.MSG_KEY: 'file save fail!!'
                }
            else:
                return {
                    BaseCrawler.STATUS_KEY: BaseCrawler.IS_OK,
                    BaseCrawler.MSG_KEY: 'image save success!!',
                    BaseCrawler.IMAGE_FILE_PATH: result
                }
        except Exception as e:
            return {
                BaseCrawler.STATUS_KEY: BaseCrawler.FILE_SAVE_FAIL,
                BaseCrawler.MSG_KEY: str(e)
            }

    def _delete_verify_code(self, file_path):
        os.remove(file_path)

    def delete_verify_code(self, file_path):
        """
        :param file_path:
        :return:
        {
            status:状态码，
            msg:消息内容
        }
        """
        if os.path.isfile(file_path) is False:
            return {
                BaseCrawler.STATUS_KEY: BaseCrawler.FILE_NOT_EXISTS,
                BaseCrawler.MSG_KEY: 'file not exists!!'
            }
        self._delete_verify_code(file_path=file_path)


class TestBaseCrawler(TestCase):
    def setUp(self):
        self.crawler = BaseCrawler()

        pass

    def tearDown(self):
        pass

    def test_get_verify_code(self):
        """测试获取验证码函数"""
        result = self.crawler.get_verify_code(session=None, url=None, data=None)
        # 测试session 为空
        self.assertEqual(result.get(BaseCrawler.STATUS_KEY),
                         BaseCrawler.SESSION_IS_NONE)
        result = self.crawler.get_verify_code(session=self.crawler.request,
                                              url=None, data=None)
        self.assertEqual(result.get(BaseCrawler.STATUS_KEY),
                         BaseCrawler.URL_IS_NONE)
        url = 'www.baidu.com'
        result = self.crawler.get_verify_code(session=self.crawler.request,
                                              url=url, data=None)
        self.assertEqual(result.get(BaseCrawler.STATUS_KEY),
                         BaseCrawler.URL_IS_WRONG)
        url = 'http://www.baidu.com'
        result = self.crawler.get_verify_code(session=self.crawler.request,
                                              url=url,
                                              data=None)
        self.assertEqual(result.get(BaseCrawler.STATUS_KEY), BaseCrawler.IS_OK,
                         result.get(BaseCrawler.MSG_KEY))
        # 测试url 为空

    def test_save_verify_code(self):
        """测试存储函数"""
        pass
