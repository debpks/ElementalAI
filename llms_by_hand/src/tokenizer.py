import os
import urllib.request as request
from urllib.parse import urlparse
import re
import requests
import traceback
from loguru import logger
from config import settings

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

class ManualTokenizer:
    def __init__(self,data_url:str=settings.data.verdict_url,local_path:str=settings.data.local_path):
        self.url = data_url
        self.local_path = local_path
        
    def validate_url(self,url: str= None)-> bool:
        try:
            if url is None:
                url = self.url
            url_validator = urlparse(url)
            
            if not all([url_validator.scheme,url_validator.netloc]):
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
            logger.info(settings.data.verdict_url)
            output_loc = ROOT_DIR+"/"+data_path+os.path.split(url)[1]
            
            if url is None:
                url = self.url
            
            request.urlretrieve(url,output_loc)
            return output_loc
        except Exception:
            logger.error(f"Error in downloading data:{traceback.format_exc()}")
            return False
        
    def load_data(self,local_path:str)-> str:
        try:
            with open(local_path,"r") as f:
                data = f.read()
                return data
        except Exception:   
            logger.error(f"Error in loading data:{traceback.format_exc()}")
            return str(False)

    def process_text(self,text:str):
        text = text.lower()
        text = re.split(r'[,.:;?_!"()--\s]',text)
        return text

    def vocabulary(self): 
        pass
    
    def encode_text(self):
        pass
    
    def decode_text(self):
        pass
    