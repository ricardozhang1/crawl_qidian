#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
'''
随机选取UserAgent
'''

class RandomUserAgent(object):

    def __init__(self,agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))
        #返回的是本类的实例cls ==RandomUserAgent

    def process_request(self,request,spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))

