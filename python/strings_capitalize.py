def solve(s):
    result=""
    for i in range(len(s)):
        
        if((i!=0 and s[i-1]==" ") or i==0):
            result += s[i].upper()
        else:
            result += s[i]
    return result
s = input()
print(solve(s))