#在操作前，先进行所需用到的数据位置整理定位

from selenium.webdriver.common.by import By
#BY.ID为元组数据类型，数据解析的时候会拆分

#点击我
login_me=(By.ID,'com.yunmall.lc:id/tab_me')

#点击已有账号，去登录
login_user_exists=(By.XPATH,'//*[@text="已有账号，去登录"]')

#输入账号
login_user=(By.ID,'com.yunmall.lc:id/logon_account_textview')

#输入密码
login_password=(By.ID,'com.yunmall.lc:id/logon_password_textview')

#点击登录
login_go=(By.ID,'com.yunmall.lc:id/logon_button')

#需要断言是否登录成功，获取登录后文本内容，定位账号位置
login_text=(By.ID,'com.yunmall.lc:id/tv_user_nikename')

#设置
login_setting=(By.ID,'com.yunmall.lc:id/ymtitlebar_left_btn_image')

#需要拖拽，定位 图片显示 以及 修改密码 位置
login_picture=(By.XPATH,'//*[@text="图片显示"]')
login_change_password=(By.XPATH,'//*[@text="修改密码"]')

#定位退出按钮
login_out=(By.XPATH,'//*[@text="退出"]')

#定位确认退出按钮
login_againout=(By.XPATH,'//*[@text="确认"]')