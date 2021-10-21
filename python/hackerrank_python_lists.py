n = int(input())
l =[]
for i in range(n):
        s = input()
        # print(s)
        j = s.split(" ")
        # print(j[1])
        k = j[0]
        
        if k == "append":
                m = int(j[1])
                l.append(m)
        elif k == "print":
                print(l)
        elif k == "remove":
                m = int(j[1])
                l.remove(m)
        elif k == "insert":
                m = int(j[1])
                a = int(j[2])
                l.insert(m,a)
                # print(l)
        elif k == "sort":
                l.sort()
        elif k == "pop":
                l.pop()
        elif k == "reverse":
                l.reverse()
