# Write a function that returns the second-smallest

# int in a given list of ints

def second_smallest(nums):
    nums.sort()
    return nums[1]

# Write a function that, given a list of ints, returns

# True if the list contains a 2 next to a 2 somewhere.

# has22([1, 2, 2]) -> True

# has22([1, 2, 1, 2]) -> False

# has22([2, 1, 2]) -> False

def has22(nums):
    for j in range(1, len(nums)):
        if nums[j-1] == 2 and nums[j-1] == nums[j]:
            return True
    return False