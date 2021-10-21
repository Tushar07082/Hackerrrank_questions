a = input().split()
n = int(a[0])
m = int(a[1])
for i in range(n//2):
        print("-"*(((m//2)-1)-3*i) + ".|."*(2*i +1) + "-"*(((m//2)-1)-3*i))
print("-"*(m//2-3)+"WELCOME"+"-"*(m//2 -3 ))
for i in range(n//2):
        print("-"*(((m//2)-1)-3*(n//2 - i-1)) + ".|."*(2*(n//2-1-i) +1) + "-"*(((m//2)-1)-3*(n//2 - i-1)))