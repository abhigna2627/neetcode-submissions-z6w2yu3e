class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        
        
        for s in strs:
            n=len(s)
            encoded_string+=str(n)+"#"+s

        return encoded_string;

    def decode(self, s: str) -> List[str]:
        
        res = []
        i = 0

        while i < len(s):

            # Find the '#'
            j = i
            while s[j] != "#":
                j += 1

            # Length of the next word
            length = int(s[i:j])

            # Extract the word
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            # Move to the next encoded word
            i = j + 1 + length

        return res
        
