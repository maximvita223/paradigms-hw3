import logging
class Logger():
    _instance = None

    def hello_log(message_user):
        logging.basicConfig(
            level=logging.DEBUG,
            filename = "mylog.log",
            format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
            datefmt='%H:%M:%S',
            )
        logging.info(message_user)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance


log = Logger()
log2 = Logger()

log.hello_log()
print(log is log2)