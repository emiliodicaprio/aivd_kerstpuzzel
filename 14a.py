import copy
import itertools
import re

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "?",
]  # noqa: E501

text_encoded_binary = "- 1 0 - - 0 0 0 - 0 - 0 - 0 - - 0 - 1 0 - - 0 1 0 1 - - - - 1 0 - 1 0 1 0 0 0 0 0 0"
flipped_text = text_encoded_binary.replace("1", "a").replace("0", "1").replace("a", "0")

b_alphabet = [bin(ord(l)) for l in alphabet]
input_list = text_encoded_binary.split(" ")
# characters = ["".join(input_list[i : i + 7]) for i in range(0, len(input_list), 7)]


def split_into_characters(input_list):
    return ["".join(input_list[i : i + 7]) for i in range(0, len(input_list), 7)]


def weird_reversal(input_list, flip_first=True):
    flipped_list = copy.copy(input_list)
    if flip_first:
        for i in range(0, len(input_list), 2):
            flipped_list[i] = reverse_unknown_bit(input_list[i])
    else:
        for i in range(1, len(input_list), 2):
            flipped_list[i] = reverse_unknown_bit(input_list[i])

    return flipped_list


def reverse_unknown_bit(bit: str):
    match bit:
        case "0":
            return "1"
        case "1":
            return "0"
        case "-":
            return "-"


def find_possible_letters(char_with_unknowns: list):
    # Check the existing bytes against letters in alphabet
    r_pat = "0b" + char_with_unknowns
    r_pat = r_pat.replace("-", ".")

    possible_letters = []

    pat = re.compile(r_pat)
    for i, pos_chr in enumerate(b_alphabet):
        match = re.match(pat, pos_chr)

        if match is not None:
            possible_letters.append(alphabet[i])

    return possible_letters


characters = split_into_characters(weird_reversal(input_list, False))
possible_letters = []
for letter in characters:
    possible_letters.append(find_possible_letters(letter))

print(possible_letters)
