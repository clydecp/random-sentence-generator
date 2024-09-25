import random
import re
from collections import defaultdict, Counter
from sys import argv


# Formats text to be used for n-gram processing
def format_text(string, n):
    # Normalize text by removing new lines and setting to lowercase
    string = string.lower().replace("\n", " ")

    # Split sentences with delimiters ['.', '?', '!']
    sentences = re.split(r'(?<=[.!?])\s+', string)
    # Split sentences into individual words and punctuation, excluding quotes and parentheses
    tokenized_sentences = [re.findall(r"\b\w+(?:'\w+)?\b|[^\w\s,.!?]", sentence) for sentence in sentences]
    new_tokenized_sentences = []
    # Pad each sentence with n-1 '<start>' tags and a single '<end>' tag
    for sentence in tokenized_sentences:
        if len(sentence) >= n:
            sentence = (n - 1) * ['<start>'] + sentence + ['<end>']
            new_tokenized_sentences.append(sentence)
    return new_tokenized_sentences


# Create list of n-grams for each sentence
def create_ngrams(n, tokens):
    ngrams = []
    if n == 1:
        # For 1-grams, just collect words
        for sentence in tokens:
            ngrams.extend(sentence)
    else:
        for sentence in tokens:
            ngrams.extend([(tuple(sentence[i - n + 1:i]), sentence[i]) for i in range(n - 1, len(sentence))])
    return ngrams


# Count frequency of each word given the previous n-1 words
def frequencies(ngrams):
    if isinstance(ngrams[0], tuple):
        return dict(Counter(ngrams))
    else:
        return dict(Counter((word,) for word in ngrams))


# Dictionary containing keys of (n-1) words and each possible next word
def create_ngram_table(ngrams):
    table = defaultdict(list)
    for ngram in ngrams:
        if isinstance(ngram[0], tuple):
            current_words, next_word = ngram
            table[current_words].append(next_word)
        else:
            table[()].append(ngram)
    return dict(table)


# Determine the probability of seeing a word, given the previous (n-1) words
def probability(frequency, ngram_table, current_words, possible_word):
    ab = frequency.get((current_words, possible_word), 0)
    a = float(len(ngram_table.get(current_words, [])))
    if a == 0:
        return 0
    return ab / a


# Chooses a random word based on the given n-1 gram
def random_word(frequency, ngram_table, current_words):
    if len(current_words) == 1 and current_words[0] == '<start>':
        # For unigrams, current_words is irrelevant
        words, probs = zip(*frequency.items())
        return random.choices(words, probs)[0]
    else:
        current_words = tuple(current_words)
        list_of_next_words = ngram_table.get(current_words, [])
        if not list_of_next_words:
            return '<end>'
        word_probabilities = [probability(frequency, ngram_table, current_words, word) for word in list_of_next_words]
        return random.choices(list_of_next_words, word_probabilities)[0]


# Generate a random sentence from n-grams
def generate_sentence(ngram_table, frequency, n):
    current_words = (n - 1) * ['<start>']
    sentence = []
    max_sentence_size = 50

    while len(sentence) < max_sentence_size:
        next_word = random_word(frequency, ngram_table, current_words)
        if next_word == '<end>':
            break
        current_words = current_words[1:] + [next_word]
        sentence.append(next_word)

    # Ensure proper spacing around punctuation
    sentence = ' '.join(sentence)
    # Remove space before commas and periods
    sentence = re.sub(r'\s+([,.])', r'\1', sentence)
    # Remove space around quotes and parentheses
    sentence = re.sub(r'\s+(["()])\s+', r'\1', sentence)
    sentence = sentence.strip()

    # Capitalize the first letter of the sentence
    sentence = sentence.capitalize()

    return sentence


def main():
    if len(argv) < 4:
        print("Usage: python script.py <n> <m> <file1> <file2> ...")
        exit()

    # Data from command line
    n = int(argv[1])
    m = int(argv[2])
    corpus_files = argv[3:]

    data = ""

    # Put all corpus text into data in series
    for file in corpus_files:
        with open(file, 'r') as file_data:
            data += file_data.read() + " "

    # Tokenize each sentence in data
    tokens = format_text(data, n)
    # Create a list of n-grams
    ngrams = create_ngrams(n, tokens)

    # Handle unigrams differently
    if n == 1:
        frequency = frequencies(ngrams)
        ngram_table = {(): list(frequency.keys())}
    else:
        frequency = frequencies(ngrams)
        ngram_table = create_ngram_table(ngrams)

    # Generate m number of sentences
    for i in range(m):
        print(f"{i + 1}. {generate_sentence(ngram_table, frequency, n)}\n")


if __name__ == "__main__":
    main()
