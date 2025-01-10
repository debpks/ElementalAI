import os
import urllib.request as request
from urllib.parse import urlparse
import re
import requests
from loguru import logger
from config import settings

class ManualTokenizer:
    def __init__(self,data_url:str=settings.data.verdict_url,local_path:str=settings.data.local_path):
        self.url = data_url
        self.local_path = local_path
        
    def validate_url(self,url: str= None)-> bool:
        try:
            if url is None:
                url = self.url
            url_validator = urlparse(url)
            
            if not all([url_validator.scheme,url_validator.netloc,url_validator.path]):
                return False
        except ValueError as e:
            logger.error(f"Invalid URL:{e}")
            return False
        try:
            response_head = requests.head(url)
            if response_head.status_code < 400:
                return True
        except (requests.ConnectionError,requests.Timeout,requests.HTTPError) as e:
            logger.error(f"Error in URL response:{e}")
            return False
        
    def download_data(self,url:str = None,data_path:str=settings.data.local_path)-> bool:
        try:
            if url is None:
                url = self.url
            request.urlretrieve(url,data_path)
        except Exception as e:
            logger.error(f"Error in downloading data:{e}")
            return False
        
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
    