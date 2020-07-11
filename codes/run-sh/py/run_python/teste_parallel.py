
from joblib import Parallel, delayed
from math import sqrt
def f(i):
	print i, sqrt(i)
Parallel(n_jobs=2, prefer="threads")(\
                   delayed(f)(i ** 2) for i in range(10))

