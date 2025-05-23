# 3551. Minimum Swaps to Sort by Digit Sum
# You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.
# Return the minimum number of swaps required to rearrange nums into this sorted order.
# A swap is defined as exchanging the values at two distinct positions in the array.
# Example 1:
# Input: nums = [37,100]
# Output: 1
# Explanation:
# Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]
# Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain the sorted order.
# Thus, the minimum number of swaps required to rearrange nums is 1.
# Example 2:
# Input: nums = [22,14,33,7]
# Output: 0
# Explanation:
# Compute the digit sum for each integer: [2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]
# Sort the integers based on digit sum: [22, 14, 33, 7]. The array is already sorted.
# Thus, the minimum number of swaps required to rearrange nums is 0.
# Example 3:
# Input: nums = [18,43,34,16]
# Output: 2
# Explanation:
# Compute the digit sum for each integer: [1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]
# Sort the integers based on digit sum: [16, 34, 43, 18]. Swap 18 with 16, and swap 43 with 34 to obtain the sorted order.
# Thus, the minimum number of swaps required to rearrange nums is 2.
# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# nums consists of distinct positive integers.
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digitSum(num):
            s=0
            while num:
                s+=num %10
                num=num//10
            return s
        t=[]
        for i,v in enumerate(nums):
            t.append((digitSum(v), v, i))
        m =sorted(t)
        count = 0
        index_1 = [v[2] for v in t]
        index_2 = [v[2] for v in m]
        m_1 ={}
        for i in range(len(index_1)):
            m_1[index_1[i]]=i
        
        for i in range(len(index_1)):
            if index_1[i]!=index_2[i]:
                a = m_1[index_2[i]]
                index_1[i], index_1[a]=index_1[a],index_1[i]
                m_1[index_1[i]]=i
                m_1[index_1[a]]=a
                count+=1
        return count
