from typing import List
"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    max_candy = candies[0]
    for i in range(1, len(candies), 1):
        if candies[i] > max_candy:
            max_candy = candies[i]

    for j in range(len(candies)):
        if candies[j]+ extraCandies >= max_candy:
            candies[j] = True
        else:
            candies[j] = False

    return candies

# kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3)



def tests():
    # assert kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3) == [True,True,True,False,True]
    # assert kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1) == [True,False,False,False,False]
    # assert kidsWithCandies(candies = [12,1,12], extraCandies = 10) == [True,False,True]
    assert kidsWithCandies(candies = [2,8,7], extraCandies = 1) == [False,True,True]

tests()