# Random Sentence Generator

A Python script that generates random sentences based on a given corpus using n-gram models. The script supports different n-gram sizes and formats the generated sentences by ensuring proper punctuation and spacing.

## Features

- Generates random sentences using 1-gram to n-gram models.
- 

## Usage

To run the script, use the following command:

python3 ngrams.py <n> <m> <file1> <file2> ...


**Parameters**
<n>: The n-gram size (e.g., 1 for unigrams, 2 for bigrams, etc.).
<m>: The number of sentences to generate.
<file1> <file2> ...: The text files containing the corpus to be used for generating sentences.

Example
To generate 5 sentences using 2-grams from corpus1.txt and corpus2.txt, run:

python script.py 2 5 corpus1.txt corpus2.txt

## How It Works
**Text Normalization:** The script reads and normalizes the text by converting it to lowercase and removing new lines.

**Tokenization:** The text is tokenized into words and punctuation marks, excluding quotation marks and parentheses.

**N-Gram Creation:** The script creates n-grams from the tokenized text.

**Frequency Calculation:** The frequency of each n-gram is calculated.

**Sentence Generation:** Random sentences are generated based on the n-grams and their frequencies.

## Example Output
Here's a sample output for a 3-gram model with 3 generated sentences:

1. But i was seated on the march
2. I had brought together in strict character however admirably satirical that after all
9. But this is the ocean has been ruined through lack of intelligence









