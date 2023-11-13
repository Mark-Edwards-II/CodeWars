import math
"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""




#  
    
def gcdOfStrings(str1: str, str2: str) -> str:
    new_string = ""
    gcd=math.gcd(len(str1),len(str2))
    i = gcd
    new_string = str1[:gcd]
    for item in [str1,str2]:
        for i in range(0,len(item),gcd):
            temp=""
            for j in range(i,i+gcd, 1):
                temp+=item[j]
            if temp != new_string:
                return ""
    print(new_string)
    return new_string


def tests():
    assert gcdOfStrings(str1 = "ABCABC", str2 = "ABC") == "ABC"
    assert gcdOfStrings(str1 = "ABABAB", str2 = "ABAB") == "AB"
    assert gcdOfStrings(str1 = "LEET", str2 = "CODE") == ""

tests()