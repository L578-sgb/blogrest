#!C:/Python/Python39/python.exe

def fibonacci(n):
    a = 0
    b = 1
    c =a + b
    i = 0
    while i < n:
        print(c)
        a = b
        b = c
        c = a + b
        i = i + 1

print("Content-type: text/html")
print()
print("Serie de Fibonacci <br>")
fibonacci(10)