# 🚀 GitHub Tag Generator with T5 + PEFT (LoRA)

This project fine-tunes a [T5-small](https://huggingface.co/t5-small) model using [PEFT](https://github.com/huggingface/peft) with LoRA (Low-Rank Adaptation) to automatically generate relevant tags for GitHub repository descriptions. It's designed to help developers and researchers organize, search, and recommend repositories more effectively.

---

## 📌 Features

- Fine-tuned on the [zamal/github-meta-data](https://huggingface.co/datasets/zamal/github-meta-data) dataset  
- Uses Hugging Face's `Trainer` API for training and evaluation  
- Implements LoRA via PEFT for efficient parameter tuning  
- Integrated with [Weights & Biases](https://wandb.ai/) for experiment tracking  
- Pushes trained model to Hugging Face Hub  
- Provides a simple tag generation pipeline using `transformers.pipeline`

---

## 🧠 Model Architecture

- **Base Model**: T5-small  
- **PEFT Strategy**: LoRA with `r=16`, `alpha=16`, dropout `0.5`  
- **Task Type**: Sequence-to-sequence (text2text-generation)

---

## 📦 Installation

```bash
git clone https://github.com/ArijitMishra/github_tag_generator_t5_locally_finetuned.git
cd github_tag_generator_t5_locally_finetuned
pip install -r requirements.txt

Make sure to set your Hugging Face token in a .env file:
HF_TOKEN=your_huggingface_token
```


## 🏋️‍♂️ Training

The model is fine-tuned using Hugging Face's `Trainer` API with PEFT (LoRA) for efficient adaptation. Below is a summary of the training setup:

### 🔧 Training Arguments

- **Epochs**: 100  
- **Batch Size**: 8 (for both training and evaluation)  
- **Learning Rate**: 1e-4  
- **Evaluation Strategy**: Every 50 steps  
- **Logging Steps**: Every 10 steps  
- **Save Strategy**: Every 50 steps, keeping the 2 most recent checkpoints  
- **Mixed Precision**: Enabled (`fp16=True`)  
- **Push to Hub**: Enabled  
- **Hub Model ID**: `ArijitMishra/t5_model_finetuned_github_tag_generator_from_local`  
- **W&B Integration**: Enabled (`report_to="wandb"`)

### 🧪 Evaluation

- Validation split: 10%  
- Metrics and logs tracked via [Weights & Biases](https://wandb.ai/)  
- Best model saved and optionally pushed to Hugging Face Hub

### 🧬 LoRA Configuration

- **Rank (r)**: 16  
- **Alpha**: 16  
- **Dropout**: 0.5  
- **Target Modules**: `["q", "v"]`  
- **Bias**: `"none"`  
- **Task Type**: `SEQ_2_SEQ_LM`

### 🧰 Data Collation

```python
data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)
```