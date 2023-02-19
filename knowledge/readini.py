from configparser import ConfigParser
import os

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../Myconfig.ini")

conf = ConfigParser()
# 加载配置文件
conf.read(file, encoding="utf-8")
# 按需读取对应需要的字段:get,默认读取出来的文件均为字符串
log_name = conf.get("log", "name")
print(type(log_name))

