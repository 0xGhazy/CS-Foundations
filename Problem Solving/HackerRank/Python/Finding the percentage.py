
n = int(input())
student = dict()
for i in range(0, n):
    x = input()
    x = x.split(" ")
    student[x[0]] = "{:.2f}".format((float(x[1]) + float(x[2]) + float(x[3])) / 3)
query_name = input()
print(student[query_name])
