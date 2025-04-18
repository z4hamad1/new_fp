"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from typing import List
from collections import Counter

def get_longest_diverse_words(file_path: str) -> List[str]:
    words = text_n.split()
    clean_words = [word.strip(string.punctuation) for word in words if word]

    def key_func(word):
        return len(set(word)), len(word)

    sorted_words = sorted(clean_words, key=key_func, reverse=True)
    return sorted_words[:10]


def get_rarest_char(file_path: str) -> str:
    char_counts = {}
    for ch in text_n:
        char_counts[ch] = char_counts.get(ch, 0) + 1

    return min(char_counts, key=char_counts.get)


def count_punctuation_chars(file_path: str) -> int:
    return sum(1 for ch in text_n if ch in string.punctuation)


def count_non_ascii_chars(file_path: str) -> int:
    return sum(1 for ch in text_n if ord(ch) > 127)


def get_most_common_non_ascii_char(file_path: str) -> str:
    char_counts = {}
    for ch in text_n:
        if ord(ch) > 127:
            char_counts[ch] = char_counts.get(ch, 0) + 1

    if not char_counts:
        return "Non-ASCII нет", 0

    max_char = max(char_counts, key=char_counts.get)
    return max_char, char_counts[max_char]


if __name__ == "__main__":
    path_name = 'data.txt'

    with open(path_name, "r", encoding="utf-8") as f:
        text_n = f.read()

    print('Топ 10 самых длинных слов', get_longest_diverse_words(text_n))

    print('Редкий символ:', get_rarest_char(text_n))

    print('Пунктуационных знаков:', count_punctuation_chars(text_n))

    print('Не ASCII символов:', count_non_ascii_chars(text_n))
 
    print('Наиболее частый не ASCII символ:', get_most_common_non_ascii_char(text_n))
