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
