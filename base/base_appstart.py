
#导包
from appium import webdriver
def appStart():
    # desired_caps为字典格式 - 常用参数：
    desired_caps = {}
    # 必填-且正确
    desired_caps['platformName'] = 'Android'
    # 必填-且正确
    desired_caps['platformVersion'] = '5.1'
    # 必填
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # APP包名
    desired_caps['appPackage'] = 'com.yunmall.lc'
    # 启动名
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    #不重置应用
    desired_caps['noreset']=True
    #安装apk文件
    # desired_caps['app']=#绝对路径，存在是不写包名，否则会冲突
    #实例化操作驱动
    app=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    return app
