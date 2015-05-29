#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from datetime import datetime
import requests


class ChatClient(object):

    def __init__(self, roomid, sleep=1):
        self.roomid = roomid
        self.sleep = sleep
        self.history = set()
        self.current = None
        self.new = None
        self.request()
        self.store()

    def request(self):
        to_post = {'roomid': self.roomid}
        r = requests.post('http://live.bilibili.com/ajax/msg', data=to_post)
        # data from server is UTF8
        self.current = self.aggregate(r.json())

    def aggregate(self, data):
        s = set()
        for msg in data['data']['room']:
            s.add(Message(**msg))
        for msg in data['data']['admin']:
            s.add(Message(**msg))
        return s

    # to forbid duplicate message, here we need to store the message history
    def store(self):
        self.history = self.current
        self.current = None

    def run(self):
        self.request()
        assert self.history is not None
        assert self.current is not None
        self.new = list(self.current - self.history)
        self.new.sort(lambda a, b: int(a.timeline - b.timeline))
        self.store()
        for msg in self.new:
            print ': '.join([msg.nickname.encode('UTF8'), msg.text.encode('UTF8')])
        return self.new

    def loop(self):
        while True:
            time.sleep(self.sleep)
            self.run()


class Message(object):

    TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(self, **kwargs):
        self.nickname = kwargs['nickname']
        self.timeline = time.mktime(datetime.strptime(kwargs['timeline'], self.TIME_FORMAT).timetuple())
        self.text = kwargs['text']
        self.uid = int(kwargs['uid'])

    def __repr__(self):
        return '<%d %s>' % (self.uid, self.timeline)

    def __eq__(self, other):
        if isinstance(other, Message):
            return self.timeline == other.timeline and self.uid == other.uid

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.uid, self.timeline))

if __name__ == '__main__':
    c = ChatClient(roomid=1029)
    c.loop()
