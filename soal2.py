def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    
    str_x = str(x)
    return str_x == str_x[::-1]

# Contoh penggunaan
x = 121
print(isPalindrome(None, x))  # Output: True
