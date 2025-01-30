from llms_by_hand.src.manual_tokenizer import TokenizerV1
from config import settings


token = TokenizerV1()
token.encode_text("I HAD always thought Jack Gisburn rather a cheap")
token.decode_text([486, 431, 42, 959, 516, 401, 763, 8, 155])

