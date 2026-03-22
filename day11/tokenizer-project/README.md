"""
# Tokenizer Project

## Description
This project implements a simple tokenizer that:
- Splits text into words (tokens)
- Assigns a unique ID to each word
- Maintains a dynamic vocabulary

## Features
- Lowercase normalization
- Punctuation removal
- Dynamic vocabulary creation
- Vocabulary persistence (saved to file)
- Unit testing included

## Example
Input:
This is a test. This test is simple.

Output:
Tokens:
["this", "is", "a", "test", "this", "test", "is", "simple"]

Vocabulary:
{"this": 1, "is": 2, "a": 3, "test": 4, "simple": 5}

## Run
python main.py

## Run Tests
pytest
"""