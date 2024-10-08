class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1 if len(sentence1) <= len(sentence2) else sentence2
        s2 = sentence2 if len(sentence1) <= len(sentence2) else sentence1
        i, j = 0, 0
        words1 = s1.split(' ')
        words2 = s2.split(' ')
        while i < len(words1) and words1[i] == words2[i]:
            i += 1
        while j < len(words1) and words1[-1-j] == words2[-1-j]:
            j += 1
        print(f"i  = {i}, j = {j}, len(word1) = {len(words1)}")
        if i+j >= len(words1):
            return True
        return False
            
sol = Solution()
sentence1 = "My name is Haley"
sentence2 = "My Haley"

sentence1 = "of"
sentence2 = "A lot of words"

sentence1 = "Eating right now"
sentence2 = "Eating"

sentence1 = "This is a amy"
sentence2 = "a amy"

print(sol.areSentencesSimilar(sentence1, sentence2))
