def is_palindrome(s):

    if len(s) == 1:
        return True
    elif len(s) == 2:
        return s[0] == s[-1]
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:len(s) - 1])
        else:
            return False
    