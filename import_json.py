import json
from transformers import GPT2Tokenizer

# Initialize the tokenizer
GPT2Tokenizer.from_pretrained('distilgpt2')

# Load the dataset (jsonl format)
def load_dataset(filepath):
    with open(filepath, 'r') as file:
        return [json.loads(line) for line in file]

# Tokenize the data
def tokenize_data(data):
    return tokenizer(data['text'],padding="max_length", truncation=True)

# Tokenize the dataset
tokenize_train_data = [tokenize_data(entry) for entry in train_dataset]
