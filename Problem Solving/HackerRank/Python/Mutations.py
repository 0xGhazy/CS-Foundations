def mutate_string(string, position, character):
    """abrackdabra"""
    new_string = ""
    for i in range(len(string)):
        if i == position:
            new_string += character
        else:
            new_string += string[i]
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)