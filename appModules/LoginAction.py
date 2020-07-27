
#encoding = utf-8
# 登录模块的封装
from pageObjects.LoginPage import LoginPage
from selenium import webdriver
import time

class LoginAction(object):

     def __init__(self):
         print("login...")

     def login(driver,username,password):
         try:
             login = LoginPage(driver)
             #将当前焦点切换到登录模块的frame中
             login.switchToFrame()
             login.userNameObj().send_keys(username)
             login.passwordObj().send_keys(password)
             login.loginButton().click()
             #切换到默认窗体
             login.switchToDefaultFrame()
         except Exception as e:
             raise e

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://mail.126.com")
    time.sleep(5)
    LoginAction.login(driver,username="111@126.com",password="111")
    time.sleep(5)
    driver.quit()

