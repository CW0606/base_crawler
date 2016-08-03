# coding:utf-8
from unittest import TestCase

"""
基础爬虫：
    验证码破解
    IP代理
"""


class BaseCrawler(object):
    VERIFY_IMAGE = 'verify_image'
    IS_OK = 2000
    GET_CODE_FAIL = 1005
    verify_IMAGE_IS_NONE = 1004
    DATA_TYPE_ERROR = 1003
    URL_IS_WRONG = 1002
    URL_IS_NONE = 1001
    SESSION_IS_NONE = 1000
    STATUS_KEY = 'status'
    MSG_KEY = 'msg'

    def __init__(self):
        pass

    def _get_verify_code(self, session, url, data, method='GET'):
        """
        获取验证码图片
        :param session:
        :param url:
        :param data:
        :param method: default['GET']
        :return:
        """
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
        if 'http://' not in url or 'https://' not in url:  # 后期需要加入url 正则验证
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
        pass

    def save_verify_code(self, image):
        """
        保存验证码，返回验证码文件路径
        :param image:
        :return:
        """
        pass
    def _delete_verify_code(self,file_path):
        """

        :param file_path:
        :return:
        """
        pass

    def delete_verify_code(self,file_path):
        """
        
        :param file_path:
        :return:
        """
        pass


class TestBaseCrawler(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_verify_code(self):
        """测试获取验证码函数"""
        pass

    def test_save_verify_code(self):
        """测试存储函数"""
        pass
