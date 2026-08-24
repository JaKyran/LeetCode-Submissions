class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a default dict so you can add values that arent seen before
        res = defaultdict(list)
        # iterate through each string in the list "strs"
        for s in strs:
            # create a list of 26 zeros, one slot for each letter a-z, to count letters
            count = [0] * 26
            # iterate through each character in the current string "s"
            for c in s:
                # figure out which letter this is (a=0, b=1, ... z=25) and add 1 to its slot
                count[ord(c) - ord('a')] += 1
            # check the dictionary for this letter-count signature (as a tuple, since lists
            # can't be dict keys), if not there, create an empty list and append the original string
            res[tuple(count)].append(s)
        # return the full list with every value thats inside res
        return list(res.values())