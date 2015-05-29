# -*- coding: utf-8 -*-

import unittest
from mock import patch

from bilichat.chat import Message
from bilichat.chat import ChatClient


class BilichatTest(unittest.TestCase):

    def setUp(self):
        d1 = {u'nickname': u'Akassin',
              u'text': u'\u54a6\u5df2\u7ecf\u80fd\u83b7\u53d6\u5230\u5b9e\u65f6\u5f39\u5e55\u4e86\u5417\uff08',
              u'timeline': u'2015-05-23 11:03:06',
              u'uid': 102141}
        d2 = {u'nickname': u'Akassin',
              u'text': u'\u54a6\u5df2\u7ecf\u80fd\u83b7\u53d6\u5230\u5b9e\u65f6\u5f39\u5e55\u4e86\u5417\uff08',
              u'timeline': u'2015-05-23 11:03:06',
              u'uid': 102142}
        d3 = {u'nickname': u'Akassin',
              u'text': u'\u54a6\u5df2\u7ecf\u80fd\u83b7\u53d6\u5230\u5b9e\u65f6\u5f39\u5e55\u4e86\u5417\uff08',
              u'timeline': u'2015-05-23 11:03:07',
              u'uid': 102141}
        self.m1 = Message(**d1)
        self.m1too = Message(**d1)
        self.m2 = Message(**d2)
        self.m3 = Message(**d3)

        self.r1 = {u'code': 0,
                   u'data': {u'admin': [{u'nickname': u'\u9ed1\u6850\u8c37\u6b4c',
                                         u'text': u'\u6211\u53bb\u5f00\u65b0\u6d6a\u76f4\u64ad',
                                         u'timeline': u'2015-05-19 19:54:34',
                                         u'uid': 43536},
                                        {u'nickname': u'\u9ed1\u6850\u8c37\u6b4c',
                                         u'text': u'http:kan.sina.com.cnu1765335300',
                                         u'timeline': u'2015-05-19 19:54:41',
                                         u'uid': 43536},
                                        {u'nickname': u'\u9ed1\u6850\u8c37\u6b4c',
                                         u'text': u'\x7f\u53bb\u65b0\u6d6a\u5427',
                                         u'timeline': u'2015-05-22 18:43:47',
                                         u'uid': 43536}],
                             u'room': [{u'nickname': u'\u5c0f\u5409hahayo',
                                        u'text': u'\u8c37\u6b4c\u4ee5\u524d\u80af\u5b9a\u662f\u65e5\u548c\u6f2b\u753b\u7684',
                                        u'timeline': u'2015-05-23 13:06:49',
                                        u'uid': 7178304},
                                       {u'nickname': u'\u706c\u706c\u4e36\u8f89\u8f89',
                                        u'text': u'\u53f3\u4e0a\u89d2\u662f\u4ec0\u4e48',
                                        u'timeline': u'2015-05-23 13:06:55',
                                        u'uid': 2523999},
                                       {u'nickname': u'\u8d85\u4eba\u7ea2\u88e4\u8869',
                                        u'text': u'\u4e3a\u4ec0\u4e48\u6211\u603b\u662f\u53d8\u6210\u5f55\u64ad',
                                        u'timeline': u'2015-05-23 13:06:57',
                                        u'uid': 4282126},
                                       {u'nickname': u'\u963f\u9cde',
                                        u'text': u'\u8c37\u6b4c\u5341\u5206\u72b9\u8c6b',
                                        u'timeline': u'2015-05-23 13:06:57',
                                        u'uid': 2514142},
                                       {u'nickname': u'Genesis\u9b54\u7406\u6c99',
                                        u'text': u'\u53f3\u4e0a\u89d2\u53d7\u4e0d\u4e86\u4e86\u3002\u3002\u3002',
                                        u'timeline': u'2015-05-23 13:07:01',
                                        u'uid': 1121600},
                                       {u'nickname': u'cyan\xb7\u82cd\u6708',
                                        u'text': u'\u8c37\u6b4c\u7684\u7b11\u5bb92333333333333',
                                        u'timeline': u'2015-05-23 13:07:07',
                                        u'uid': 1112147},
                                       {u'nickname': u'\u6296M\u5c0f\u53d7\u9505\u8126\u809b',
                                        u'text': u'\u53c8\u7b11\u7684\u597d\u7325\u7410',
                                        u'timeline': u'2015-05-23 13:07:07',
                                        u'uid': 369989},
                                       {u'nickname': u'ilovemikua',
                                        u'text': u'\u6211\u4e5f\u662f\uff0c\u597d\u5de7wwwwwwwwww',
                                        u'timeline': u'2015-05-23 13:07:18',
                                        u'uid': 1451084},
                                       {u'nickname': u'\u8eb2\u55b5\u55b5\u4e36',
                                        u'text': u'\u8c37\u6b4c\u662f\u5728\u73a9\u6e38\u620f\u5462\uff0c\u8fd8\u662f\u5728\u73a9\u8868\u60c5\u5462\u3002\u3002',
                                        u'timeline': u'2015-05-23 13:07:20',
                                        u'uid': 417229},
                                       {u'nickname': u'\u5446\u8272',
                                        u'text': u'\u53f3\u4e0a\u89d2\u7684\u8868\u60c5\u662f\u8c37\u6b4c\u505a\u51fa\u6765\u7684\u5417 ',
                                        u'timeline': u'2015-05-23 13:07:22',
                                        u'uid': 313867}]},
                   u'msg': u''}

        self.r2 = {u'code': 0,
                   u'data': {u'admin': [{u'nickname': u'\u9ed1\u6850\u8c37\u6b4c',
                                         u'text': u'\u6211\u53bb\u5f00\u65b0\u6d6a\u76f4\u64ad',
                                         u'timeline': u'2015-05-19 19:54:34',
                                         u'uid': 43536},
                                        {u'nickname': u'\u9ed1\u6850\u8c37\u6b4c',
                                         u'text': u'http:kan.sina.com.cnu1765335300',
                                         u'timeline': u'2015-05-19 19:54:41',
                                         u'uid': 43536},
                                        {u'nickname': u'\u9ed1\u6850\u8c37\u6b4c',
                                         u'text': u'\x7f\u53bb\u65b0\u6d6a\u5427',
                                         u'timeline': u'2015-05-22 18:43:47',
                                         u'uid': 43536}],
                             u'room': [{u'nickname': u'\u534e\u4e3d\u4e3d\u7684\u98ce\u666f',
                                        u'text': u'\u4e00\u8138\u6109\u60a6\u7684\u8868\u60c5',
                                        u'timeline': u'2015-05-23 13:08:45',
                                        u'uid': 6020232},
                                       {u'nickname': u'\u4fca\u795e',
                                        u'text': u'\u81ea\u5df1\u9009\u5168\u9519\u3002\u4e3a\u4ec0\u4e48\u8c37\u5927\u6253\u6253\u54c8\u6b20\u90fd\u80fd\u9009\u5bf9\u3002\u3002\u7ecf\u9a8c\u4e48\u3002',
                                        u'timeline': u'2015-05-23 13:08:46',
                                        u'uid': 3204584},
                                       {u'nickname': u'\u5c0f\u5409hahayo',
                                        u'text': u'\u663e\u793a\u5668\uff1a \u8c37\u6b4c\u4e3b\u4eba\u8138\u90e8\u62bd\u7b4b\u4e86\uff1f',
                                        u'timeline': u'2015-05-23 13:09:00',
                                        u'uid': 7178304},
                                       {u'nickname': u'\u7434\u4e5d\u4e09',
                                        u'text': u'2333',
                                        u'timeline': u'2015-05-23 13:09:15',
                                        u'uid': 825840},
                                       {u'nickname': u'Funiayi',
                                        u'text': u'\u8fd9\u5230\u5e95\u662f\u953b\u70bc\u5973\u7684 \u8fd8\u662f\u653b\u7565\u5979\u554a',
                                        u'timeline': u'2015-05-23 13:09:17',
                                        u'uid': 4955113},
                                       {u'nickname': u'\u5173\u4e8e\u54d4\u54e9\u54d4\u54e9\u52a8\u753b',
                                        u'text': u'\u8fd9\u6d63\u718a\u592a\u840c\u4e86\u54c8\u54c8\u54c8\u54c8',
                                        u'timeline': u'2015-05-23 13:09:19',
                                        u'uid': 472878},
                                       {u'nickname': u'Accelerator***',
                                        u'text': u'233333333333333',
                                        u'timeline': u'2015-05-23 13:09:20',
                                        u'uid': 565549},
                                       {u'nickname': u'\u590f\u5c9a\u542c\u96e8',
                                        u'text': u'\u53f3\u4e0a\u89d2\u7b11\u8db4',
                                        u'timeline': u'2015-05-23 13:09:21',
                                        u'uid': 179223},
                                       {u'nickname': u'\u964c\u5c0f\u5343',
                                        u'text': u'\u989c\u827a\u597d\u8bc4',
                                        u'timeline': u'2015-05-23 13:09:38',
                                        u'uid': 3087616},
                                       {u'nickname': u'\u9ad8\u6e05\u4e94\u7801\u6eda\u7c97',
                                        u'text': u'\u4e0d\u884c\u4e86 \u6211\u8981\u4e13\u5fc3\u770b\u8c37\u6b4c\u7684\u989c\u827a',
                                        u'timeline': u'2015-05-23 13:09:40',
                                        u'uid': 3389126}]},
                   u'msg': u''}

    def testMessageComp(self):
        assert self.m1 == self.m1too
        assert self.m1 != self.m2
        assert self.m1 != self.m3
        set1 = set()
        set1.add(self.m1)
        set2 = set()
        set2.add(self.m1)
        set2.add(self.m1)
        assert set1 == set2

    def testNewMessage(self):
        c = ChatClient(roomid=1)

        with patch('bilichat.chat.requests') as mock_requests:

            class Wrapped(object):
                def __init__(self, data):
                    self.data = data

                def json(self):
                    return self.data

            class SideEffect(object):
                count = 0

                @classmethod
                def my_side_effect(cls, *args, **kwargs):
                    cls.count += 1
                    if cls.count % 2 == 1:
                        return Wrapped(self.r1)
                    else:
                        return Wrapped(self.r2)

            mock_requests.post.side_effect = SideEffect.my_side_effect
            s = c.run()
            assert len(list(s)) > 0
