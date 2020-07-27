#用于编写126邮箱登录页面的页面元素对象
from util.ObjectMap import *
from util.ParseConfigurationFile import ParseCofigFile
class LoginPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseCofigFile() #获取配置文件
        self.loginOptions = self.parseCF.getItemsSection("126mail_login") #获取配置文件
        print("loginoptions",self.loginOptions)

    def switchToFrame(self):
        # self.driver.switch_to.frame(frameNumber)
        try:
            #从定位表达式配置文件中读取frame的定位表达式
            frameNumber = int(self.loginOptions["loginPage.frameNumber".lower()])
            print(frameNumber)
            self.driver.switch_to.frame(frameNumber)
        except Exception as e:
            raise e

    def switchToDefaultFrame(self):
        self.driver.switch_to.default_content( )

    def userNameObj(self):
        try:
            #获取登录页面的用户名输入框页面对象，并返回给调用者
            locateType ,locatorExpression = self.loginOptions["loginPage.username".lower()].split(">")
            # elementObj = getElement(self.driver,"xpath",'//input[@name = "email"]')
            elementObj = getElement(self.driver, locateType,locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def passwordObj(self):
        try:
            #获取登录页面的密码输入框页面对象，并返回给调用者
            locateType, locatorExpression = self.loginOptions["loginPage.password".lower()].split(">")
            #elementObj = getElement(self.driver,"xpath","//input[@name='password']")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception as e:
            raise e

    def loginButton(self):
        try:
            #获取登录页面的登录按钮页面对象，并返回给调用者
            locateType, locatorExpression = self.loginOptions["loginPage.loginbutton".lower()].split(">")
            # elementObj = getElement(self.driver,"id","dologin")
            elementObj = getElement(self.driver, locateType, locatorExpression)
            return elementObj
        except Exception  as e:
            raise e

if __name__ == '__main__':
    #测试代码
    from selenium import webdriver
    import  time
    driver = webdriver.Chrome()
    driver.get("http://mail.126.com")
    login = LoginPage(driver)
    time.sleep(10)
    login.switchToFrame()
    #输入用户名
    login.userNameObj().send_keys("111@126.com")
    login.passwordObj().send_keys("111")
    login.loginButton().click()
    time.sleep(10)
    login.switchToDefaultFrame()
    assert u"未读邮件" in driver.page_source
    driver.quit()

