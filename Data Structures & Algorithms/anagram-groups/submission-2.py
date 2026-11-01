class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # did this on my own but need to read through other solutions
        map = {} 

        for word in strs:
            letters = "".join(sorted(word))
            if letters in map:
                map[letters].append(word)
            else:
                map[letters] = [word]

        return list(map.values())