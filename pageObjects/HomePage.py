#主页的页面对象
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseCofigFile

class HomePage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()

    def addressLink(self):
        try:
            #从定位表达式配置文件中读取定位通讯录按钮的定位方式和表达式
            locateType ,locatorExpression = self.parseCF.getOptionValue("126mail_homePage","homepage.addressbook".lower()).split(">")
            #获取通讯录页面元素
            elementObj = getElement(self.driver,locateType,locatorExpression)
            return  elementObj
        except Exception as e:
            raise e

