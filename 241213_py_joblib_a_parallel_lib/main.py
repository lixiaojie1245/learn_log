from joblib import Parallel, delayed

def fib(n):
    if n<2:
        return 1
    return fib(n-1)+fib(n-2)

print(Parallel(n_jobs=-1)(delayed(fib)(n) for n in range(1,35)))

