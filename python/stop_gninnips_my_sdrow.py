"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
"""

def spin_words(sentence):
    sentence_b = sentence.split(" ")
    for j in range(len(sentence_b)):
        if len(sentence_b[j]) > 4:
            new_word = ""
            for i in range(len(sentence_b[j])-1, -1, -1):
                new_word+=sentence_b[j][i]
            sentence_b[j] = new_word
    return " ".join(sentence_b)



def single_word():
    assert spin_words("Welcome") == "emocleW"
    assert spin_words("to") == "to"
    assert spin_words("CodeWars") == "sraWedoC"

def multiple_words():
    assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
    assert spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes"

single_word()
multiple_words()