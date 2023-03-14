"""
日志名字
日志级别：debug，info，warning，error，critical（fatal）
日志渠道：控制台、文件
日志内容：

"""
import logging

# 定义日志收集器
logger = logging.getLogger("日志收集器的名称")

# 设定日志收集器的收集等级
logger.setLevel(logging.INFO)

# 设定日志输出渠道
handler1 = logging.StreamHandler()
handler2 = logging.FileHandler("py_log.log", encoding="utf-8")

# 设置输出日志格式
fmt = '%(asctime)s - %(name)s %(levelname)s %(filename)s %(lineno)d 行：%(message)s'
famtter = logging.Formatter(fmt)

handler1.setFormatter(famtter)
handler2.setFormatter(famtter)
logger.addHandler(handler1)
logger.addHandler(handler2)

logger.info("试一试好了没1")
