class Solution:
    def removeVowels(self, s: str) -> str:
        new = []
        vowels = 'aeiou'
        for char in s:
            if char not in vowels:
                new.append(char)

        return ''.join(new)