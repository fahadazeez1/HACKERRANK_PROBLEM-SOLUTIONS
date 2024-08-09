# Python solution file
cube = lambda x: x**3 

def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))