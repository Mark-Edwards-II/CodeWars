"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""



def reverseVowels(s: str) -> str:
    rev_s=s[::-1]
    s = [*s]
    j=0
    run = True
    for i in range(len(s)):
        if s[i] in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
            while j < len(rev_s) and run:
                if rev_s[j] in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
                    s[i]=rev_s[j]
                    run=False
                j+=1
        run=True
    return "".join(s)

def tests():
    assert reverseVowels(s = "hello") == "holle"
    assert reverseVowels(s = "leetcode") == "leotcede"

tests()