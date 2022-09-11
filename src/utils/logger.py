import logging


class Logger:

    def __init__(self):
        logger = logging.getLogger(__name__)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        if not logger.handlers:
            ch = logging.StreamHandler()
            ch.setFormatter(formatter)
            logger.addHandler(ch)
        logger.setLevel(logging.INFO)
        logger.propagate = False
        self.logger = logger

    def __getattr__(self, item):
        return getattr(self.logger, item)

    def debug(self, msg, *args, **kwargs):
        return self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        return self.logger.info(msg, *args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        return self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        return self.logger.error(msg, *args, **kwargs)
