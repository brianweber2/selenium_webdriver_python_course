from logger.logger import logger


def test_logger():
    logger.debug("A debug statement is executed.")
    logger.info("An info statement is executed.")
    logger.warning("Balance too low to purchase.")
    logger.error("Test case failed.")
    logger.critical("Critical message.")
