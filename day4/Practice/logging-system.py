# Design logging system that support scalability
from abc import ABC , abstractmethod
class Logger(ABC):
    @abstractmethod
    def log_message(self,message:str):
        pass 

class FileLogger(Logger):
    def __init__(self,sms):
        self.sms = sms 
    
    def log_message(self, message):
        print("Logging data in file logger.")
        
# DatabaseLogger
# ConsoleLogger

class LogService:
    def log_message(logger: Logger):
        logger.log_message("hey there")


logger = LogService
logger.log_message(FileLogger("sms"))


# Extension : Later support : 
# ElasticSearchLogger
    
