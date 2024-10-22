from typing import List

# Touchscreen Keyboard
KEYBOARD = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]

def char_posistion(c1: str):
    for i, row in enumerate(KEYBOARD):
        try:
            j = row.index(c1)
            break
        except ValueError:
            continue
    return i, j

def char_distance(c1: str, c2: str):
    c1_pos = char_posistion(c1)
    c2_pos = char_posistion(c2)
    return abs(c1_pos[0] - c2_pos[0]) + abs(c1_pos[1] - c2_pos[1])
    

def distance(word_1: str, word_2: str):
    acc_distance = 0
    for chars in zip(word_1, word_2):
        acc_distance += char_distance(*chars)
    return acc_distance

num_cases = int(input())
for _ in range(num_cases):
    spell_checker_list: List[List] = []
    typed_word, num_words = input().split()
    num_words = int(num_words)
    for _ in range(num_words):
        suggested_word = input()
        d = distance(typed_word, suggested_word)
        spell_checker_list.append([suggested_word, d])
        spell_checker_list = sorted(spell_checker_list, key = lambda w_d: w_d[0])
    spell_checker_list = sorted(spell_checker_list, key = lambda w_d: w_d[1])
    for word_distance in spell_checker_list:
        print(*word_distance)

