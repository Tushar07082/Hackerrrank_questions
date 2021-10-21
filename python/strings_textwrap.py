import textwrap

def wrap(string, max_width):
        result = ""
        j =0
        for i in range(len(string)):
               if ((i+1)%max_width == 0):
                     result +=  string[j:(i+1)]+"\n"
                     j = i+1
        result += string[j:]
        return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)