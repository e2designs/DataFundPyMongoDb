import csv, time, numpy as np


def read_dict(f, h):
    """Converts a csv file to a list of OrderedDict Elements"""
    input_file = csv.DictReader(open(f), fieldnames=h)
    return input_file


def conv_reg_dict(d):
    """
    Converts a list of OrderedDict elements to a list of regular
    dictionary elements for easier processing
    """
    return [dict(x) for x in d]


def sim_times(d, n):
    """
    runs a simulation that creates two lists—lsd and lsgc. 
    List lsd contains n run times for list comprension and 
    list lsgc contains n run times for generator comprehension. 
    Using simulation provides a more accurate picture of the true time 
    it takes for both of these processes by running them over and over (n times).
    """
    i = 0
    lsd, lsgc = [], []
    while i < n:
        start = time.time()
        [x for x in d]
        time_d = time.time() - start
        lsd.append(time_d)
        start = time.time()
        (x for x in d)
        time_gc = time.time() - start
        lsgc.append(time_gc)
        i += 1
    return (lsd, lsgc)


def gen(d):
    yield (x for x in d)


def sim_gen(d, n):
    i = 0
    lsg = []
    generator = gen(d)
    while i < n:
        start = time.time()
        for row in generator:
            None
        time_g = time.time() - start
        lsg.append(time_g)
        i += 1
        generator = gen(d)
    return lsg


def avg_ls(ls):
    return np.mean(ls)


if __name__ == "__main__":
    f = "data/names.csv"
    headers = ["first", "last"]
    r_dict = read_dict(f, headers)
    dict_ls = conv_reg_dict(r_dict)
    n = 1000
    ls_times, gc_times = sim_times(dict_ls, n)
    g_times = sim_gen(dict_ls, n)
    avg_ls = np.mean(ls_times)
    avg_gc = np.mean(gc_times)
    avg_g = np.mean(g_times)
    gc_ls = round((avg_ls / avg_gc), 2)
    g_ls = round((avg_ls / avg_g), 2)
    print("generator comprehension:")
    print(gc_ls, "times faster than list comprehension\n")
    print("generator:")
    print(g_ls, "times faster than list comprehension")
