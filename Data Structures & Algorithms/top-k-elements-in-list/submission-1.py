class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # needed explicit help, need to reivew all solutions
        map = {}
        for num in nums:
            map[num] = 1 + map.get(num, 0)

        heap = []
        for num in map:
            heapq.heappush(heap, (map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        # need to better analyze this part
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result