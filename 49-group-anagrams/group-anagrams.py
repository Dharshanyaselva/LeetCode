class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res_map = {}

        for item in strs:
            key = tuple(sorted(item))
            res_map.setdefault(key, []).append(item)

        return list(res_map.values())
        
        