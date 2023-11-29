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