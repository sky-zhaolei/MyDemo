"""
公共日志模块，logging

"""
import logging
from handle_config import conf


class MyLogger(logging.Logger):

    def __init__(self, name, level=logging.INFO, file=None):
        # 设置输出级别，输出渠道，输出格式
        super().__init__(name, level)
        # 设置日志输出格式
        fmt = '%(asctime)s - %(name)s %(levelname)s %(filename)s %(lineno)d 行：%(message)s'
        famtter = logging.Formatter(fmt)

        # 控制台渠道
        handler1 = logging.StreamHandler()
        handler1.setFormatter(famtter)
        self.addHandler(handler1)

        # 文件渠道
        if file :
            handler2 = logging.FileHandler(file, encoding="utf-8")
            handler2.setFormatter(famtter)
            self.addHandler(handler2)


# 判断是否需要输出日志到文件
if conf.get("log", "file_ok"):
    file_name = conf.get("log", "filename")
else:
    file_name = None


logger = MyLogger(conf.get("log", "name"), level=conf.get("log", "leaver"),  file=file_name)


if __name__ == '__main__':
    logger.info("试一下")

#试试看

