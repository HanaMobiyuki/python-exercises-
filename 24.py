# Write a Python program to test whether a passed letter is a vowel or not.
def vowel_check(l):
    if l == 'a' or l == 'e' or l == 'i' or l == 'o'or l == 'u' or l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U':
        return True
    else:
        return False
print(vowel_check('a'))
print(vowel_check('Z'))