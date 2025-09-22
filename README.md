🚀 GitHub Tag Generator with T5 + PEFT (LoRA)
This project fine-tunes a T5-small model using PEFT with LoRA (Low-Rank Adaptation) to automatically generate relevant tags for GitHub repository descriptions. It's designed to help developers and researchers organize, search, and recommend repositories more effectively.

📌 Features
Fine-tuned on the zamal/github-meta-data dataset

Uses Hugging Face's Trainer API for training and evaluation

Implements LoRA via PEFT for efficient parameter tuning

Integrated with Weights & Biases for experiment tracking

Pushes trained model to Hugging Face Hub

Provides a simple tag generation pipeline using transformers.pipeline

🧠 Model Architecture
Base Model: T5-small

PEFT Strategy: LoRA with r=16, alpha=16, dropout 0.5

Task Type: Sequence-to-sequence (text2text-generation)

📦 Installation
bash
git clone https://github.com/ArijitMishra/github_tag_generator_t5_locally_finetuned.git
cd github_tag_generator_t5_locally_finetuned
pip install -r requirements.txt
Make sure to set your Hugging Face token in a .env file:

Code
HF_TOKEN=your_huggingface_token
🏋️‍♂️ Training
python
trainer.train()
Training arguments include:

100 epochs

Batch size: 8

Learning rate: 1e-4

Evaluation every 50 steps

Model checkpointing and Hub push enabled

🔍 Tag Generation
After training, use the pipeline to generate tags:

python
from transformers import pipeline

tag_generator = pipeline("text2text-generation", model="./t5_tag_generator", tokenizer="./t5_tag_generator")

def generate_tags(text):
    output = tag_generator(text, num_beams=5, early_stopping=True)
    decoded = output[0]["generated_text"]
    return clean_and_deduplicate_tags(decoded)
Example:

python
generate_tags("Best libraries for accessing NLP datasets and evaluation tools in Python.")
# Output: nlp, datasets, evaluation, python, huggingface
📊 Dataset
Source: zamal/github-meta-data

Format: JSON with input (repo description) and target (tags)

🧪 Evaluation
Validation split: 10%

Metrics tracked via Weights & Biases

Model saved and pushed to Hugging Face Hub: ArijitMishra/t5_model_finetuned_github_tag_generator_from_local

📁 Output Directory
Trained model and tokenizer are saved to:

Code
./t5_tag_generator
🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.