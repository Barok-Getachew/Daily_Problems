class Solution(object):
    def isPalindrome(self, x):
        return(str(x)==str(x)[::-1])
        # By casting the number type to string and cheking the reverse string to its orginal string and the to return the bool