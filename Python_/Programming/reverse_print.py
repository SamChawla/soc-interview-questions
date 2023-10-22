# Write a program to print a string in reverse order without using any string functions or [::-1] notation.

def print_reverse(data):
    if len(data) == 0:
        return
    print_reverse(data[1:])
    print(data[0], end='')



if __name__ == '__main__':
    print_reverse('hello world')

