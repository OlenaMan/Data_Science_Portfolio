## Sentiment Analysis on Amazon Product Reviews 
(spaCy + spaCyTextBlob)

### Overview

This project demonstrates a practical natural language processing workflow for analysing sentiment in Amazon product reviews.
It focuses on safe data loading, text preprocessing, sentiment scoring, and basic qualitative evaluation, with an emphasis on clarity,
defensive programming, and interpretability rather than model optimisation.

The script applies rule-based sentiment analysis using TextBlob polarity scores integrated into spaCy, and includes simple inspection
outputs to support manual validation of results.

### Business Context

Customer reviews contain valuable signals about product quality, customer satisfaction, and recurring issues.
Understanding sentiment at scale helps businesses monitor brand perception, identify common pain points, and prioritise product or service improvements.

This project explores how raw review text can be cleaned and analysed to extract sentiment signals in a transparent and reproducible way,
suitable for early-stage analysis or baseline benchmarking.

### What I Did

- Loaded the Datafiniti Amazon product reviews dataset with explicit file and schema checks

- Validated required columns and handled missing or malformed data defensively

- Cleaned and preprocessed review text using spaCy tokenisation and linguistic features

- Removed stop words and non-alphabetic tokens to standardise input text

- Applied sentiment analysis using spaCyTextBlob polarity scores

- Classified reviews as positive, negative, or neutral based on polarity

- Tested the pipeline on manual sample reviews for sanity checking

- Printed sentiment distributions and example reviews for qualitative evaluation

- Demonstrated semantic similarity between reviews using spaCy vector embeddings

### Key Skills Demonstrated

- Text preprocessing with spaCy

- Rule-based sentiment analysis

- Defensive programming and error handling

- Data validation and cleaning

- Basic NLP evaluation and inspection techniques

- Python scripting and modular function design

- pandas for data manipulation

### Dataset

- Based on the Datafiniti Amazon Consumer Reviews dataset

- Primary text field: `reviews.text`

- Data type: unstructured text

- Task type: sentiment analysis (polarity-based classification)

- Reviews with missing text are excluded to ensure data integrity

### Techniques Used

#### Text Preprocessing (spaCy)

- Lowercasing and whitespace normalisation

- Tokenisation using spaCy’s language model

- Stop word removal

- Filtering to alphabetic tokens only

#### Sentiment Analysis (spaCyTextBlob)

- Polarity score in the range `[-1.0, 1.0]`

- Rule-based interpretation:
  - polarity > 0 → positive
  - polarity < 0 → negative
  - polarity = 0 → neutral

#### Similarity Analysis

- Uses `Doc.similarity()` from spaCy

- Demonstrates semantic similarity between two cleaned reviews

- Intended for illustration, not quantitative evaluation

### Results (High Level)

- The pipeline successfully separates reviews into positive, negative, and neutral sentiment categories

- Polarity scores align well with intuitive sentiment in manual test cases

- Sentiment distributions provide a quick overview of customer opinion trends

- Similarity scores illustrate how semantic relationships between reviews can be explored

- The project highlights the strengths and limitations of polarity-based sentiment methods, particularly their simplicity and transparency

- (Detailed outputs and examples are printed directly to the console when the script is run.)
