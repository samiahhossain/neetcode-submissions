class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = {} 

        for word in strs:
            letters = "".join(sorted(word))
            if letters in map:
                map[letters].append(word)
            else:
                map[letters] = [word]

        return list(map.values())