"""
高级应用
1 记录器
2 处理器
2.1 Handles 可以把日志分发到不同目的地
    可以是文件、标准输出、邮件、socket等
3 过滤器
4 格式化器
"""
import logging


def test1():
    logging.warning("This is warning")
    logging.error("This is error")
    logging.critical("This is critical")


def test2():
    logging.basicConfig(format="%(pathname)s\n"
                               "%(asctime)s | %(levelname)s | "
                               "%(filename)s-%(lineno)s: "
                               "%(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
    logging.debug("This is debug")


def test3():
    # 单例对象
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler()
    logger.removeHandler()
    sh = logging.StreamHandler(stream=None)
    # delay表示缓存与否
    fh = logging.FileHandler('example.log', mode='w', encoding='UTF-8',
                             delay=False)
    sh.setFormatter()


if __name__ == '__main__':
    test2()
