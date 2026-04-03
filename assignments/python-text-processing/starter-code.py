"""
Python Text Processing - Starter Code

Run this file with:
python starter-code.py
"""

PUNCTUATION = ".,!?;:"


def clean_text(text):
    """Convert to lowercase and remove selected punctuation."""
    text = text.lower()
    for ch in PUNCTUATION:
        text = text.replace(ch, "")
    return text


def load_words(file_path):
    """Read text from a file and return cleaned words."""
    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned = clean_text(raw_text)
    words = cleaned.split()
    return words


def word_frequencies(words):
    """Build a frequency dictionary for a list of words."""
    freq = {}
    for word in words:
        if word.strip() == "":
            continue
        freq[word] = freq.get(word, 0) + 1
    return freq


def top_n_words(freq, n=5):
    """Return the n most common words as (word, count) tuples."""
    return sorted(freq.items(), key=lambda item: item[1], reverse=True)[:n]


def write_report(path, total_words, unique_words, top_words):
    """Write analysis results to a report file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write("Text Analysis Report\n")
        f.write("====================\n")
        f.write(f"Total words: {total_words}\n")
        f.write(f"Unique words: {unique_words}\n\n")
        f.write("Top words:\n")
        for word, count in top_words:
            f.write(f"- {word}: {count}\n")


def main():
    input_file = "sample-text.txt"
    output_file = "report.txt"

    words = load_words(input_file)
    freq = word_frequencies(words)
    top_words = top_n_words(freq, 5)

    print(f"Total words: {len(words)}")
    print("Top 5 words:")
    for word, count in top_words:
        print(f"{word}: {count}")

    write_report(output_file, len(words), len(freq), top_words)
    print(f"Report written to {output_file}")


if __name__ == "__main__":
    main()
