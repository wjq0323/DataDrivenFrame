from pageObjects.HomePage import HomePage
from pageObjects.AddressBookPage import AddressBookPage
import traceback
import time

class AddContactPerson(object):
    def __init__(self):
        print("add contact person")

    @staticmethod
    def add(driver, contactName, contactEmail, isStar, contactPhone, contactComment):
        try:
            #创建主页实例对象
            hp = HomePage(driver)
            # 单机通讯录链接
            hp.addressLink().click()
            time.sleep(3)
            #创建添加联系人页实例对象
            apb = AddressBookPage(driver)
            apb.createContactPersonButton().click()
            if contactName:
                apb.contactPersonName().send_keys(contactName) #非必填
            apb.contactPersonEmail().send_keys(contactEmail)#必填项
            if isStar == u"是":
                apb.starContacts().click()
            if contactPhone:
                apb.contactPersonMobile().send_keys(contactPhone)
            if contactComment:
                apb.contactPersonComment().send_keys(contactComment)
            apb.savecontactPerson().click()
        except Exception as e:
            raise e

if __name__ == '__main__':
    from appModules.LoginAction import LoginAction
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.get("http://mail.126.com")
    time.sleep(5)
    LoginAction.login(driver,username="111@126.com",password="111")
    time.sleep(5)
    AddContactPerson.add(driver,"zs","zs@qq.com",u"是","","")
    time.sleep(3)
    assert ("zs" in driver.page_source)
    driver.quit()