
def check(number):
    n = int(number)
    while n < 1 or n >100 :
            n = int(input())

    if n % 2 == 0: # even
        if n in range (2,5+1):
            print("Not Weird")
        if n in range(6,20+1):
            print("Weird")
        if n > 20:
            print("Not Weird")
    else:
        print("Weird")



n = int(input())
check(n)
