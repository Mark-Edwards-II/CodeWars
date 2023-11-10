def fun_with_anagrams(text):
    for i in range(len(text)):
        for j in range(i+1, len(text)):
            temp1=text[i]
            temp2=text[j]
            if sorted(temp1) == sorted(temp2):
                text.remove(text[j])
    return text
text=["code","aaagmnrs","anagrams","doce"]
print(fun_with_anagrams(text))