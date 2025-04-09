# Random Sentence Generator

A Python script that generates random sentences based on a corpus using n-gram models.


## Setup

To run the script, use the following command:

python3 ngrams.py [n] [m] [file1] [file2] ...

**Parameters:**

- **[n]**: The n-gram size.

- **[m]**: The number of sentences to generate.

- **[file1] [file2] ...** : The text files containing the corpus to be used for generating sentences. (Example files found in 'example-corupuses').

**Example**

To generate 5 sentences using 2-grams from corpus1.txt and corpus2.txt, run:

python ngram.py 3 3 corpus1.txt corpus2.txt

**Output**

1. But i was seated on the march
2. I had brought together in strict character however admirably satirical that after all
3. But this is the ocean has been ruined through lack of intelligence

## How It Works
**Text Normalization:** The script reads and normalizes the corpus.

**Tokenization:** The corpus is tokenized into words and punctuation marks.

**N-Gram Creation:** The script creates n-grams from the tokenized text and calculates frequencies.

**Sentence Generation:** Random sentences are generated based on the n-grams and their frequencies.









