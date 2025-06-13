import collections

def sliding_windows_max(nums, k):
    output = []
    left = right = 0
    queue = collections.deque()
    
    while right < len(nums):
        while queue and nums[queue[-1]] < nums[right]:
            queue.pop()
        queue.append(right)
        if left > queue[0]:
            queue.popleft()
        if (right + 1) >= k:
            output.append(nums[queue[0]])
            left += 1   
        right += 1
    return output

nums = [1, 3, -1, -3, 5, 3, 6, 7] 
k = 3 

print(sliding_windows_max(nums, k))