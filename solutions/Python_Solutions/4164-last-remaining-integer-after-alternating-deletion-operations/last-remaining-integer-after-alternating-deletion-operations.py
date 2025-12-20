'''
write 1 -> n
starting from left, delete every second number
starting from right, delete every single number
return last integer

start w left, then right then left .....

holy moly n can be 10^15
o(1) or lg n will be chill


ok so in first op we remove every even number. 
second op we remove 

left only ops:

    #0 operations done
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 

    #1 operation done, now we have indicies st (index % 2 ^ (number of operations ) == 0)
0 2 4 6 8 10 12 14

    #2 operations done, noe we have all indicies st (index % 2 (number)) 
0 4 8 12



0 8


okay so each left operation leaves us with all indicies st (index % 2 ^ (number of operation1) == 0)

right:


    #0 operatoins done
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 

    #1 operation done, odd inderx wsx
1 3 5 7 9 11 13 15

    #2 operation done, ind (index + 1)  % 2 ^ (num ops) == 0
3 7 11 15

    #3 operation done. (index + 1) % 2 ^ (3) == 0
7 15

    #4 operation done

15


i think that after each operation we will have a clue about one of the bits of the final integer. 
then that would be log wrt input n .

operation 1: 
after n operations, you will only have the indices st (index % 2 ^ n) == 0

operation 2: 
after n operations, you will have the ind st (index + 1) % 2 ^ n == 0


ok now need to: 
i think i need to be able to get a bit of information for each step that we do
also know how to have it bounded by n. i guess we have to do this lg n number of times or very close to that. bc we kill half each time yad yad

0     1     2     3     4     5     6     7     8     9     10     11     12     13     14     15     
0000  0001  0010  0011  0100  0101  0110  0111  1000  1001  1010   1011   1100   1101   1110   1111

operation 1: (keep all indicies w a 0 in last position)

0      2      4      6      8      10      12      14
0000   0010   0100   0110   1000   1010    1100    1110

operation 2: (keep all indices with a 1 in second to last position)

2      6      10      14
0010   0110   1010    1110



operation 1 second time: (keep all ind w 0 in third from left pos)
2      10
0010   1010

operation 2 second time: (keep ind w a 1 in fourth pos)

10
1010



ok clearly found the way that I can do this for n as a power of 2. i am not sure this generalizes to other n unfortunately. 
n = 13 instead of 16

0     1     2     3     4     5     6     7     8     9     10     11     12
0000  0001  0010  0011  0100  0101  0110  0111  1000  1001  1010   1011   1100


operation 1: (we still keep all bits where last bit isd 00)

0     2     4     6     8     10     12     
0000 0010   0100  0110  1000  1010   1100


operation 2: (keep all where second last is 0.) why is it now selecting for a 0 in that position instead of a 1? is it because in the list we gave the operation 2, it was odd? 7 elements instead of even. 
maybe the even oddness of length of arr we give to each operation really matters. 


0      4      8      12
0000   0100  1000    1100
operation 1 pt 2
0      8
0000   1000
operation2 pt 2

8


vars numLeft, isOpOne


ok new theory for nth operatoin 2: 
numOpsDone
if len(arr) % 2 == 0:
    keep all indices where (numOpsDone - 1 from left ) bit is 1 
else:
    keep all indices where (numOpsDone - 1 from left ) bit is 0

i think the operation 1 will always just select for its bit to be 0

ok so if we have a list of even length, doing both operations will result in a list of size n // 2

1 2 3 4 5 6 7
1 3 5 7

1 3 5 7 

if we have odd length..... we get either n + 1 // 2 or math.ceil(n / 2)


'''
import math
class Solution:
    def lastInteger(self, n: int) -> int:
        numLeft = n
        isOpOne = True
        numOpsDone = 1
        numBitsNeeded = math.ceil(math.log2(n)) + 1
        bits = [0] * numBitsNeeded
        
        while numLeft > 1:
            if isOpOne:
                bits[-numOpsDone] = 0
                #need to update numLeft
            
            else:
                if numLeft % 2 == 0:
                    #even length of nums left
                    bits[-numOpsDone] = 1

                else:
                    #odd length of nums left
                    bits[-numOpsDone] = 0

            isOpOne = not isOpOne
            numOpsDone += 1
            numLeft = math.ceil(numLeft / 2)
        
        #print("bits: " + str(bits))

        #ok lets get out bits back into an int. AND MUST REMEMBER TO ADD ONE BECAUSE WE WERE WORKING W ZERO BASED INDEX BUT OUR LIST OF 1 TO N IS 1 BASED DUH

        num = 0

        for i in range(len(bits)):
            bit = bits[numBitsNeeded - i - 1]
            num += bit * (2 ** i)

        num += 1

        return num    


        
