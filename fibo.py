# from my_sys import feb, feb2
# from my_sys import feb as hehe

# feb(500)
# hehe(700)
# print(feb2(1000))

import my_sys

if __name__ == "__main__":
    import sys
    my_sys.feb(int(sys.argv[1]))

