from appium import webdriver
import os,time,unittest,HTMLTestRunner
class Testlogin(unittest.TestCase):
    def setUp(self):
        self.desired_caps={}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['deviceName']='a6969'
        self.desired_caps['preformVersion']='5.0.2'
        self.desired_caps['appPackage'] = 'com.tencent.mobileqq'
        self.desired_caps['appActivity'] ='.activity.SplashActivity'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        time.sleep(2)
    def tearDown(self):
        self.driver.find_element_by_id('com.tencent.mobileqq:id/conversation_head').click()
        self.driver.find_element_by_id('com.tencent.mobileqq:id/settings').click()
        self.driver.find_element_by_id('com.tencent.mobileqq:id/account_switch').click()
        self.driver.find_element_by_id('com.tencent.mobileqq:id/logoutBtn').click()
        self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
        self.driver.quit()
    def testLogin1(self):
        self.driver.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()

        time.sleep(2)
        me=self.driver.find_element_by_android_uiautomator('new UiSelector().text("QQ号/手机号/邮箱")')
        me.clear()
        me.send_keys('319197149')
        password=self.driver.find_element_by_id('com.tencent.mobileqq:id/password')
        password.clear()
        password.send_keys('lileilei.930423')
        self.driver.find_element_by_id('com.tencent.mobileqq:id/login').click()
        m=self.driver.find_element_by_id('com.tencent.mobileqq:id/conversation_head')
        if m is not None:
            print('login is sucess')
        else:
            print('login is Flase')
            print(self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogText').text)
    def testLogin2(self):
        me=self.driver.find_element_by_android_uiautomator('new UiSelector().text("QQ号/手机号/邮箱")')
        me.clear()
        me.send_keys('31919719')
        password=self.driver.find_element_by_id('com.tencent.mobileqq:id/password')
        password.clear()
        password.send_keys('lileilei.93423')
        self.driver.find_element_by_id('com.tencent.mobileqq:id/login').click()
        m=self.driver.find_element_by_id('com.tencent.mobileqq:id/conversation_head')
        if m is not None:
            print('login is sucess')
        else:
            print('login is Flase')
            print(self.driver.find_element_by_id('com.tencent.mobileqq:id/dialogText').text)
if __name__ == '__main__':
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(Testlogin("testLogin1"))
    suiteTest.addTest(Testlogin("testLogin2"))
    now=time.strftime('%Y-%m%d',time.localtime(time.time()))
    report_dir= r'%s.html'%now
    re_open= open(report_dir,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=re_open,title='QQ测试',description='测试结果')
    runner.run(suiteTest)
