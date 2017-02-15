from appium import webdriver
import time
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='a6969'
desired_caps['preformVersion']='5.0.2'
desired_caps['appPackage']='com.taobao.taobao'
desired_caps['appActivity']='com.taobao.tao.welcome.Welcome'
desired_caps['unicodeKeyboard'] = True
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
time.sleep(2)
sousuo=driver.find_element_by_id('com.taobao.taobao:id/home_searchedit')#搜索
sousuo.click()
time.sleep(2)
suo=driver.find_element_by_id('com.taobao.taobao:id/searchEdit')
suo.clear()
time.sleep(2)
suo.send_keys('移动电源')
driver.find_element_by_id('com.taobao.taobao:id/searchbtn').click()
time.sleep(15)
driver.find_element_by_id('com.taobao.taobao:id/toolbar_footprint').click()
driver.find_element_by_id('id/ali_user_guide_title').click()
shuru=driver.find_element_by_id('id.accountCompleteTextView')
shuru.clear()
shuru.send_keys('15964636199')
paww=driver.find_element_by_id('id/content')
paww.clear()
paww.send_keys('li.930423')
driver.find_element_by_id('id/loginButton').click()
time.sleep(10)
driver.quit()
