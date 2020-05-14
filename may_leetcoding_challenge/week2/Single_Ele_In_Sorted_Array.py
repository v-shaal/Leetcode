# [540] Single Element in a Sorted Array
##
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
# Find this single element that appears only once.

# Example 1:
#
#
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
#
#
# Example 2:
#
#
# Input: [3,3,7,7,10,11,11]
# Output: 10

# Note: Your solution should run in O(log n) time and O(1) space.
#

#Trivial SOlution

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        se =set()
        count=0
        for i in nums:
            count+=i
            se.add(i)

        sum_of_element = sum(se)
        missing_ele = 2*sum_of_element-count
        return missing_ele



# Complexity O(log n)

#Soln by #be_focused

#If every element in the sorted array were to appear exactly twice, they would occur in pairs at indices i, i+1 for all even i.
#
#Equivalently, nums[i] = nums[i+1] and nums[i+1] != nums[i+2] for all even i.
#
#When we insert the unique element into this list, the indices of all the pairs following it will be shifted by one, negating the above relationship.
#
#So, for any even index i, we can compare nums[i] to nums[i+1].
#
#If they are equal, the unique element must occur somewhere after index i+1
#If they aren't equal, the unique element must occur somewhere before index i+1
#
#Using this knowledge, we can use binary search to find the unique element.
#
#We just have to make sure that our pivot index is always even, so we can use mid = 2 * ((lo + hi) // 4) instead of the usual mid = (lo + hi) // 2.


def singleNonDuplicate(self, nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = 2 * ((lo + hi) // 4)
        if nums[mid] == nums[mid+1]:
            lo = mid+2
        else:
            hi = mid
    return nums[lo]
