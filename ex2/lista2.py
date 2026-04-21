def count_vowels(s: str) -> int:
    count: int = 0
    for i in s:
        if (i in "AEIOU") or (i in "aeiou"):
            count += 1
    return count

def is_palindrome(s: str) -> bool:
    pal: bool = False
    s = s.lower().replace(" ", "")
    if s == s[::-1]:
        pal = True
    return pal

def count_occurrences(s: str, chars: list) -> dict:
    occ: dict = {}
    s = s.lower()
    for i in chars:
        occ[i] = s.count(i)
    return occ

def unique_elements(original: list) -> list:
    return list(dict.fromkeys(original)) # set() não preserva a ordem

def cumulative_sum(numbers: list) -> list:
    cum: list = list(range(len(numbers)))
    for i in range(len(numbers)):
        cum[i] = sum(numbers[0:i+1])
    return cum

def word_frequency(words_str: str) -> dict:
    words: list = words_str.lower().split(" ")
    freq: dict = {}
    for i in words:
        freq[i] = words.count(i)
    return freq

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    merge: dict = {}
    for i in set(dict1) | set(dict2):
        merge[i] = dict1.get(i, 0) + dict2.get(i, 0)
    return merge

def is_valid_parentheses(s: str) -> bool:
    mapping: dict = {')': '(', '}': '{', ']': '['}
    stack: list = []
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0

def anagram_groups(words_str: str) -> dict:
    words: list = words_str.lower().split(" ")
    anagrams: dict = {}
    for i in words:
        key = ''.join(sorted(i))
        if key not in anagrams.keys():
            anagrams[key]: list = []
        anagrams[key].append(i)
    return anagrams

def filter_and_square(numbers: list, threshold: int = 0) -> list:
    sqred: list = []
    for i in numbers:
        if i > threshold:
            sqred.append(i**2)
    return sqred

def transform_words(words: list, transform) -> list:
    return list(map(transform, words))

def dict_from_lists(keys: list, values: list, filter_none = True) -> dict:
    k: int = 0
    out: dict = {}
    for i in keys:
        if (values[k] is not None) or (not filter_none):
            out[i] = values[k]
        k += 1
    return out
    
def set_operations(list1: list, list2: list, operation: str = "union") -> set:
    set1: set = {item.lower() for item in list1}
    set2: set = {item.lower() for item in list2}
    result:set = {}
    if operation == "union":
        result = set1.union(set2)
    elif operation == "intersection":
        result = set1.intersection(set2)
    elif operation == "difference":
        result = set1.difference(set2)
    return result
