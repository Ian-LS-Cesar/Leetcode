class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int] | None:
        hashmap = {}
        for i in range(len(nums)):
            numero_complementar = target - nums[i]
            if numero_complementar in hashmap:
                return [i, hashmap[numero_complementar]]
            hashmap[nums[i]] = i
        return []
