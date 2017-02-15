import os,unittest
from uiautomator import devices as d
class Testyingke(unittest.TestCase):
    def setUp(self):
        cmd='adb shell am start -n com.meelive.ingkee/com.meelive.ingkee.ui.main.MainPageActivity'
        os.system(cmd)
        self.d=d
        #手机号登录
    def testlogin_phonenumber(self):
        self.d(resourceId='com.meelive.ingkee:id/btn_phone_third').click()#shouiphonenumber
        self.d(resourceId='com.meelive.ingkee:id/edit_phone_login_phonenum').set_text('')#iphonenumber
        self.d(resourceId='com.meelive.ingkee:id/btn_phone_login_verify').click()#获取验证码
        if self.d(text='提示').exists:
            print*(resourceId='com.meelive.ingkee:id/txt_content').text)
        else:
            self.d(resourceId='com.meelive.ingkee:id/edit_phone_login_verifycode').set_text() #输入验证码
            self.d(resourceId='com.meelive.ingkee:id/btn_phone_login').click()#login
            if self.d(text='提示').exists:
                print((resourceId='com.meelive.ingkee:id/txt_content').text)
            else:
                if self.d(text='设置头像').exists:
                    self.d(resourceId='com.meelive.ingkee:id/phone_login_edit_nick').set_text()
                    self.d(resourceId='com.meelive.ingkee:id/phone_login_sex_male').click()#设置男
                    self.d(resourceId='com.meelive.ingkee:id/phone_login_edit_confirm').click()#完成出事设置
                    if self.d(resourceId='com.meelive.ingkee:id/img_search').exists:
                        print('登录成功')
                else:
                    if self.d(resourceId='com.meelive.ingkee:id/img_search').exists:
                        print('登录成功')
                    else:
                        print('登录失败')
    def test_login_weixin(self):
        #微信登录
        self.d(resourceId='com.meelive.ingkee:id/btn_weixin_third').click()
        if self.d(text='提示').exists:
            self.d(resourceId='com.meelive.ingkee:id/btn_confirm').click()#确认下载
            if self.d(resourceId='com.meelive.ingkee:id/btn_cancel').click():
                print('取消微信登录')
    def test_login_weibo(self):
        #qq登录
        self.d(resourceId='com.meelive.ingkee:id/btn_qq_third').click()
    def tearDown(self):
        self.d(className='android.widget.RelativeLayout',index=2).click()
        self.d(resourceId='com.meelive.ingkee:id/btn_no_disturb').click()
        self.d(resourceId='com.meelive.ingkee:id/btn_logout').click()
        self.d.press.home()
