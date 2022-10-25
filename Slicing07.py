def main(s,n):
    """
    The s string variable is given. return all characters except n characters at the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    if (2 <= len(s) <= 10**5) and (1 <= n <= len(s)):
        return s[0:(len(s)-n)]
print(main('hello',25))