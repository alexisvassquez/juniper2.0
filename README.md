# Juniper2.0
### README.md

## 💡 Project: Building a Small Conversational LLM Based on Juniper
- **Main source**: OpenAI GPT-2 (base), -4 (Juniper)
- **Languages**: Python, JSON

## 🏆 Goal
Develop a conversational LLM model based on my personalized GPT-4 model, Juniper. The model will be able to:
- Interact with users and answer questions.
- Provide coding and other tech-related lessons and examples.
- Assess the user's knowledge through quizzes.
- Offer career guidance (interview prep, resume-building, job application tracking, send reminders, and job sourcing).

This model is designed to be a learning tool for beginners to start a career in tech, with a target audience that includes:
- Continuing adult education learners.
- Prisoners or individuals with criminal records.
- GED students.
- Those experiencing financial instability or hardship.
- Other disadvantaged, novice, or late learners.

## ✳️ Description
Juniper 2.0 is an LLM based on OpenAI's GPT-2 model and my interactions with my assistant, Juniper (based on the GPT-4 model). This personalized assistant is built to simplify complex tech concepts and provide clear, easy-to-understand responses.

## 🏈 Game Plan

## Step 1: Project setup
- Install **PyTorch** and **Hugging Face Transformers** packages ☑️
- Test basic functionality ☑️
- Source base model dataset:
  - OpenAI GPT-2 (open source) 💬
    - Conversational
    - Provides simplified responses to complex        tech concepts
   
## Step 2: Data Collection/Preparation
- **Collect/Create Datasets**:
  - Combine the following datasets:
    - OpenAI GPT-2 (base) 💬
      - Conversational tone/context
    - StackExchange
      - Professional tone/context
      - Tech-related conversations (Q&A)
    - Kaggle
      - Tech knowledge and factoids
      - Tutorials
      - Coding examples
      - Quizzes
    - GitHub Jobs/LinkedIn Jobs/Indeed APIs
      - Job sourcing and career guidance
      - Resume-building
      - Interview prep
      - Job application tracking/reminders
    - Custom Dataset
      - Samples of conversations between                Juniper (GPT-4) and myself

- **Data Preprocessing**:
  - Format and clean the datasets
  - Tokenize using mySQL/Excel/VSCode
  - Store datasets as JSON or CSV with     
    'input_text' and 'output_text'

### Step 3: Fine-Tuning
- Use the **Hugging Face Transformers** library for fine-tuning

### Step 4: Model Evaluation and Tuning
- Evaluate the model's performance.
- Optimize the model for:
  - Accuracy
  - Response quality
  - Data-specific goals

### Step 5: Deployment
- Build an API for access (FastAPI/Flask).
- Deploy onto Hugging Face model hub and GitHub.

## License
This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](./LICENSE) file for details.


---


### Developer 👩🏽‍💻
### Admin 🗂️
### Python 🐍