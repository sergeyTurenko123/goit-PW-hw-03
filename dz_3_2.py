from multiprocessing import Pool, cpu_count
import time


def factorize(*args):
    start = time.time()
    n = 1
    numbers = []
    for i in args:
        while n <= i:
            if i % n == 0:
                numbers.append(n)
            n+=1
    end = time.time() - start
    print (numbers, end)

if __name__ == "__main__":

    cpu_count = cpu_count()
    pool = Pool(cpu_count)
    pool.map(factorize, (1500000, 1000000, 100000))   
    