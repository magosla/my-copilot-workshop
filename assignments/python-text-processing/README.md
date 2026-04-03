# 📘 Assignment: Python Text Processing

## 🎯 Objective

Build practical Python skills for working with text data by reading files, cleaning and transforming strings, and producing simple text analysis results. You will create a command-line program that processes a text file and generates useful summaries.

## 📝 Tasks

### 🛠️ Read and Clean Text Data

#### Description
Create a Python program that loads text from a file and normalizes it so later analysis is consistent. Your program should handle letter case and punctuation in a predictable way.

#### Requirements
Completed program should:

- Read text content from a file named `sample-text.txt`
- Convert all text to lowercase
- Remove punctuation characters like `. , ! ? ; :` using string methods or loops
- Split the cleaned text into individual words
- Print the total number of words found

```text
Example Input (file):
Hello, students! Python is fun. Python is powerful.

Example Output:
Total words: 8
```

### 🛠️ Generate Word Analysis Report

#### Description
Extend your program to analyze the cleaned words and write results to an output file. This helps practice both text manipulation and file output.

#### Requirements
Completed program should:

- Count how many times each word appears
- Display the top 5 most frequent words in the console
- Save a report file named `report.txt` that includes:
- total words
- unique word count
- top 5 words with frequencies
- Ignore empty strings and whitespace-only entries

```text
Example Output (console):
Top 5 words:
python: 2
is: 2
hello: 1
students: 1
fun: 1
```
