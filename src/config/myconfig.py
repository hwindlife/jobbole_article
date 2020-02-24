#-*-encoding=utf-8-*-
# 测试ConfigParser
import os
from configparser import ConfigParser

# 初始化
conf = ConfigParser()

# 配置文件的绝对路径
conf_path = os.path.dirname(os.path.realpath(__file__)) + "/myconfig.ini"
print(conf_path)
# 读取配置文件
conf.read(conf_path)

"""
读取配置信息
"""
# 查看配置中的所有section
sections = conf.sections()
print(sections)

# 返回所有section和序列
sub_conf = conf.options("server")
print(sub_conf)

# 返回section中option的值
value_sub_conf = conf.get("server", "pro_server")
print(value_sub_conf)
