from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]

    Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]
    """
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                return [i,j]
            
def test_two_sum():
    assert two_sum([2,7,11,15], 9) == [0,1]
    assert two_sum([3,2,4],6) == [1,2]
    assert two_sum([3,3], 6) == [0,1]

def memory_usage():
    import tracemalloc
    # starting the monitoring
    tracemalloc.start()
    # function call
    two_sum([2,7,11,15],9)
    # displaying the memory
    print(tracemalloc.get_traced_memory())

if __name__ == "__main__":
    test_two_sum()
    memory_usage()