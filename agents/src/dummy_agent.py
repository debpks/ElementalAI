#### Hugging Face Serverless API

from math import log
import os
import tokenize
from transformers import AutoTokenizer
from huggingface_hub import InferenceClient,login
from config import settings

HF_TOKEN = settings.HUGGINGFACE.HF_TOKEN

login(token=HF_TOKEN)

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-3B-Instruct")

client_api = InferenceClient("https://jc26mwg228mkj8dw.us-east-1.aws.endpoints.huggingface.cloud")

prompt_raw= [{"role":"user","content":"The capital of France is"}]

print("Prompt_Pre:",prompt_raw)

prompt = tokenizer.apply_chat_template(prompt_raw,tokenize=False)

# prompt = """<|begin_of_text|><|start_header_id|>user<|end_header_id|>""" + prompt + """<|eot_id|><|start_header_id|>assistant<|end_header_id|>"""

print("Prompt_Post:",prompt)

text_gen = client_api.text_generation(prompt, max_new_tokens=50)


print(text_gen)

chat_completion = client_api.chat.completions.create(prompt_raw, max_tokens=50)

print(chat_completion)
print(chat_completion.choices[0].message.content)