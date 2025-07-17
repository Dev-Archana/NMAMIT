def is_palindrome(s):

    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    
 
    if clean_s == clean_s[::-1]:
        return "YES"
    else:
        return "NO"


input_str = input()


print(is_palindrome(input_str))