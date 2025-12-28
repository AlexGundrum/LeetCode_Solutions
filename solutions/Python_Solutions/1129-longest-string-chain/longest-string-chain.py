'''
a word is a pred of another if you can insert exactly one (NOT ZERO!) chars in word a to make it == to wordB

abc -> abac

a word chain is a sequence of words where w1 -> w2 -> w3 etc....

a single word is a word chain with k == 1

return length of longest possible word chain with words chosen from given list of words


ok so need to have lists of each len of words. have all words with 2 char 3 char etc. 


dp(str) -> the length of chain you can make with this as the link. 

do we have to run this dp on each of the input words? 
can't just start with smallest len words. might have len of 2 4 5 6 so the 2 which is smallest won't be longest 

lets see how slow that is. 
shoot we can have up to 1000 words in list. but i think most of those will get cached anyway? 



ok so once we're given a word we will check the things one char longer than it .

but what is the way to best see if they are predecessors? two pointer? 

zzzc     dabc
012
len 4, - 2 + 1
'''

from functools import lru_cache
class Solution:
    def is_predecessor(self, w1, w2):
        l1, l2 = 0, 0
        leftCount = 0
        while l1 < len(w1) and l2 < len(w2):
            if w1[l1] == w2[l2]:
                leftCount += 1
                l1 += 1
                l2 += 1
            else:
                break
        rightCount = 0
        r1, r2 = len(w1) - 1, len(w2) - 1

        while 0 <= r1 < len(w1) and 0 <= r2 < len(w2):
            if w1[r1] == w2[r2]:
                rightCount += 1
                r1 -= 1
                r2 -= 1
            else:
                break
        
        #l1 means that l1 chars were matched in w2
        #len() - r1 + 1 = number of chars matched on right half
        return (leftCount + rightCount) >= len(w1)
        if leftCount == len(w1) or rightCount == len(w1):
            return True
        if leftCount + rightCount + 1 == len(w2):
            return True
        return False

    def longestStrChain(self, words: List[str]) -> int:
        words_by_char = defaultdict(list)
        for WORD in words:
            words_by_char[len(WORD)].append(WORD)


        @lru_cache(maxsize = None)
        def dp(string):
            LEN = len(string)
            words_to_check = words_by_char[LEN + 1]
            maxSeen = 1
            #ok so now we have to check all future johns
            for word in words_to_check:
                if self.is_predecessor(string, word):
                    val = 1 + dp(word)

                    maxSeen = max(maxSeen, val)
        
            return maxSeen
        
        best = 1
        for word in words:
            score = dp(word)
            best = max(best, score)

        return best