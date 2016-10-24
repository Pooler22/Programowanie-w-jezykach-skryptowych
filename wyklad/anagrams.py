from functools import reduce


def is_anagram(a, b):
    return sorted(a) == sorted(b)


print(is_anagram("asd", "dsa"), is_anagram("asd", "dsa."))


def is_anagram_ext(a, *b):
    return sorted(a) == sorted(b[0]) if (len(b) == 1) else reduce((lambda x, y: x if (is_anagram(x, y)) else ""), b)


print(is_anagram_ext("asd", "dsa", "sda"), is_anagram_ext("asd", "sda"), is_anagram_ext("asd", "sda", "dsa."))
