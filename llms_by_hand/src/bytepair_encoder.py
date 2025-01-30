import importlib
import tiktoken
from loguru import logger

logger.info("Tiktoken_version:{}",importlib.metadata.version("tiktoken"))

gpt_tokenizer = tiktoken.get_encoding("gpt2")
