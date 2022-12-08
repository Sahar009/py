import random
options = ('rock', 'paper', 'scissors')
player = None
computer = random.choice(options)

player = input('Enter a choice (rock, paper, scisssors')


# range produces a sequence of object from start  to end

print(range(100))

# looping through a range

for item in range(0, 44):
    print(item)

# range doesnt really care abt the variables

for _ in range(0, 10):
    print(_)

    # also takes a 3 params
for _ in range(0, 10, 2):
    print(_)
    # range inverse
# (10,0,-1)

for _ in range(2):
    print(range(10))

    # functions
    # A function is a block of code which only runs when it is called.


def say_hello():
    print('hello everyone')
# say_hello()


def say_hi(name, number):
    print('hello{},aged {}'.format(name, number))


say_hi('sodiq', 32)
