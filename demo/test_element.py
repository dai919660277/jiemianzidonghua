from time import sleep

def test_dxd(driver):
    driver.get("http://www.baidu.com")# 打开百度网
    sleep(3)

    driver.get("http://www.jd.com")# 打开京东网
    sleep(3)
    # 返回
    driver.back()# 返回上个链接
    sleep(3)
    # 前进
    driver.forward()# 进入下个链接
    sleep(3)
    # 刷新
    driver.refresh()# 刷新网址
sleep(3)

def test_input(driver):
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)

    input=driver.find_element_by_xpath("//input[@name='t1']")
    input.clear()# 清空输入框

    input.send_keys("水晶之痕：东方大亨")# 输入 水晶之痕：东方大亨
    sleep(3)

def test_radio(driver):
    driver.get("http://ui.yansl.com/#/radio")
    sleep(2)

    radio=driver.find_element_by_xpath("//input[@name='sex'][2]")
    radio.click()# 点击
    sleep(3)

import autoit
from selenium.webdriver import ActionChains

def test_checkbox(driver):
    driver.get("http://ui.yansl.com/#/checkbox")
    sleep(1)

    checkbox = driver.find_element_by_xpath("//label[text()='多选框2']/..//span[1]")
    attribute = checkbox.get_attribute("class")
    if not attribute == 'el-checkbox is-checked':
        checkbox.click()
        sleep(3)
    checkbox = driver.find_element_by_xpath("//label[text()='多选框2']/..//span[1]")
    attribute = checkbox.get_attribute("class")
    if attribute == 'el-checkbox is-checked':
        checkbox.click()
        sleep(2)

def test_select(driver):
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)

    select=driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/div/input")
    select.click()
    sleep(2)

    option=driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]")
    actions = ActionChains(driver)
    actions.move_to_element(option).perform()
    sleep(3)
    option.click()
    sleep(3)

def test_slider(driver):
    driver.get("http://ui.yansl.com/#/slider")
    sleep(2)

    slider=driver.find_element_by_xpath("//*[@id='form']/form/div[5]/div/div/div/div[1]")
    sleep(3)
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(slider,0,-200).perform()
    sleep(3)

def test_time(driver):
    driver.get("http://ui.yansl.com/#/dateTime")
    sleep(2)

    ti=driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div[1]/div/div/input")
    sleep(3)
    ti.clear()
    ti.send_keys("14:25:00")
    sleep(2)

def test_file(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)

    file=driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div/input")
    file.clear()
    file.send_keys("E:\\softwaredate/xpath总.png")

    sleep(3)
from selenium.webdriver.common.keys import Keys


def test_file1(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)
    file = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/div[1]/button/span")
    file.click()
    sleep(2)
    autoit.win_wait("打开", 10)
    sleep(2)
    # autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "E:\\softwaredate/xpath总.png")
    sleep(2)
    autoit.control_click("打开", "Button1")
    sleep(3)

def test_windows(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)

    dang_dang = driver.find_element_by_link_text("当当")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dang_dang).key_up(Keys.CONTROL).perform()
    sleep(2)
    jd = driver.find_element_by_link_text("京东")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(jd).key_up(Keys.CONTROL).perform()
    sleep(2)
    dn = driver.find_element_by_partial_link_text("度娘")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dn).key_up(Keys.CONTROL).perform()
    sleep(2)

    # 获取所有窗口的句柄
    handles = driver.window_handles
    for h in handles:
        # 根据窗口句柄，切换窗口
        driver.switch_to.window(h)
        sleep(2)
        if driver.title.__contains__("京东"):
            break

