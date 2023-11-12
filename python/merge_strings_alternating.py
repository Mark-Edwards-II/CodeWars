"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

def mergeAlternately(word1: str, word2: str) -> str:
    new_string = ""
    i = 0
    while i < len(word1) and i < len(word2):
        new_string+=word1[i]
        new_string+=word2[i]
        i+=1
    if len(word1) > len(word2):
        new_string+=word1[len(word2):]
    elif len(word2) > len(word1):
        new_string+=word2[len(word1):]
    return new_string



def test():
    assert mergeAlternately(word1 = "abc", word2 = "pqr") == "apbqcr"
    assert mergeAlternately(word1 = "ab", word2 = "pqrs") == "apbqrs"
    assert mergeAlternately(word1 = "abcd", word2 = "pq") == "apbqcd"

test()