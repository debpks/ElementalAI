import importlib
import tiktoken
from loguru import logger
from transformers import AutoTokenizer, GPT2Tokenizer


logger.info("Tiktoken_version:{}",importlib.metadata.version("tiktoken"))

gpt_tokenizer = tiktoken.get_encoding("gpt2")

# a = AutoTokenizer()
corpus = [
    "This is the Hugging Face Course.",
    "This chapter is about tokenization.",
    "This section shows several tokenizer algorithms.",
    "Hopefully, you will be able to understand how they are trained and generate tokens.",
]

tokenizer = AutoTokenizer.from_pretrained('gpt2')

#### We Will Train a Tokenizer on the Corpus
#### 