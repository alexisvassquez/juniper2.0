from transformers import pipeline

# Load fine-tuned model
generator = pipeline("text-generation", model="./fine_tuned_model")

# Example usage
prompt = "Juniper is an intelligent assistant that"
result = generator(prompt, max_length=50)
print(result[0]['generated_text'])


