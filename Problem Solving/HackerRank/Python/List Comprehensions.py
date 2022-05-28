if __name__ == '__main__':
    result = []
    summ = 0
    x = int(input())
    xlist = list(range(0,x+1))
    y = int(input())
    ylist = list(range(0,y+1))
    z = int(input())
    zlist = list(range(0, z+1))
    n = int(input())
    test = [[x, y, z] for x in xlist for y in ylist for z in zlist]
    for i in test:
        summ = sum(root for root in i)        
        if summ == n:
            summ = 0
            pass
        else:
            result.append(i)
    print(result)
