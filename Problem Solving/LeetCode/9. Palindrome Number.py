class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        rev_str_num = ""
        for ch in str_num[::-1]:
            rev_str_num += ch
            
        if rev_str_num == str_num:
            return True
        else:
            return False
