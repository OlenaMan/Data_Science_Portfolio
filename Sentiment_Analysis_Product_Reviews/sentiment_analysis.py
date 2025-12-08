"""
Sentiment analysis on Amazon product reviews using spaCy + spaCyTextBlob.

This script:
- Loads the Datafiniti Amazon reviews CSV safely.
- Cleans and preprocesses the text.
- Applies sentiment analysis (polarity via TextBlob through spaCy).
- Prints basic evaluation info and example outputs.

Defensive programming:
- Explicit file existence checks.
- Clear error messages for missing / malformed data.
"""

from pathlib import Path
from typing import Dict, Any

import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# -------------------------------------------------------------------
# Safe dataset loading
# -------------------------------------------------------------------


def load_dataset(csv_path: str) -> pd.DataFrame:
    """
    Load the dataset with defensive checks.

    - Verifies that the file exists.
    - Attempts to read the CSV with pandas.
    - Ensures that the 'reviews.text' column is present.

    Raises:
        FileNotFoundError: if the CSV is not found.
        ValueError: if the CSV cannot be read or lacks required columns.
    """
    path = Path(csv_path)

    # Check if file exists before attempting to read
    if not path.is_file():
        raise FileNotFoundError(
            f"Dataset not found at: {csv_path}. "
            f"Ensure the CSV file is in the same folder as this script."
        )

    try:
        # low_memory=False avoids dtype guessing issues on large CSVs
        df = pd.read_csv(path, low_memory=False)
    except Exception as exc:
        raise ValueError(f"Unable to read CSV file: {exc}") from exc

    # Defensive check: required column must exist
    if "reviews.text" not in df.columns:
        raise ValueError(
            "Expected column 'reviews.text' was not found in the dataset. "
            "Check that you are using the correct Datafiniti CSV."
        )

    return df


# -------------------------------------------------------------------
# Text preprocessing
# -------------------------------------------------------------------

def preprocess_text(nlp: spacy.Language, text: Any) -> str:
    """
    Clean and preprocess a single review using spaCy.

    Steps:
    - Ensure the input is a string.
    - Convert to lowercase.
    - Strip leading/trailing whitespace.
    - Use spaCy to tokenize.
    - Remove stop words.
    - Keep only alphabetic tokens (filter out numbers, punctuation, etc.).

    Returns:
        A cleaned string suitable for sentiment analysis.
    """
    if not isinstance(text, str):
        # If the value is not a string, return an empty string
        return ""

    # Basic string-level cleaning
    clean = text.lower().strip()

    # Use spaCy for tokenization and linguistic attributes
    doc = nlp(clean)

    # Keep non-stopword alphabetic tokens
    filtered_tokens = [
        token.text
        for token in doc
        if not token.is_stop and token.is_alpha
    ]

    return " ".join(filtered_tokens)


# -------------------------------------------------------------------
# Sentiment analysis function
# -------------------------------------------------------------------

def analyze_sentiment(nlp: spacy.Language, text: str) -> Dict[str, Any]:
    """
    Analyse sentiment of a single review using spaCyTextBlob.

    Uses:
        doc._.blob.polarity  -> float in [-1.0, 1.0]

    Interpretation:
        polarity > 0  -> positive
        polarity < 0  -> negative
        polarity == 0 -> neutral

    Returns:
        dict with keys:
            - 'sentiment' (str: 'positive', 'negative', or 'neutral')
            - 'polarity' (float)
    """
    if not text or not isinstance(text, str):
        # Neutral default for empty or non-string text
        return {"sentiment": "neutral", "polarity": 0.0}

    doc = nlp(text)

    # spaCyTextBlob adds the ._.blob extension to the Doc
    polarity = doc._.blob.polarity

    if polarity > 0:
        label = "positive"
    elif polarity < 0:
        label = "negative"
    else:
        label = "neutral"

    return {"sentiment": label, "polarity": polarity}


# -------------------------------------------------------------------
# Basic evaluation / inspection helpers
# -------------------------------------------------------------------

