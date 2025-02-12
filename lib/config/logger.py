#   Python's logger module is used to log messages to the console and to a file.

#   Importing required dependencies
import logging as Log

class LogWatcher(object):
    def __init__(self):
        self.log = Log.getLogger(__name__)
        self.log.setLevel(Log.DEBUG)

    def setup(self, name):

        #   Initializing the file handler
        file_handler = Log.FileHandler(name)
        file_handler.setLevel(Log.DEBUG)
        file_handler.setLevel(Log.ERROR)

        #   Initializing the console handler
        console_handler = Log.StreamHandler()
        console_handler.setLevel(Log.INFO)

        #   Initializing the formatter
        formatter = Log.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        #   Adding the handlers to the logger -- issues below
        self.log.addHandler(file_handler)
        self.log.addHandler(console_handler)

        #   Log the application is running
        self.log.info(f"{name} is running")

class AppWatcher(LogWatcher):

    def __init__(self):
        super().__init__()

        self.name = "app.log"

class CookieWatcher(LogWatcher):

    def __init__(self):
        super().__init__()

        
        
