from configparser import ConfigParser
from config.VarConfig import pageElementLoctorPath
#解析存储定位元素的定位表达式文件 以便获取定位表达式
class ParseCofigFile(object):

    def __init__(self):
        self.cf = ConfigParser() #configparser模块支持读取.conf和.ini等类型的文件，在文件夹新建一个.ini文件，写入一些信息，
        self.cf.read(pageElementLoctorPath,encoding= "utf-8")#得到配置文件的路径

    def getItemsSection(self,sectionName):
        #获取配置文件中指定section下所有的option键值对
        #并以字典的类型返回给调用者

        '''
        注意：使用self.cf.items(sectionName)此种方法获得的配置文件中的options内容均转换为小写
        比如 loginPage.frame 变成loginpage.frame
        '''
        optionsDict = dict(self.cf.items(sectionName))
        return optionsDict

    def getOptionValue(self,sectionName,optionName):
        #获取指定section下指定的option值
        value = self.cf.get(sectionName,optionName)
        return value

if __name__ == '__main__':
    pc = ParseCofigFile()
    print(pc.getItemsSection("126mail_login"))
    print(pc.getOptionValue("126mail_login","loginPage.frameNumber"))
