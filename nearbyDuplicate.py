from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq_map  = {}
        result: bool = False
        for i, num in enumerate(nums):
            if num in freq_map:
                if abs(freq_map[num] - i) < k:
                    result = True
                    break
            else:
                freq_map[num] = i
        return result