def split_and_join(line):
        line = line.split()
        result = "-".join(line)
        return result
    # write your code here


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)