import os
import urllib.request as request
from urllib.parse import urlparse
import re
from loguru import logger
from config import settings

class ManualTokenizer:
    def __init__(self,data_url):
        self.data_url = data_url

    def validate_url(self,url: str)-> bool:
        try:
            url_validator = urlparse(url)
            if not all[url_validator.scheme,url_validator.netloc,url_validator.path]:
                return False
        except ValueError as e:
            logger.error(f"Invalid URL:{e}")
               
    def download_data(self):
        pass
    
    def load_data(self):
        pass
    
    def process_text(self):
        pass
    
    def vocabulary(self):
        pass
    
    def encode_text(self):
        pass
    
    def decode_text(self):
        pass
    