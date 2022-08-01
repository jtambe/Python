'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from queue import PriorityQueue
        
        d = {}
        s = set()
        res = []
        q = PriorityQueue(k)
        qLength = 0
        
        for i in range(len(nums)):
            if(nums[i] in s):
                d[nums[i]] = d[nums[i]] + 1
            else:
                s.add(nums[i])
                d[nums[i]] = 1
                
        for x in d:
            if(qLength < k):
                q.put((d[x], x))
                qLength += 1
            else:
                minElement = q.get()
                if(minElement[0] < d[x]):
                    q.put((d[x], x))
                else:
                    q.put((minElement[0], minElement[1]))
               
        while not q.empty():
            res.append(q.get()[1])
            
        return res
