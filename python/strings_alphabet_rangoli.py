def print_rangoli(size):
        m = chr(96+size)
        w = m
        
        for i in range(size):
                print("-"*(2*size - 2-2*i),end="")
                for j in range(2*i + 1):

                        print(m,end="")
                        if((j+(2*size - 2-2*i)) <= 2*size - 1):
                                m = chr(ord(m)-1)
                        else :
                                m = chr(ord(m)+1)
                        if(i==size-1 and j == 2*i):
                                print("",end="")
                        else:
                                print("-",end="")
                print("-"*(2*size - 3-2*i))
                m = w
        for i in range(size-1):
                print("-"*(2*size - 2-2*(size-2-i)),end="")
                for j in range(2*(size-2-i) + 1):
                        print(m,end="")
                        if(i==size-1 and j == 2*i):
                                print("",end="")
                        else:
                                print("-",end="")
                print("-"*(2*size - 3-2*(size-2-i)))
                m = w


    # your code goes here
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)