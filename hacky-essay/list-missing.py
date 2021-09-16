#!/usr/bin/env python3
import os
from collections import Counter

top_entries = set()
global_enable_top_entries = False

def load_essay(tsv_path):
    words = set()
    with open(tsv_path) as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split("\t")
            word = parts[0]
            words.add(word)
    return words

def dump_missing_words(csv_path, words):
    output_path = csv_path.replace('.csv', '-missing.csv')
    with open(csv_path) as csv:
        lines = csv.readlines()
    with open(output_path, 'w') as output:
        for line in lines:
            word = line.split(',')[0]
            word = word.replace('\n', '')
            if word.startswith('#') or any(c.isascii() or c == '，' for c in word): continue
            if word not in words:
                output.write(line)

words = load_essay('hacky-essay.txt')
dump_missing_words('lihkg_ngram_1_16_lite.csv', words)
# dump_missing_words('lihkg_ngram_1_16.csv', 1, words)
dump_missing_words('apple_ngram_1_16.csv', words)
dump_missing_words('wiki_ngram_1_16.csv', words)
dump_missing_words('existingwordcount.csv', words)
dump_missing_words('wordslist.csv', words)
