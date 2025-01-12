from llms_by_hand.src.tokenizer_utility import ManualTokenizerUtility
from config import settings

token = ManualTokenizerUtility()

data = token.process_text(token.load_data(token.download_data()))

print(token.vocabulary(data))