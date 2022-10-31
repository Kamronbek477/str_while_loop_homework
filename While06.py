def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    k=0
    i=0
    while i<len(s):
        if str(s[i])==('a'):
            k+=1
        if str(s[i])==('e'):
            k+=1
        if str(s[i])==('o'):
            k+=1
        if str(s[i])==('i'):
            k+=1
        if str(s[i])==('u'):
            k+=1
        i+=1
    
    return k

print(main("CodeschoolUz"))