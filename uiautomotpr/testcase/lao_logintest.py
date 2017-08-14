# -*- coding: utf-8 -*-
# @Time    : 2017/8/12 16:04
# @Author  : lileilei
# @File    : lao_logintest.py
# @Software: PyCharm
from uiautomator import  device as d
import  unittest,os,ddt,time
from uiautomotpr.util.assert_suc import assert_i
from uiautomotpr.util.data_yaml import data
data=data(f=r'C:\\Users\Administrator\Desktop\appium-uiautomatior\\uiautomotpr\data\data.json')
@ddt.ddt
class TestaixuetangCase(unittest.TestCase):
    def setUp(self):
        cmd = 'adb shell am  start   com.aixuetang.teacher/.activities.LoginActivity '
        os.system(cmd)
    def tearDown(self):
        cmd='adb shell am force-stop com.aixuetang.teacher'
        os.system(cmd)
    @ddt.data(*data)
    def testlogin(self,data):
        d(resourceId='com.aixuetang.teacher:id/et_username').set_text(data['username'])
        d(resourceId='com.aixuetang.teacher:id/et_password').set_text(data['password'])
        d(resourceId='com.aixuetang.teacher:id/tv_login').click()
        assert_m=assert_i(cm=d(resourceId='com.aixuetang.teacher:id/tv_login'))
        self.assertTrue(assert_m)
