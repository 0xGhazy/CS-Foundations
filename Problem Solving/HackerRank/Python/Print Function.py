def PrintFunction(n):
    test = ""
    for i in range(1,n+1):
        test += str(i)
    print(test)

if __name__ == '__main__':
    n = int(input())
    PrintFunction(n)