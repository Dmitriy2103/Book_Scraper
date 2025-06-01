import logging

def setup_logger():
    logger = logging.getLogger("BookScraper")
    logger.setLevel(logging.DEBUG)
    
    file_handler = logging.FileHandler('logs/scraper.log')
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)