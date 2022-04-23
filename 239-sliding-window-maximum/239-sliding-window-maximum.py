class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         브루스포스로 풀면 타임아웃
#         if not nums:
#             return nums
        
#         r= []
#         for i in range(len(nums)-k+1):
#             r.append(max(nums[i:i+k]))
#         return r

#       큐사용                 
        q = collections.deque()
        sol = []
        for i in range(len(nums)):
            if q and i - q[0] == k:
                q.popleft()
            while q:
                if nums[q[-1]] < nums[i]:
                    q.pop()
                else:
                    break
            q.append(i)
            if i >= k - 1:
                sol.append(nums[q[0]])
        return sol