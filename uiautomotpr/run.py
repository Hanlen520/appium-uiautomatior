# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: run.py
@time: 2017/8/14 11:51
"""
import os,time,unittest
from uiautomotpr.util import HTMLTestRunner
if __name__=='__main__':
    basdir = os.path.abspath(os.path.dirname(__file__))
    path=os.path.join(basdir+'\\testcase')
    test_suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(path, pattern='*test.py', top_level_dir=None)
    for test in discover:
        for test_case in test:
            test_suit.addTest(test_case)
    now = time.strftime('%Y-%m%d', time.localtime(time.time()))
    filepath = os.path.join(basdir + '\\testresult\\%s-result.html' % now)
    re_open = open(filepath, 'wb')
    renner = HTMLTestRunner.HTMLTestRunner(stream=re_open, title=u'爱学堂demo by uiautomator', description=u'测试结果')
    renner.run(test_suit)