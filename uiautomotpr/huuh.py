from uiautomator import  device as d
import  time,sys,random,unittest,os
def cmd():
    os.system('adb devices ')
    path=os.path.join(os.getcwd(),'QQ6.6.6.apk')
    os.system('adb install %s '%path)
def qidong():
    d.screen.on()
    cmd='adb shell am  start -n com.tencent.mobileqq/.activity.SplashActivity '
    os.system(cmd)
    d.press.home()
def login():
    try:
        d(resourceId='com.tencent.mobileqq:id/btn_login').click()
        d(text='QQ号/手机号/邮箱').set_text('319197149')
        d(resourceId='com.tencent.mobileqq:id/password').set_text('lileilei.930423')
        d(resourceId='com.tencent.mobileqq:id/login').click()
        time.sleep(20)
        if d(text='消息').exists:
            print('登录成功')
        else:
            print('denglushibai')
    except Exception as e:
        print(e)
def fabiao_shuoshuo():
    m=d(resourceId='com.tencent.mobileqq:id/name',index='2',className='android.widget.ImageView')
    m[3].click()
    if d(text='兴趣部落').exists:
        d(resourceId='com.tencent.mobileqq:id/qzone_feed_entry').click()
        if d(text='好友动态').exists:
            d(resourceId='com.tencent.mobileqq:id/name',index=2,className='android.widget.LinearLayout').click()
            time.sleep(1)
            d(resourceId='com.tencent.mobileqq:id/name',index='1').click()
            time.sleep(1)
            d(resourceId='com.tencent.mobileqq:id/name').set_text('this is 北京')
            time.sleep(1)
            d(resourceId='com.tencent.mobileqq:id/ivTitleBtnRightText').click()
            time.sleep(1)
            print('ok')
        else:
            print('进入空间失败')
    else:
        print('你的程序可能没有找到您想要的，请确认您的定位是否正确')
def logout():
    d(resourceId='com.tencent.mobileqq:id/conversation_head').click()
    d(resourceId='com.tencent.mobileqq:id/settings').click()
    d(resourceId='com.tencent.mobileqq:id/account_switch').click()
    d(resourceId='com.tencent.mobileqq:id/logoutBtn').click()
    d(resourceId='com.tencent.mobileqq:id/dialogRightBtn').click()
    if d(text='登录').exists:
        print('不能退出成功')
    else:
        print('退出成功')
        time.sleep(1)
        os.system('adb uninstall com.tencent.mobileqq')
        time.sleep(2)
        if d(text='QQ').exists:
            print('卸载失败')
        else:
            print('卸载成功')
if __name__=="__main__":
    cmd()
    qidong()
    login()
    fabiao_shuoshuo()
    logout()
