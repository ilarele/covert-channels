#!/usr/bin/python

import time

NR_BENCKMARKS = 10
LOOPS = 10000000

def benchmark():
    start_time = time.time()
    count = 0
    while LOOPS > count:
        count += 1
    end_time = time.time()
    
    assert end_time >= start_time
    return end_time - start_time, LOOPS 

if __name__ == "__main__":
    count = 0
    total_dtime = 0
    total_loops = 0
    while count < NR_BENCKMARKS:
        dtime, loops = benchmark()
        total_dtime += dtime
        total_loops += loops
        count += 1
    
    avg_dtime = total_dtime/count
    avg_loops = total_loops/count

    f = open('benchmark.txt', 'w+')
    f.write(repr(avg_loops) + " " + repr(avg_dtime) + "\n")
    f.close()
