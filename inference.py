from transformers import pipeline

tag_generator = pipeline(
    "text2text-generation", model="./t5_tag_generator", tokenizer="./t5_tag_generator"
)

def clean_and_deduplicate_tags(decoded):
    tags = [tag.strip().lower() for tag in decoded.split(",")]

    ignore_list = {"a", "an", "the", "and", "or", "of", "to", "on", "in", "for", "with", "etc", "from"}
    filtered = [tag for tag in tags if tag not in ignore_list and len(tag) > 1]
    return ", ".join(dict.fromkeys(filtered))

def generate_tags(text):
    output = tag_generator(text, num_beams=5, early_stopping=True)
    decoded = output[0]["generated_text"]
    return clean_and_deduplicate_tags(decoded)

hf_repos = [
    "Best GitHub repositories with practical notebooks demonstrating real-world AI applications from Hugging Face.",
    "Best libraries for accessing NLP datasets and evaluation tools in Python.",
    "Searching for Hugging Face Diffusers repositories for generating images, audio, and other media with pre-trained diffusion models.",
]

for text in hf_repos:
    tags = generate_tags(text)
    print(f"The value for {text} is: ")
    print(tags)