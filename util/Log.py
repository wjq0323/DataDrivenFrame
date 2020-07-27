#初始化日志 对象

import logging
import logging.config
from config.VarConfig import parentDirPath

#读取日志配置文件
logging.config.fileConfig(parentDirPath + u"\config\Logger.conf")
#选择一个日志格式
logger = logging.getLogger("example02") #01也行

#定义debug级别日志打印方法
def debug(message):
    logger.debug(message)

#定义info级别日志打印方法
def info(message):
    logger.info(message)

#定义warning级别日志打印方法
def warning(message):
    logger.warning(message)