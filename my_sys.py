print("welcome sys@!")

def he(a):
    print(a)
he("sys test!")

# Modules
# sys.py
def feb(n):    # in dãy số Fibonacci đến n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def feb2(n):   # trả về dãy số Fibonacci đến n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
