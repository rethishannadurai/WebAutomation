import inspect
import logging

from allure_commons._allure import step


def customLogger():
    # 1.) This is used to get the  class / method name from where this customLogger method is called
    logname = inspect.stack()[1][3]

    # 2.) Create the logging object and pass the logname in it
    logger = logging.getLogger(logname)

    # 3.) Set the Log level
    logger.setLevel(logging.DEBUG)

    # 4.) Create the filehandler to save the logs in the file
    # filehandler = logging.FileHandler("../../reports/PCM.log", mode='a')

    filehandler = logging.FileHandler("reports/PCM.log", mode='a')

    # 5.) Set the logLevel for filehandler
    filehandler.setLevel(logging.DEBUG)

    # 6.) Create the formatter in which format do you like to save the logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    # 7.) Set the formatter to filehandler
    filehandler.setFormatter(formatter)

    # 8.) Add file handler to logging
    logger.addHandler(filehandler)

    #  9.) Finally return the logging object

    return logger


def allureLogs(text):
    with step(text):
        pass
