class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for i in nums:
            if i not in count_map:
                count_map[i] = 0

            count_map[i]+=1
        
        count_pairs = list(count_map.items())

        count_pairs.sort(key=lambda x: x[1],reverse=True)

        max_list = [x[0] for x in count_pairs]

        return max_list[0:k:1]

            
        