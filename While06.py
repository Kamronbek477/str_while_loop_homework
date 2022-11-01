


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
        if s[i]=='a':
            k+=1
        if s[i]=='u':
            k+=1
        if s[i]=='e':
            k+=1
        if s[i]=='i':
            k+=1
        if s[i]=='o':
            k+=1
        else:
            k+=0
            
        i+=1
    
    return len(s)-k

print(main("Ccuijoyyaez"))