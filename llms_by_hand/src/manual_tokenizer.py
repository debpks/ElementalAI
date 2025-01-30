from math import log
from llms_by_hand.src.tokenizer_utility import ManualTokenizerUtil
from loguru import logger

tokenizer_util = ManualTokenizerUtil()

class TokenizerV1():
    def __init__(self):
        self.vocab,self.idx2word = tokenizer_util.vocabulary(tokenizer_util.process_text(tokenizer_util.load_data()))
        
        
    def encode_text(self,text:str)-> list[int]:
        text = tokenizer_util.process_text(text)
        text = [t if t in self.vocab else "<|unk|>" for t in text]
        encoded_text = [self.vocab[word] for word in text]
        return encoded_text
    
    def decode_text(self,ids: list)-> list[str]:
        text = [self.idx2word[idx] for idx in ids]
        return text