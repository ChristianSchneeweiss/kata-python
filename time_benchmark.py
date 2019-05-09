from time import time


def benchmark(func):
    def new_func():
        start = time()
        func()
        end = time()
        print(f"Took {(end - start) * 1000} milliseconds")
    
    return new_func
