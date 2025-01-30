import os
import urllib.request as request
from urllib.parse import urlparse
import re
from collections import Counter
import requests
import traceback
from loguru import logger
from config import settings

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

class ManualTokenizerUtil:
    
    def __init__(self,data_url:str=settings.data.verdict_url,local_path:str=settings.data.local_path,download:bool=True):
        self.url = data_url
        self.local_path = local_path
        self.download = download
        assert self.validate_url(self.url)
        
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
        
    def load_data(self,local_path:str=None)-> str:
        if self.download:

            local_path = self.download_data(self.url)
        try:
            if local_path is None:
                local_path = self.local_path
            with open(local_path,"r") as f:
                data = f.read()
                return data
        except Exception:   
            logger.error(f"Error in loading data:{traceback.format_exc()}")
            return str(False)

    def process_text(self,text:str)-> list:
        text = text.lower()
        text = re.split(r'[,.:;?_!"()--\s]',text)
        text = [word for word in text if word != ""]
        return text
    
    def vocabulary(self,text: list)-> dict:
        text = sorted(set(text))
        text.extend(["<|unk|>","<|endoftext|>"])
        vocab = {wrd:idx for idx,wrd in enumerate(text)}
        idx2word = {idx:wrd for wrd,idx in vocab.items()}
        return vocab,idx2word
    