def split_and_join(line):
    # write your code here
    lines = line.split(" ")
    return "-".join(lines)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)