#地址薄页面
from util.ParseConfigurationFile import ParseCofigFile
from util.ObjectMap import *

class AddressBookPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parseCF = ParseCofigFile()
        self.addContactOptions = self.parseCF.getItemsSection("126mail_addContactsPage")
        print(self.addContactOptions)

    def createContactPersonButton(self):
        try:
            #获得新建联系人按钮
            locateType , locatorExperssion = self.addContactOptions["addContactsPage.createContactsBtn".lower()].split(">")
            element = getElement(self.driver,locateType,locatorExperssion)
            return element
        except Exception as e:
            raise e

    def contactPersonName(self):
        try:
            #获得新建联系人界面中的姓名输入框
            locateType,locatorExperssion = self.addContactOptions["addContactsPage.contactPersonName".lower()].split(">")
            element = getElement(self.driver,locateType,locatorExperssion)
            return element
        except Exception as e:
            raise e

    def contactPersonEmail(self):
        try:
            #获得新建联系人界面中的电子邮件输入框
            locateType,locatorExperssion = self.addContactOptions["addContactsPage.contactPersonEmail".lower()].split(">")
            element = getElement(self.driver,locateType,locatorExperssion)
            return element
        except Exception as e:
            raise e

    def starContacts(self):
        try:
            #获得新建联系人界面中的星标联系人输入框
            locateType,locatorExperssion = self.addContactOptions["addContactsPage.starContacts".lower()].split(">")
            element = getElement(self.driver,locateType,locatorExperssion)
            return element
        except Exception as e:
            raise e

    def contactPersonMobile(self):
        try:
            #获得新建联系人界面中的联系人电话输入框
            locateType,locatorExperssion = self.addContactOptions["addContactsPage.contactPersonMobile".lower()].split(">")
            element = getElement(self.driver,locateType,locatorExperssion)
            return element
        except Exception as e:
            raise e

    def contactPersonComment(self):
        try:
            #获得新建联系人界面中的联系人备注输入框
            locateType,locatorExperssion = self.addContactOptions["addContactsPage.contactPersonComment".lower()].split(">")
            element = getElement(self.driver,locateType,locatorExperssion)
            return element
        except Exception as e:
            raise e

    def savecontactPerson(self):
        try:
            #获得新建联系人界面中的保存联系人按钮
            locateType,locatorExperssion = self.addContactOptions["addContactsPage.savecontactPerson".lower()].split(">")
            element = getElement(self.driver,locateType,locatorExperssion)
            return element
        except Exception as e:
            raise e