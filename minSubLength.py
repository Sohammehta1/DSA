'''
The idea is to maintain a left and right pointer which iterates through the array.
If we find a subarray sum >=target we compare with min_len. and then increament L to figure 
out if  a smaller subarray satisfies the condition. 
At the end of each loop we increament r.
We repeat this until r==len(arr)

T.C -> O(N)
'''

from typing import List


def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    
    min_len = float('inf')
    l =0
    curr_sum = 0
    for r in range(len(nums)):
        curr_sum += nums[r]
        if curr_sum>=target:
            min_len = min(min_len,r-l+1)
            curr_sum -= nums[l]
            l+=1
            while curr_sum >=target:
                min_len = min(min_len, r-l+1)
                curr_sum -= nums[l]
                l+=1
    return min_len if min_len!=float('inf') else 0