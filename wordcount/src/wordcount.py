import re, sys
from typing import Tuple

def count_lines(s: str) -> Tuple[list[str], float]:
    line_separator = re.compile(r'\n')
    lines = line_separator.split(string=s)
    line_count = len(lines) - 1
    # print(f"string {s} will be split in {lines}. count is {line_count}")
    return lines, line_count

def count_words(lines: list[str]) -> Tuple[list[str], float]:
    words = []
    for line in lines:
        line_words = line.split()
        words.extend([word for word in line_words])
    word_count = len(words)
    # print(f"lines {lines} contain words {words}. count is {word_count}")
    return words, word_count


def process_stdin() -> bytes:
    return "".join(sys.stdin)

def main():
    # print(f"input your string")
    s = process_stdin()
    # print(s)
    lines, line_count = count_lines(s)
    words, word_count = count_words(lines)
    byte_count = len(s)
    
    print(f"{line_count} {word_count} {byte_count}")

