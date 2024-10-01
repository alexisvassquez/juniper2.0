from datasets import load_dataset

# Load OpenWebText dataset
dataset = load_dataset("openwebtext")

# Inspect the first few samples
print(dataset['train'][0])

from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrain("distilgpt2")

def tokenize_function(examples):
	return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512) 

tokenized_datasets = dataset.map(tokenize_function, batched=True)

from transformers import GPT2LMHeadModel, Trainer, TrainingArguments

model = GPT2LMHeadModel.from_pretrained("distilgpt2")

training_args = TrainingArguments(
	output_dir="./results",
	overwrite_output_dir=True,
	num_train_epochs=1,
	per_device_train_batch_size=8,
	save_steps=10_000,
	save_total_limit=2,
	logging_dir="./logs",
	logging_steps=500,
)

trainer = Trainer(
	model=model,
	args=training_args,
	train_dataset=tokenized_datasets["train"],
	eval_dataset=tokenized_datasets["train"]
)

trainer.train()
trainer.save_model("./fine_tuned_model")

from transformers import pipeline

generator = pipeline("text-generation", model="./fine_tuned_model")
result = generator("Juniper is an intelligent assistant that", max_length=50)
print(result)
