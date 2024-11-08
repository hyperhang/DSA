class Solution:
    def compressedString(self, word: str) -> str:
        compressed_word = []
        i = 1
        cur = word[0]
        count = 1
        while i < len(word):
            if word[i] == cur :
                if count < 9:
                    count += 1
                else:
                    compressed_word.append(f"9{cur}")
                    count = 1
            else:
                compressed_word.append(f"{count}{cur}")
                count = 1
                cur = word[i]
            i += 1
        compressed_word.append(f"{count}{cur}")
        return ''.join(compressed_word)
    
sol = Solution()
word = "abcde"
print(sol.compressedString(word))