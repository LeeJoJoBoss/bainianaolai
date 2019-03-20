#将需要用到的操作方法整理
#设置一个通用数据
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver=driver
    #定位元素
    def base_find_element(self,location,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda l:l.find_element(*location))
    #点击
    def base_click(self,location):
        self.base_find_element(location).click()

    #输入
    #需要注意的，输入框最好先进行清空再进行数据填入
    def base_input(self,location,values):
        element=self.base_find_element(location)
        element.clear()
        element.send_keys(values)

    #获取文本信息
    def base_get_text(self,location):
        return self.base_find_element(location).text

    #拖拽
    def base_drag_and_drop(self,aa,bb):
        self.driver.drag_and_drop(aa,bb)