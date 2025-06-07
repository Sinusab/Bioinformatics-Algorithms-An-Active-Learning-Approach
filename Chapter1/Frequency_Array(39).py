def Pattern_Count(text,pattern):
    k = len(pattern)
    num = 0
    for i in range(len(text)-k+1):
        if text[i:i+k] == pattern:
            num+=1
    return num

import itertools

def PatternToNumber(pattern):
    k = len(pattern)
    letters = ['A','C','G','T']
    combinations = [''.join(p) for p in itertools.product(letters, repeat=k)]
    for i in range(4**k):
        if combinations[i]==pattern:
            return i

PatternToNumber('ATGCAA')

import itertools

def NumberToPattern(number, k):
    letters = ['A','C','G','T']
    combinations = [''.join(p) for p in itertools.product(letters, repeat=k)]
    return combinations[number]

NumberToPattern(5437,7)

def ComputingFrequencies(text, k):
    frequency_array = []
    for i in range(k**4):
        frequency_array.append(0)
    for i in range(len(text)-k):
        pattern = text[i:i+k]
        j = PatternToNumber(pattern)
        frequency_array[j] += 1
    return frequency_array

ComputingFrequencies('ACTGACTCCCACCCC', 3)

def FrequentWords(text, k):
    frequent_patterns = []
    frequent_array = ComputingFrequencies(text, k)
    max_count = max(frequent_array)
    for i in range(k**4):
        if frequent_array[i] == max_count:
            pattern = NumberToPattern(i, k)
            frequent_patterns.append(pattern)
    return frequent_patterns

FrequentWords('ACTGACTCCCACCCC', 3)
