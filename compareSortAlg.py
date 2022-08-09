# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Mohammad Zarei
# Created Date: 9 Aug 2022
# ---------------------------------------------------------------------------
"""
comparing the time peformance of sorting algorithms
"""

#imports
from random import randint
from timeit import repeat
from sort import *
import numpy as np
import pandas as pd
import seaborn as sns 


def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from sort import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=5)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run

    # print(f"Algorithm: {algorithm}. Mean execution time: {np.min(times)}")
    return np.min(times)


ALGORITHMS = ['sorted', 'insertion', 'merge', 'quick', 'bucket']

if __name__ == "__main__":
    times = []
    for alg in ALGORITHMS:
        for size in [100,1000,10000,100000]:
            array = [randint(0,size) for i in range(size)]
            meanTime = run_sorting_algorithm(algorithm=alg, array=array)
            times.append([alg, size, meanTime])
    
    times = pd.DataFrame(times, columns=['ALG', 'SIZE', 'TIME'])
    times.to_csv('times.csv')
    fig = sns.lineplot(data=times, x="SIZE", y="TIME", hue="ALG", markers=True).get_figure()
    fig.savefig('plot.png')
