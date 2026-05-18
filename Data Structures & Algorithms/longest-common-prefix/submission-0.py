class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=strs[0]
        for str in strs:
            while not str.startswith(pref):
                pref=pref[:-1]
        return pref
        