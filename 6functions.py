#  say hello
def sayHello():
    """Print a Fibonacci series up to n."""
    print('hello all')

sayHello()

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    """Do nothing, but document it.
    No, really, it doesn't do anything.
    """
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

def concat(*args, sep="/"):
    return sep.join(args)

print( concat("earth", "mars", "venus") )
print( concat("earth", "mars", "venus", sep=".") )

#lambda
def make_incrementor(n):
    return lambda x: x + n

lambda_func = make_incrementor(42)
print(lambda_func(2))