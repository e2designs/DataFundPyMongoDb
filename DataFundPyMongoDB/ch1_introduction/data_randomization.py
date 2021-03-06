"""
A stochastic process is a family of random variables from some probability space
into a state space (whew!).

Simply, it is a random process through time. Data randomization is the process
of selecting values from a sample in an unpredictable manner with the goal of
simulating reality. Simulation allows application of data randomization in data
science. The previous section demonstrated how simulation can be used to
realistically compare iterables (list comprehension, generator comprehension,
and generators).

In Python , pseudorandom numbers are used to simulate data randomness (reality).
They are not truly random because the 1st generation has no previous number.
We have to provide a seed (or random seed) to initialize a pseudorandom number
generator. The random library implements pseudorandom number generators for
various data distributions, and random.seed() is used to generate the initial
(1st generation) seed number.

The following code example reads a CSV file and converts it to a list of regular
dictionary elements.
- The code continues by creating a random number used to retrieve a random
  element from the list.

- Next, a generator of three randomly selected elements is created and
  displayed. The code continues by displaying three randomly shuffled elements
  from the list.

- The next section of code deterministically seeds the random number generator,
  which means that all generated random numbers will be the same based on the
  seed. So, the elements displayed will always be the same ones unless the seed
  is changed.

- The code then uses the system’s time to nondeterministically generate random
  numbers and display those three elements.

- Next, nondeterministic random numbers are generated by another method and
  those three elements are displayed.

- The final part creates a names list so random choice and sampling methods can
  be used to display elements.
"""
import csv
import random
import time


def read_dict(f, h):
    """Converts a csv file to a list of OrderedDict Elements"""
    input_file = csv.DictReader(open(f), fieldnames=h)
    return (input_file)


def conv_reg_dict(d):
    """
    Converts a list of OrderedDict elements to a list of regular
    dictionary elements for easier processing
    """
    return [dict(x) for x in d]


def r_inds(ls, n):
    """Generates a random list of n elements"""
    length = len(ls) - 1
    yield [random.randrange(length) for _ in range(n)]


def get_slice(ls, n):
    """
    Creates a randomly shuffled list of n elements from the dictionary list
    """
    return ls[:n]


def p_line():
    """Prints a blank line"""
    print()


if __name__ == '__main__':
    # Read CSV and convert to list of dictionary elements
    f = 'data/names.csv'
    headers = ['first', 'last']
    r_dict = read_dict(f, headers)
    dict_ls = conv_reg_dict(r_dict)

    # Create random number based on the number rof indices from the dictionary
    # list
    n = len(dict_ls)
    r = random.randrange(0, n-1)
    print('randomly selected index:', r)
    print('randomly selected element:', dict_ls[r])

    # Create generatorand populated with 3 randomly determined elements
    elements = 3
    generator = next(r_inds(dict_ls, elements))
    p_line()
    print(elements, 'randomly generated indicies:', generator)
    print(elements, 'elements based on indicies:')
    for row in generator:
        print(dict_ls[row])

    # randomly shuffles the indicies and puts them in list x
    x = [[i] for i in range(n-1)]
    random.shuffle(x)
    p_line()
    print('1st', elements, 'shuffled elements:')
    ind = get_slice(x, elements)
    for row in ind:
        print(dict_ls[row[0]])

    # Create deterministic random based on static seed
    seed = 1
    random_seed = random.seed(seed)
    rs1 = random.randrange(0, n-1)
    p_line()
    print('deterministic seed', str(seed) + ':', rs1)
    print('corresponding element:', dict_ls[rs1])

    # Create random seed based on system time
    t = time.time()
    random_seed = random.seed(t)
    rs2 = random.randrange(0, n-1)
    p_line()
    print('non-deterministic time seed', str(t) + ' index:', rs2)
    print('corresponding element:', dict_ls[rs2], '\n')
    print(elements, 'random elements seeded with time:')
    for i in range(elements):
        r = random.randint(0, n-1)
        print(dict_ls[r], r)

    # Random seed with no variable
    random_seed = random.seed()
    rs3 = random.randrange(0, n-1)
    p_line()
    print('non-deterministic auto seed:', rs3)
    print('corresponding element:', dict_ls[rs3], '\n')
    print(elements, 'random elements auto seed:')
    for i in range(elements):
        r = random.randint(0, n-1)
        print(dict_ls[r], r)
    names = []
    for row in dict_ls:
        name = row['last'] + ', ' + row['first']
        names.append(name)
    p_line()
    print(elements, 'names with "random.choice()":')
    for row in range(elements):
        print(random.choice(names))
    p_line()
    print(elements, 'names with "random.sample()":')
    print(random.sample(names, elements))

# OUTPUT
"""
randomly selected index: 1
randomly selected element: {'first': 'Adam', 'last': 'Zapel'}

3 randomly generated indicies: [0, 1, 1]
3 elements based on indicies:
{'first': 'Adam', 'last': 'Baum'}
{'first': 'Adam', 'last': 'Zapel'}
{'first': 'Adam', 'last': 'Zapel'}

1st 3 shuffled elements:
{'first': 'Adam', 'last': 'Zapel'}
{'first': 'Adam', 'last': 'Baum'}

deterministic seed 1: 0
corresponding element: {'first': 'Adam', 'last': 'Baum'}

non-deterministic time seed 1646660038.127642 index: 0
corresponding element: {'first': 'Adam', 'last': 'Baum'}

3 random elements seeded with time:
{'first': 'Adam', 'last': 'Baum'} 0
{'first': 'Adam', 'last': 'Zapel'} 1
{'first': 'Adam', 'last': 'Baum'} 0

non-deterministic auto seed: 1
corresponding element: {'first': 'Adam', 'last': 'Zapel'}

3 random elements auto seed:
{'first': 'Al', 'last': 'Bino'} 2
{'first': 'Adam', 'last': 'Baum'} 0
{'first': 'Adam', 'last': 'Zapel'} 1

3 names with "random.choice()":
Baum, Adam
Bino, Al
Baum, Adam

3 names with "random.sample()":
['Zapel, Adam', 'Baum, Adam', 'Bino, Al']
"""
