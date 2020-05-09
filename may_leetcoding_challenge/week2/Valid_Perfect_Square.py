# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
# Input: 16
# Output: true
#
# Example 2:
#
#
# Input: 14
# Output: false

#read more at https://cp-algorithms.com/num_methods/roots_newton.html
def NewtonMethod(self, num):
    r = num
    while r*r > num:
        r = (r + num/r) // 2
    return r*r == num


#binary Search Method
def BinarySearch(self, num):
    left = 0
    right = num

    while left <= right:
        mid = left + (right-left)//2
        if  mid ** 2 == num:
            return True
        elif mid ** 2 > num:
            right = mid -1
        else:
            left = mid +1
    return False