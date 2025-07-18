S = 'ABCBC'
n = 3
palindromes = []

def check_palindrome(s1):
    return s1 == s1[::-1]


for i in range(0, len(S) - n + 1):
    substr = S[i:i + n]
    if check_palindrome(substr):
        palindromes.append(substr)

print("Palindromic substrings of length", n, "are:", palindromes)
