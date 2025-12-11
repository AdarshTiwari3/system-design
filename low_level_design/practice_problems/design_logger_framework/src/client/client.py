"""Client"""
from core.log_manager import LogManager
from enums.log_level import LogLevel
from appenders.console_log_appender import ConsoleAppender
from appenders.file_log_appender import FileAppender
from strategies.json_formatter_strategy import JsonFormatterStrategy



def main():
    log_manager = LogManager.get_instance()
    logger = log_manager.get_logger("payment.service")

    logger.set_level(LogLevel.DEBUG)

   
    console_text = ConsoleAppender()
    file_text = FileAppender("logs/payment.log")

    logger.add_appender(console_text)
    logger.add_appender(file_text)

    logger.debug("Debugging payment flow...")
    logger.info("Payment request created")
    logger.warn("High latency detected")
    logger.error("Payment failed")
    logger.fatal("Critical failure: shutting down system")

    # --- JSON format appenders ---
    json_formatter = JsonFormatterStrategy()
    console_json = ConsoleAppender(json_formatter)
    file_json = FileAppender("logs/payment.json", json_formatter)

    logger.add_appender(console_json)
    logger.add_appender(file_json)

    logger.info("Payment started")
    logger.error("Payment failed due to insufficient balance")
