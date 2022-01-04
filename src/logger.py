import logging


class Log:

    def get_logger(self, name):
        self.logger = logging.getLogger(name)
        return self.logger
