# Cameron Clyde
#
# CMSC 416
# 2/5/2024
#
# Programming Assignment 1
#
# This program uses n-gram modeling to generate a given number of sentences.
#   This is done by taking a pattern of 'n-1' consecutive words in a sentence and counting the number of
#   occurrences of each unique word following the pattern. Once we get the frequencies of the following words we can
#   generate a sentence by starting with a single word and picking the next word based on the probability.
#
#
# Use instructions:
#   Run program by typing 'ngram.py n m input-file(s)' into terminal
#   n: dimension of ngram
#   m: number of sentences to be generated
#   input-file(s): one or more .txt filepaths to be used as corpus, separated by a space
#
#
#
#
# Example:
#   python3 ngram.py 3 10 pg84.txt
#   This program generates random sentences based on a Ngram model.
#
#   0. i was not the time that the reverse of this agreement by keeping this work or any part of the preceding night ,
#   for i longed to obtain food and clothes which i was unable to injure anything human , sorrows .

#   1. he was a shattered wreck — the sounding cataract haunted him like a dream , and i may die .
#
#   2. i had formerly occupied a part of the murderer .
#
#   3. i thought of the rhine in a state of mind i wrote , and i should have been the meed of his child so completely
#   as i was or what i so much dreaded to behold , on these subjects .
#
#   4. the spirits of the glaciers and hide himself from pursuit among the trees .
#
#   5. i had selected his features as beautiful as her promised gift , i should have been my constant friend and
#   companion .
#
#   6. i had created .
#
#   7. i have been massacred before his eyes , and in a few hours before ; they appeared to me , and the thunder of its
#   unspeakable torments , dared to fancy amiable and benevolent mind .
#
#   8. “ i know not ; call on the point of repeating his blow , when i was not so miserable as i shall be with you ,
#   my creator , make me happy ; and when i awoke , and i believed myself destined for some time , i felt
#
#   9. but it is true , but i was , i was overcome by these means was enabled , with a repulsive physiognomy and
#   manners , so the foundation ’ s house .
#
#   Algorithm:
#
#       Normalize the text data:
#           1. Input files are opened and stored in series in a string.
#           2. This string is split into sentences with [.?!] as boundaries.
#           3. Each sentence is split into individual words/punctuation and pad the start with n-1
#           '<start>' tags and a single '<end>' tag
#
#       Create ngrams:
#           1. Take in list of tokenized sentences and for each sentence:
#               - Look at n words in a sentence. Create a two index tuple with the first index being a tuple of the
#                 first n-1 words and the second index the nth word. this tuple to a list
#               - Increment index and slide our n words by one index.
#               - If the nth token is the '<end>' tag, go to next sentence
#               - Go back to first step in for loop
#
#       Create ngram table and frequency table:
#           ngram-table:
#               1. create a new dictionary
#               2. for each ngram in our list of ngrams:
#                   - if the n-1 tuple is a key in the dict
#                       - Append value to list of values
#                   - else
#                       - add key and value to list
#
#           frequency table:
#               1. create a new dictionary
#               2. for each ngram in our list of ngrams:
#                   - if the n-1 tuple is a key in the dict
#                       - increment value by 1
#                   - else
#                       - add key to list and set its value to 1
#
#       Generate m number of sentences:
#           1. Begin with n-1 '<start>' tags
#           2. Choose a random next word
#               - Compare n-1 tuple to the ngram table
#               - Grab the list of values as possible next words
#               - for each n-1 tuple and possible next word
#                   * create a list of weighted probabilities based on the frequencies of the next possible word
#               - randomly pick a new word from the weighted probabilities
#           3. Check if next word is '<end>' tag
#               - If yes, break
#               - If not, add new word to sentence
#           4. Repeat at step 2 with the new n-1 tuple
#
# Sources:
#   - ngram_python_guide1.pdf (from assignment)
#   -
#
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
