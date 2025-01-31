from random import shuffle
from llms_by_hand.src import dataloader
from llms_by_hand.src.manual_tokenizer import TokenizerV1
from config import settings
from llms_by_hand.src.bytepair_encoder import gpt_tokenizer
from llms_by_hand.src.dataloader import Dataloader,GPTDataset
token = TokenizerV1()
query = "I HAD always thought Jack Gisburn rather a cheap"
token.encode_text(query)
token.decode_text([486, 431, 42, 959, 516, 401, 763, 8, 155])

gpt_encode = gpt_tokenizer.encode(query,allowed_special={"<|endoftext|>"},disallowed_special=None)
print('gpt_encode:', gpt_encode)

print(gpt_tokenizer.decode(gpt_encode))

with open("llms_by_hand/data/the-verdict.txt","r") as f:
    data = f.read()

dataset = GPTDataset(data,gpt_tokenizer,max_length=4,stride=1)

dataloader_v1 = Dataloader(dataset,batch_size=1,num_workers=5,shuffle=False)