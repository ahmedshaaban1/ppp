import multiprocessing as mp

def double(x):
    return x * x

pool = mp.Pool(5)

print(pool.map(double, [1, 2, 3]))
