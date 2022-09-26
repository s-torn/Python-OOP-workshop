from my_decorator import add_logging

@add_logging('log.txt')
def example():
   return 'I\'m a function'

@add_logging('log.txt')
def example_2(n1, n2):
    return n1 + n2

if __name__ == '__main__':
    print(example())
    print(example_2(2, 3))