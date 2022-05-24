import logging

class LoggingConfig():
    # 构造函数
    def __init__(self,logging,path):
        self.logging=logging
        self.path=path
    # logging初始化配置，并返回logger实例化对象，供外部使用
    def logging_config(self):
        # 实例化 logger
        logger = self.logging.getLogger(__name__)
        logger.setLevel(level =  self.logging.INFO)
        # 实例化 handler
        handler =  self.logging.FileHandler(self.path)
        handler.setLevel( self.logging.INFO)
        # 判断当前日志对象中是否有处理器，如果没有，则添加处理器
        if not logger.handlers:
            formatter =  self.logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            # 实例化 console
            console =  self.logging.StreamHandler()
            console.setLevel( self.logging.INFO)
            formatterConsole =  self.logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console.setFormatter(formatterConsole)

            logger.addHandler(handler)
            logger.addHandler(console)

            # logger.info("Start print log")
            # logger.debug("Do something")
            # logger.warning("Something maybe fail.")
            # logger.info("Finish")
            
        return logger