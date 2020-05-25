import logging

logger_hander = logging.FileHandler('webapp/logs/app.log', encoding='utf-8')
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
)
logger_hander.setFormatter(logging_format)
