def string_palindrome(s):
    s=s.lower()
    new_s=s[::-1]
    if s==new_s:
        print("Palindrome")
    else:
        print("NOT")
string_palindrome("Ana")
