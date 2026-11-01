class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        map = {} # 

        for word in strs:
            letters = "".join(sorted(word))
            if letters in map:
                map[letters].append(word)
            else:
                map[letters] = [word]

        return list(map.values())