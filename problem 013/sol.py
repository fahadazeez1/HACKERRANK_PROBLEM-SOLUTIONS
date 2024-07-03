# Python solution file
def list_operations(n, commands):
    my_list = []
    
    for command in commands:
        parts = command.split()
        operation = parts[0]

        if operation == "insert":
            index = int(parts[1])
            element = int(parts[2])
            my_list.insert(index, element)
        elif operation == "print":
            print(my_list)
        elif operation == "remove":
            element = int(parts[1])
            my_list.remove(element)
        elif operation == "append":
            element = int(parts[1])
            my_list.append(element)
        elif operation == "sort":
            my_list.sort()
        elif operation == "pop":
            my_list.pop()
        elif operation == "reverse":
            my_list.reverse()

if __name__ == '__main__':
    N = int(input())
    commands = [input() for _ in range(N)]
    list_operations(N, commands)
