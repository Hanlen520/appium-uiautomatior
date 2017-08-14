# -*- coding: utf-8 -*-
# @Date    : 2017-08-14 11:04:46
# @Author  : lileilei 
import ddt,unittest
import os
import time
from uiautomator import device as d
from uiautomotpr.util.assert_suc import assert_i
from uiautomotpr.util.data_yaml import data
data=data(f=r'C:\\Users\Administrator\Desktop\\appium-uiautomatior\\uiautomotpr\data\\xiugai.json')
@ddt.ddt
class TestaixuetangCase(unittest.TestCase):
    def setUp(self):
        cmd = 'adb shell am  start   com.aixuetang.teacher/.activities.LoginActivity '
        os.system(cmd)
    @ddt.data(*data)
    def testlogin(self,data):
        time.sleep(2)
        d(text=u'忘记密码').click()
        d(resourceId='com.aixuetang.teacher:id/phoneNum').set_text(data['username'])
        d(resourceId='com.aixuetang.teacher:id/et_code').set_text(data['yazhangma'])
        d(resourceId='com.aixuetang.teacher:id/tv_register').click()
        m=d(resourceId='com.aixuetang.teacher:id/tv_msg_tip').exists
        self.assertTrue(m)
    def tearDown(self):
        cmd='adb shell am force-stop com.aixuetang.teacher'
        os.system(cmd)
