print ("hello")
print (1)
print(type(1))

key_ = True
if key_ :
    print("Be careful not to fall off!")

print (2+2)

s = 'First line.\nSecond line.'   # \n means newline
print(s)

print('doesn\'t')  #use \'
print("doesn't")
print('"Isn\'t," they said.')

print('C:\some\name')
print(r'C:\some\name')

print(3 * 'a' + 'b') #aaab
print('Py' 'thon') #Python

word = 'Python'
print(word[0])
print(word[-1])
print(word[:3])
print(word[2:5])

print('J' + word[1:])
print('Py' + word[-2:])

s = 'pythonbasic'
print(len(s))

squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[3])
print(squares + [36, 49, 64, 81, 100])
squares[3] = 64
print(squares)
squares.append(216)
squares.append(3**4)
print(squares)


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
print(len(letters)) #4

n = ['a', 'b', 'c']
m = [1, 2, 3] 
x = [n, m]   #[['a', 'b', 'c'], [1, 2, 3]]
print(x)
print(x[0])    #['a', 'b', 'c']
print(x[0][1])  #b


a, b = 0, 1
while a < 10:
    print("a =", a)
    print("b =", b)
    a, b = b, a+b

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

print()

# if Statements
x = int(input("Please enter an integer: "))

if x < 0:
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
else:
    print('More')

#for Statements¶
languages = ['python', 'javascript', 'java']
for w in languages:
    print(w, len(w))

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
#lặp qua key và value của users nếu value = inactive thi xóa nó khỏi users
for key, value in users.copy().items():
    if value == 'inactive':
        del users[key]
print(users)
# Strategy:  Create a new collection
#tạo một mảng rỗng for qua users nếu status == active thì thêm user vào mảng
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(users)

for x in range(5):
    print(x)

print(list(range(5,10)))    #[5, 6, 7, 8, 9]
print(list(range(0, 10, 3)))    #[0, 3, 6, 9]
print(list(range(-10, -100, -30)))    #[-10, -40, -70]

for n in range(2, 10): # Vòng lặp cho n từ 2 đến 9
    for x in range(2, n):  # Vòng lặp cho x từ 2 đến n-1
        if n % x == 0:     # Kiểm tra n có chia hết cho x không
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
          # Nếu không thi n là số nguyên tố
        print(n, 'is a prime number')
# 2 là số nguyên tố vì nó không chia hết cho bất kỳ số nào từ 2 đến 1.
# 3 là số nguyên tố vì không có số nào từ 2 đến 2 chia hết cho 3.
# 4 không phải số nguyên tố vì 4 chia hết cho 2 (4 equals 2 * 2).
# 5 là số nguyên tố.
# 6 không phải số nguyên tố vì 6 chia hết cho 2 (6 equals 2 * 3).
# 7 là số nguyên tố.
# 8 không phải số nguyên tố vì 8 chia hết cho 2 (8 equals 2 * 4).
# 9 không phải số nguyên tố vì 9 chia hết cho 3 (9 equals 3 * 3).

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# pass Statements
# while True:
#     pass 

# class MyEmptyClass:
#     pass

# def initlog(*args):
#     pass

# match Statements

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(http_error(404))

class Point:
    def __init__(self, x, y): #định nghĩa class point với hai tham số truyền vào x,y
        self.x = x
        self.y = y
        
    def __repr__(self): #định nghĩa  để trả về biểu diễn chuỗi của đối tượng Point khi được in ra.
        return f"Point(x={self.x}, y={self.y})"

def where_is(point): # hàm where_is nhận tham số là point
    match point: # sử dụng match để kiểm tra
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
var = 5
print(Point(1, var))
print(Point(1, y=var))
print(Point(x=1, y=var))
print(Point(y=var, x=1))


from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': ").lower())

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")