class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            dict[sortedS].append(s)
        return list(dict.values())
        