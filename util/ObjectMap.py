#本页面用于实现定位页面元素的公共方法

from  selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#获取单个页面元素对象
def getElement(driver,locateType,locatorExpression):
    try:
        element = WebDriverWait(driver,30).until(lambda x:x.find_element(by = locateType, value = locatorExpression))
        #WebDriverWait是显示等待
        # sleep是强制等待设置固定休眠时间，单位为秒。 由python的time包提供, 导入 time 包后就可以使用。缺点：不智能，使用太多的sleep会影响脚本运行速度。
        # 隐式等待:implicitly_wait() 它不针对某一个元素，是全局元素等待，即在定位元素时，需要等待页面全部元素加载完成，才会执行下一个语句。如果超出了设置时间的则抛出异常。
        # 缺点：当页面某些js无法加载，但是想找的元素已经出来了，它还是会继续等待，直到页面加载完成（浏览器标签左上角圈圈不再转），才会执行下一句。某些情况下会影响脚本执行速度
        return element
    except Exception as e:
        raise e

#获取多个页面元素对象
def getElements(driver,locateType,locatorExpression):
    try:
        elements = WebDriverWait(driver,30).until(lambda x:x.find_elements(by = locateType, value = locatorExpression))
        return elements
    except Exception as e:
        raise e

if __name__ == '__main__':
    #进行单元测试
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver,"id","kw")   #定位id为kw的元素
    print(searchBox.tag_name)
    aList = getElements(driver,"tag name","a") #定位所有标签为a的元素
    print(len(aList))
    driver.quit()
