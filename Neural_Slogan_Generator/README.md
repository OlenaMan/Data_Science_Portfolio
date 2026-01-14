## Slogan Classifier and Generator (LSTM)

### Overview

This project demonstrates an end-to-end deep learning workflow for building two NLP models:

1) A **slogan generator** trained with an **LSTM** to generate industry-conditioned slogans by predicting text one word at a time.  
2) A **slogan classifier** trained with an **LSTM** to predict a company’s **industry** from a given slogan.

The notebook covers dataset loading, text preprocessing, sequence modelling, model training, and evaluation, with emphasis on how model design choices affect performance and generalisation.

### Business Context

Slogans are short, high-impact marketing phrases that communicate brand identity and positioning. Automating slogan generation can support creative ideation at scale, while classifying slogans by industry can help with brand analysis, market intelligence, and content moderation.

This project explores how far sequence models can go with limited labelled text data across many categories, and highlights common challenges such as **data imbalance** and **overfitting** in multi-class NLP classification.

### What I Did

- Loaded and inspected the slogan dataset (`slogan-valid.csv`) including column structure and missing values

- Extracted relevant features (`industry`, `output`) and removed missing entries

- Preprocessed slogans using spaCy:
  - lowercasing
  - punctuation removal
  - token-based reconstruction

- Created a **generator training text** by prefixing each slogan with its industry (industry conditioning)

- Built a vocabulary using Keras `Tokenizer` and converted text into integer sequences

- Prepared training sequences for the generator using progressively longer n-grams and padded them to a fixed length

- Built and trained an **LSTM generator** (Embedding → LSTM → LSTM → Dense softmax)

- Implemented a `generate_slogan()` function that predicts one word at a time from a seed industry prompt

- Prepared classifier training data using full padded slogan sequences (not n-grams)

- Addressed stratified split constraints by removing industries with only one example

- Built and trained an **LSTM classifier** (Embedding → LSTM → LSTM → Dense softmax)

- Evaluated classifier performance and identified overfitting using train vs test accuracy

- Implemented a `classify_slogan()` function to predict an industry from an input slogan

- Combined both models in a simple pipeline:
  - generate slogan → classify generated slogan → compare intended vs predicted industry

### Key Skills Demonstrated

- Natural language preprocessing (spaCy)

- Sequence modelling with LSTMs (TensorFlow / Keras)

- Tokenisation and padding for NLP

- Multi-class classification (softmax)

- Model evaluation and error analysis

- Overfitting detection and interpretation of generalisation gaps

- Handling class imbalance and stratified splitting constraints

- Python (pandas, numpy, scikit-learn, TensorFlow)

### Dataset

- Source file: `slogan-valid.csv`

- Key columns used:
  - `industry` (label for classification)
  - `output` (slogan text)

- Task types:
  - **Text generation** (next-word prediction using industry-conditioned input)
  - **Multi-class classification** (predict industry from slogan)

- Challenge:
  - Large number of unique industries (142)
  - Some industries appear only once, requiring filtering before stratified splitting

### Models Used

#### Slogan Generator (LSTM)

- Goal: generate slogan text conditioned on an industry seed prompt

- Training approach:
  - Prefix industry to slogan text
  - Create progressively longer sequences (n-gram style)
  - Predict next word using softmax over the vocabulary

- Architecture:
  - Embedding layer (100 dims)
  - LSTM (150 units, return sequences)
  - LSTM (100 units)
  - Dense softmax output over vocabulary

#### Slogan Classifier (LSTM)

- Goal: predict industry from full processed slogan text

- Training approach:
  - Tokenise and pad full slogans (not progressive sequences)
  - One-hot encode industry labels

- Architecture:
  - Embedding layer (100 dims)
  - LSTM (150 units, return sequences)
  - LSTM (100 units)
  - Dense softmax output over industries

### Results (High Level)

- The generator learns plausible word-to-word sequencing and can produce fluent text-like outputs, but industry conditioning is imperfect and can drift off-topic after the seed prompt.

- The classifier shows extreme train/test mismatch:
  - Very high training accuracy (~99%) but low test accuracy (~20%)
  - This indicates strong **overfitting** and weak generalisation across unseen slogans.

- When combining the models, generated slogans may be classified into a different industry than the seed prompt if the generated content contains stronger cues for another category.

- Overall, the project highlights:
  - The difficulty of multi-class classification with many labels and limited samples per class
  - The tendency of LSTMs to memorise training data without stronger regularisation or more data
  - The practical challenges of controlling generated text with lightweight conditioning

- (Training curves, evaluation outputs, and example generations are included in the notebook.)











