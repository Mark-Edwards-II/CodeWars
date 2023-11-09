"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
"""

def unique_in_order(sequence):
    if not sequence:
        return []
    new_sequence = [sequence[0]]
    for letter in sequence:
        if letter != new_sequence[len(new_sequence)-1]:
            new_sequence.append(letter)
    return new_sequence


"""Should work with empty sequence"""
def empty_sequence():
    assert unique_in_order("") == []
    assert unique_in_order([]) == []
    assert unique_in_order(()) == []

"""Should work with single element sequence"""
def element_sequence():
    assert unique_in_order("A") == ["A"]
    assert unique_in_order(["A"]) == ["A"]
    assert unique_in_order(("A",)) == ["A"]

"""Should reduce duplicates"""
def reduce_duplicates():
    assert unique_in_order("AA") == ["A"]
    assert unique_in_order("AAAABBBCCDAABBB") == ["A", "B", "C", "D", "A", "B"]

"""Should be case-sensitive"""
def case_sensitive():
    assert unique_in_order("ABBCcA") == ["A", "B", "C", "c", "A"]

"""Should work with different element types"""
def element_types():
    assert unique_in_order([1, 2, 3, 3, -1]) == [1, 2, 3, -1]
    assert unique_in_order(["a", "b", "b", "a"]) == ["a", "b", "a"]

empty_sequence()
element_sequence()
reduce_duplicates()
case_sensitive()
element_types()