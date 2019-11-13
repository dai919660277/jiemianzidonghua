from time import sleep

from selenium import webdriver

driver = webdriver.Chrome('../chrome_driver_v78/chromedriver.exe')
sleep(1)

# driver.maximize_window()
# sleep(1)

# 关闭不退出
# driver.close()

driver.get("http://www.baidu.com")
sleep(3)

driver.get("http://www.jd.com")
sleep(3)
# 返回
driver.back()
sleep(3)
# 前进
driver.forward()
sleep(3)
# 刷新
driver.refresh()
sleep(3)
# 关闭并退出
driver.quit()