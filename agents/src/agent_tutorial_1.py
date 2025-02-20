from transformers import AutoTokenizer

# Load the tokenizer
model_id = "mistralai/Mistral-7B-Instruct-v0.1"
model_id = "HuggingFaceTB/SmolLM2-1.7B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)

chat = [
  {"role": "user", "content": "Hello, how are you?"},
  {"role": "assistant", "content": "I'm doing great. How can I help you today?"},
  {"role": "user", "content": "I'd like to show off how chat templating works!"},
]

# Tokenize the chat

print(tokenizer.apply_chat_template(chat,tokenize=False,add_generation_prompt=True))
