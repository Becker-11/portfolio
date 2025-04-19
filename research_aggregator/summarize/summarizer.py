# summarize/summarizer.py
import warnings
from transformers import logging as hf_logging

# 1) Only show errors from the transformers library
hf_logging.set_verbosity_error()

# 2) Ignore the torch.tensor copy‑construct UserWarning spam
warnings.filterwarnings(
    "ignore",
    message=".*torch.tensor.*",
    category=UserWarning
)


import yaml
from pathlib import Path
from typing import List, Dict

from transformers import pipeline
from keybert import KeyBERT

# Determine project root and config path
ROOT = Path(__file__).resolve().parents[1]  # points to portfolio/research_aggregator
CONFIG_PATH = ROOT / "config" / "sources.yaml"

# Load any summarization settings if needed

def load_config() -> Dict:
    with CONFIG_PATH.open() as f:
        return yaml.safe_load(f)
import warnings
from transformers import logging as hf_logging

# 1) Only show errors from the transformers library
hf_logging.set_verbosity_error()

# 2) Ignore the torch.tensor copy‑construct UserWarning spam
warnings.filterwarnings(
    "ignore",
    message=".*torch.tensor.*",
    category=UserWarning
)
# Initialize summarization pipeline and KeyBERT model
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    tokenizer="facebook/bart-large-cnn",
)
kw_model = KeyBERT()


def summarize_text(text: str, max_length: int = 60, min_length: int = 30) -> str:
    """Generate a concise summary of the given text."""
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']


def extract_keywords(text: str, top_n: int = 5) -> List[str]:
    """Extract top keywords from the given text."""
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=top_n)
    # keywords is List[(phrase, score)], return just phrases
    return [phrase for phrase, score in keywords]


def enrich_paper(paper: Dict) -> Dict:
    """Add summary and keywords to a paper dict."""
    abstract = paper.get("abstract", "")
    paper["summary"] = summarize_text(abstract)
    paper["keywords"] = extract_keywords(abstract)
    return paper


if __name__ == "__main__":
    # Example usage:
    example = """
    Deep learning models have achieved state-of-the-art performance on a variety of tasks,
    but ensuring their alignment with human safety values remains a challenge...
    """
    print("Summary:", summarize_text(example))
    print("Keywords:", extract_keywords(example))
