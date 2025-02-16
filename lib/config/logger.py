#  Handling the application logging
#   Based Basic Python logging concepts by  https://last9.io/blog/python-logging-best-practices/#basic-python-logging-concepts
#   Importing required dependencies
import logging as Log
from typing import Optional, Union

class Logger(object):

    """
        Logger class to handle application logging
    """
    def __init__(self, name:Optional[str] = None):

        """
            *   Initialize the logger
            *   Set the logging level to DEBUG
            *   Set the logging format
            *   Set the logging handler
            *   param name: str - default: Class name
        """
        
        #   Initialize the handler
        self.name = name or self.__class__.__name__
        
        self.log = Log.getLogger(f"{self.name}")
        self.log.setLevel(Log.DEBUG)
        
        #   Initialize the Flags
        self.file_handler = False
        self.console_handler = False

    def SetupHandler(self, handler:Union[Log.FileHandler | Log.StreamHandler]):
        
        """
            *   Setup the Log handler
            *   param handler:[Log.FileHandler, Log.StreamHandler]
        """
        #   Initializing the formatter
        formatter = Log.Formatter('%(asctime)s - %(levelname)s -\t %(name)s -\t %(message)s')
        handler.setFormatter(formatter)
        self.log.addHandler(handler)
    
    def ConsoleHandler(self):


        """
            *   Add a console handler to the logger
        """
        
        #   Ensure that the Flag is not set to True
        if not self.console_handler:
            
            #   Set the flag
            self.console_handler = True
            
            #   Initializing the handler
            handler = Log.StreamHandler()
            self.SetupHandler(handler)

            #   Send message to the console
            self.log.info(f"{self.name} has been initialized.")

    def FileHandler(self):

        """
            *   Add a file handler to the logger
        """
        #   Ensure that the Flag is not set to True
        if not self.file_handler:

            #   Initializing the handler
            handler = Log.FileHandler(f"{self.name}.log")
            self.SetupHandler(handler)

            #   Send message to the console
            self.log.info(f"{self.name} has been initialized.")
            
            #   Set the flag
            self.file_handler = True

        else:
            self.log.warning(f"{self.name} Console handler already initialized")

    def info(self, message):
        self.log.info(message)
    
    def error(self, message):
        self.log.error(message)
    
    def warn(self, message):
        self.log.warning(message)
    
    def debug(self, message):
        self.log.debug(message)

class AppWatcher(Logger):

    def __init__(self):
        super().__init__(name=f"{self.__class__.__name__}")
        

class CookieWatcher(Logger):

    def __init__(self):
        super().__init__(name=f"{self.__class__.__name__}")

        
        