def print_basic_evaluation(df: pd.DataFrame) -> None:
    """
    Print some simple evaluation information to the console.

    Shows:
    - Sentiment distribution (counts and proportions).
    - A few example reviews with their predicted sentiment and polarity.
    """
    print("\n=== Sentiment distribution (counts) ===")
    print(df["sentiment"].value_counts())

    print("\n=== Sentiment distribution (proportions) ===")
    print(df["sentiment"].value_counts(normalize=True))

    # Show a small sample of each sentiment for manual inspection
    for label in ["positive", "negative", "neutral"]:
        print(f"\n=== Example {label} reviews ===")
        subset = df[df["sentiment"] == label].head(3)

        # Defensive: handle case where there are fewer than 3 reviews
        # of a class
        if subset.empty:
            print(f"No {label} reviews found.")
            continue

        for _, row in subset.iterrows():
            original = row.get("reviews.text", "")
            polarity = row.get("polarity", 0.0)
            print(f"- Review: {original[:200]!r}...")
            print(f"  Polarity: {polarity:.3f}")


def print_similarity_example(nlp: spacy.Language, df: pd.DataFrame) -> None:
    """
    Compare similarity between two cleaned reviews using spaCy's .similarity().

    Notes:
    - Uses the first two rows in the cleaned text as an example.
    - Includes defensive checks for dataset size.
    """
    if len(df) < 2:
        print("\nNot enough reviews to compute similarity (need at least 2).")
        return

    review_a = df["clean_text"].iloc[0]
    review_b = df["clean_text"].iloc[1]

    doc_a = nlp(review_a)
    doc_b = nlp(review_b)

    similarity_score = doc_a.similarity(doc_b)

    print("\n=== Similarity example ===")
    print(f"Clean review 0: {review_a[:200]!r}...")
    print(f"Clean review 1: {review_b[:200]!r}...")
    print(f"Similarity score (0–1): {similarity_score:.3f}")


# -------------------------------------------------------------------
# Main script logic
# -------------------------------------------------------------------

def main() -> None:
    """
    Main entry point for the script:
    - Loads the dataset.
    - Drops missing review texts.
    - Loads spaCy model and adds spaCyTextBlob.
    - Preprocesses text.
    - Runs sentiment analysis.
    - Prints some basic evaluation and similarity example.
    """
    # Path to the CSV file
    csv_path = "Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv"

    # Load dataset
    df = load_dataset(csv_path)

    # Drop rows where 'reviews.text' is missing
    df = df.dropna(subset=["reviews.text"]).copy()

    # Defensive check: avoid running on an empty DataFrame
    if df.empty:
        raise ValueError("Missing 'reviews.text', no data remains.")

    # Load spaCy model and attach spaCyTextBlob
    try:
        nlp = spacy.load("en_core_web_md")
    except OSError as exc:
        raise OSError(
            "spaCy model 'en_core_web_md' is not installed. "
            "Run: python -m spacy download en_core_web_md"
        ) from exc

    # Add spaCyTextBlob pipeline component for sentiment (polarity) scores
    if "spacytextblob" not in nlp.pipe_names:
        nlp.add_pipe("spacytextblob")

    # Preprocess reviews (clean text column)
    df["clean_text"] = df["reviews.text"].apply(lambda x: preprocess_text(nlp, x))

    # Run sentiment analysis on cleaned text
    df["sentiment_result"] = df["clean_text"].apply(
        lambda x: analyze_sentiment(nlp, x)
    )
    df["sentiment"] = df["sentiment_result"].apply(lambda x: x["sentiment"])
    df["polarity"] = df["sentiment_result"].apply(lambda x: x["polarity"])

    # Test model on a few manual sample reviews
    print("\n=== Manual test examples ===")
    sample_reviews = [
        "This product is amazing, exceeded my expectations!",
        "Terrible quality. It broke after one use and I want a refund.",
        "It works fine, nothing special but does the job."
    ]

    for text in sample_reviews:
        clean = preprocess_text(nlp, text)
        result = analyze_sentiment(nlp, clean)
        print(f"\nOriginal: {text!r}")
        print(f"Cleaned : {clean!r}")
        print(f"Result  : {result}")

    # Basic evaluation: distribution and example reviews
    print_basic_evaluation(df)

    # Example of similarity between two reviews
    print_similarity_example(nlp, df)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        # Top-level catch to avoid hard crashes and provide clear messaging
        print(f"\nError while running sentiment analysis: {error}")
