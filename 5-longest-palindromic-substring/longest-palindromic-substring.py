class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''
        for center in range(len(s)):
            even_palindrome = self.findPalindrome(s, center, center + 1)
            odd_palindrome = self.findPalindrome(s, center, center)
            longest_palindrome = max([longest_palindrome, even_palindrome, odd_palindrome], key=len)
        return longest_palindrome
    
    def findPalindrome(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]