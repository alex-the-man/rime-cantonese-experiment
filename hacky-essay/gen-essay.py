#!/usr/bin/env python3
import os
from collections import Counter

top_entries = set()
global_enable_top_entries = False

def load_ngram_csv(csv_path, weight, words, enable_top_entries=True):
    with open(csv_path) as f:
        lines = f.readlines()
        i = 0
        skipped_header = False
        for line in lines:
            if not skipped_header:
                skipped_header = True
                continue
            parts = line.split(",")
            word = parts[0]
            if any(c.isascii() or c == '，' for c in word): continue
            count = int(parts[1])
            words[word] = weight * count + words.get(word, 0)
            if global_enable_top_entries and enable_top_entries and i < 50000:
                top_entries.add(word)
            i += 1

words = dict()
# load_ngram_csv('lihkg_ngram_1_16_lite.csv', 1, words)
load_ngram_csv('lihkg_ngram_1_16.csv', 1, words)
load_ngram_csv('apple_ngram_1_16.csv', 1, words)
load_ngram_csv('wiki_ngram_1_16.csv', 1, words, enable_top_entries=False)
load_ngram_csv('existingwordcount.csv', 1, words, enable_top_entries=True)

files = [
    'rime-cantonese/jyut6ping3.dict.yaml',
    'rime-cantonese/jyut6ping3.maps.dict.yaml',
    'rime-cantonese/jyut6ping3.phrase.dict.yaml',
    'org-essay.txt',
    'existingwordcount.csv',
    'wordslist.csv',
]

# Keep all entries from this file, even if the word doesn't exist in the corpus.
keep_everything_set = set([
    'rime-cantonese/jyut6ping3.dict.yaml', # Gotta keep all entries from the dict to avoid Rime suggesting 罕音詞組
    # 'rime-cantonese/jyut6ping3.phrase.dict.yaml',
])

combined = Counter()

for file in files:
    output_path = file.replace('.txt', '.log')
    output_path = output_path.replace('.csv', '.log')
    output_path = output_path.replace('.yaml', '.log')
    output_path = os.path.basename(output_path)

    processed_words = set()
    with open(file) as input:
        lines = input.readlines()

    with open(output_path, 'w') as output:
        keep_everything = file in keep_everything_set

        for top_entry in top_entries:
            combined[top_entry] = words[top_entry]

        for line in lines:
            if file.endswith('csv'):
                word = line.split(',')[0]
            else:
                word = line.split('\t')[0]
            word = word.replace('\n', '')
            if len(word) == 0 or '，' in word: continue
            if word.startswith('#') or any(c.isascii() or c == '，' for c in word): continue
            if word in words:
                if word in processed_words: continue
                combined[word] = words[word]
                processed_words.add(word)
                output.write(word + '\t' + str(words[word]) + '\n')
            else:
                if keep_everything:
                    combined[word] = 0
                    output.write(word + '\t' + str(0) + '\n')
                else:
                    output.write('# dropped ' + word + '\n')

with open('hacky-essay.txt', 'w') as output:
    for (k, v) in combined.most_common():
        if v == 0 and len(k) == 1: continue
        output.write(k + "\t" + str(v) + "\n")
