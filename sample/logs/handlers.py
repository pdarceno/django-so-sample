from logging import FileHandler, INFO, ERROR, DEBUG

class AppFileHandler(FileHandler):
    def __init__(self, filename, loglevel, mode, encoding, delay):
        super().__init__(filename, mode, encoding, delay)
        self.loglevel = loglevel
    
    def emit(self, record):
        if not record.levelno == self.loglevel:
            return
        super().emit(record)

class AppDebugFileHandler(AppFileHandler):
    def __init__(self, filename, mode='a', encoding=None, delay=False):
        super().__init__(filename, DEBUG, mode, encoding, delay)

class AppErrorFileHandler(AppFileHandler):
    def __init__(self, filename, mode='a', encoding=None, delay=False):
        super().__init__(filename, ERROR, mode, encoding, delay)

class AppInfoFileHandler(AppFileHandler):
    def __init__(self, filename, mode='a', encoding=None, delay=False):
        super().__init__(filename, INFO, mode, encoding, delay)