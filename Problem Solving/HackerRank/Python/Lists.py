main_list = []

n = int(input())

for i in range(0, n):
    command = input()

    if "insert" in command:
        command = command.split()
        index = command[1]
        value = command[2]
        main_list.insert(index, value)

    elif "print" in command:
        print(main_list)


    elif "remove" in command:
        command = command.split()
        item = command[1]
        main_list.remove(item)

    elif "append" in command:
        command = command.split()
        item = command[1]
        main_list.append(item)

    elif "sort" in command:
        main_list.sort() 

    elif "pop" in command:
        main_list.pop()

    elif "reverse" in command:
        main_list.reverse()
