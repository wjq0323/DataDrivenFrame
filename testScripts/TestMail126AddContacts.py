#编写具体的操作代码
from util.ParseExcel import ParseExcel
from appModules.LoginAction import *
from pageObjects.LoginPage import *
import time
from config.VarConfig import *
from appModules.LoginAction import LoginAction
from appModules.AddContactPersonAction import AddContactPerson
import traceback
from selenium.webdriver.chrome.options import Options
from util.Log import *

#实例化解析对象
excelObj = ParseExcel()
#将excel数据加载到内存
excelObj.loadWorkBook(dataFilePath)

def LaunchBrowser():
    #创建Chrome浏览器的一个Options实例对象
    chrome_options = Options()
    #向Options实例中添加禁用扩展插件的设置参数项
    chrome_options.add_argument("--disable-extensions")
    #添加屏蔽 --ignore-certificate-errors提示信息的设置参数项
    chrome_options.add_experimental_option("excludeSwithches",["ignore - certificate -errors"])
    chrome_options.add_argument('-- start - maxmized') #一启动就最大化
    driver = webdriver.Chrome()
    driver.get("http://mail.126.com")
    time.sleep(3)
    return driver

def test126MailAddContacts():
    logging.info(u"126邮箱添加联系人数据驱动测试开始...")
    try:
        userSheet = excelObj.getSheetByName(u"126账号")
        #获取126账号sheet中是否执行列
        isExuteUser = excelObj.getColumn(userSheet,account_isExecute)
        # 获取126账号sheet中的数据表列
        dataBookColumn = excelObj.getColumn(userSheet,account_dataBook)
        print("测试为126邮箱添加联系人执行开始")
        for idx ,i in enumerate(isExuteUser[1:]):
            #循环遍历 为需要执行的账号添加联系人
            if i.value == 'y': #表示要执行
                userRow = excelObj.getRow(userSheet,idx+2) #得到第i行的数据 为什么是加2呢
                #获取第i行中的用户名和密码
                username = userRow[account_username - 1].value
                password = str(userRow[account_password - 1].value)
                print(username,password)

                driver = LaunchBrowser()
                logging.info(u"启动浏览器，访问126邮箱主页...")

                #登录126邮箱
                LoginAction.login(driver,username,password)
                time.sleep(5)
                try:
                    #断言登录后跳转页面的标题是否包含"网易邮箱"
                    assert(u"收 信" in driver.page_source)
                    logging.info(u"用户%s登录后，断言页面关键字'收信'成功" % username)
                except AssertionError as e:
                    logging.debug(u"用户%s登录后，断言页面关键字'收信'失败" u"异常信息：%s" %(username,str(traceback.format_exc())))
                #获取为第idx + 2 行用户添加的联系人的数据表sheet名
                dataBookName = dataBookColumn[idx+1].value
                #获取对应的数据表对象
                dataSheet = excelObj.getSheetByName(dataBookName)
                #获取联系人数据表中是否执行列对象
                isExuteData = excelObj.getColumn(dataSheet,contacts_isExecute)
                contactNum = 0 #记录添加成功的联系人的个数
                isExecuteNum = 0 #记录需要执行联系人的个数
                for id,data in enumerate(isExuteData[1:]):
                    #循环遍历是否执行添加联系人列 如果被设置为添加 则进行添加
                    if data.value == "y":
                        #如果是第id行的联系人呗设置为执行 则isExecuteNum自增1
                        isExecuteNum += 1
                        #获取联系人表第id+2行对象
                        rowContent = excelObj.getRow(dataSheet,id+2)
                        #获取联系人姓名 \邮箱等
                        contactPersonName = rowContent[contacts_contactPersonName - 1].value
                        contactPersonEmail = rowContent[contacts_contactPersonEmail -1].value
                        isStar = rowContent[contacts_isStar - 1].value
                        contactPersonPhone = rowContent[contacts_contactPersonMoblie - 1].value
                        contactPersoncComment = rowContent[contacts_contactPersonComment - 1].value
                        assertKeyWord = rowContent[contacts_assertKeyWords - 1].value
                        print(contactPersonName,contactPersonEmail,assertKeyWord,contactPersonPhone,contactPersoncComment,isStar)

                        #执行新建联系人操作
                        AddContactPerson.add(driver,contactPersonName,contactPersonEmail,isStar,contactPersonPhone,contactPersoncComment)
                        time.sleep(1)

                        logging.info(u"添加联系人 %s 成功" % contactPersonName)

                        #在联系人工作表中写入添加联系人的执行时间
                        excelObj.writeCellCurrentTime(dataSheet,rowNo=id+2,colsNo = contacts_runTime)
                        try:
                            assert assertKeyWord in driver.page_source
                        except AssertionError as e:
                            #断言失败 在联系人工作表中写入添加联系人测试失败信息
                            excelObj.writeCell(dataSheet,"faild",rowNo = id+2,colsNo = contacts_testResult,style = "red"  )
                            logging.info(u"断言关键字 %s 失败" % assertKeyWord)
                        else:
                            #断言成功 写入添加联系人成功信息
                            excelObj.writeCell(dataSheet,"pass",rowNo = id + 2,colsNo = contacts_testResult,style = "green" )
                            contactNum += 1
                            logging.info(u"断言关键字 %s 成功" % assertKeyWord)
                    else:
                        logging.info(u"联系人 %s 被忽略执行" % contactPersonName)
                print("contactNum:",contactNum,"isExcuteNum:",isExecuteNum)

            if contactNum == isExecuteNum:
                #则成功
                excelObj.writeCell(dataSheet,"pass",rowNo = idx + 2,colsNo = account_testResult,style = "green")
                logging.info(u"为用户 %s 添加%d个联系人，%d个成功" % (username,isExecuteNum,contactNum))
                print("为用户",username,"添加",contactNum,"个联系人，测试通过" )
            else:
                excelObj.writeCell(dataSheet, "faild", rowNo=idx + 2, colsNo=account_testResult, style="red")
                logging.info(u"用户 %s 被设置为忽略执行" % excelObj.getCellOfValue(userSheet,rowNo=idx + 2, colsNo=account_username))
            driver.quit()
    except Exception as  e:
        logging.debug(u"数据驱动框架主程序发生异常，异常信息为：%s" %str(traceback.print_exc()))
        print("数据驱动框架主程序发生异常，异常信息为：")
        print(traceback.print_exc())

if __name__ == '__main__':
    test126MailAddContacts()
    print("126登录成功")