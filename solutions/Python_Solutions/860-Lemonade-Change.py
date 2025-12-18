'''
https://leetcode.com/problems/lemonade-change/description/?envType=daily-question&envId=2024-08-15

At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

'''

class Solution(object):
    def lemonadeChange(self, bills):
        register = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if bill == 5:
                register[5] += 1
            elif bill == 10:
                if register[5] == 0:
                    return False
                register[10] += 1
                register[5] -= 1
            else:
                if register[5] == 0:
                    return False
                if register[10] == 0:
                    if register[5] >= 3:
                        register[20] += 1
                        register[5] -= 3
                    else:
                        return False
                else:
                    register[20] += 1
                    register[10] -= 1
                    register[5] -=1
        
        return True
        
        
