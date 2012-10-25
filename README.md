
// CPU
// dom0
// - benchmark:
// - scp bench.py root@ip:
// - ssh root@ip1 'python bench.py' &&  ssh root@ip2 'python bench.py'
// - bench.py -> writes in file benchmark.txt: loops_per_sec N
// 
- sender do not need benchmark, it sends signals "seconds" based

sender + receiver (interpret msgs):
- while (1)
    if new_sec:
        print loops
        (compare with benchmark => percentage)
        loops = 0
        print percent
        
comunicate: 0 1 0 1 0 1 1 1 ... => send ascii message
start and wait to have 50% => start countig 25 sec with 50%
Y = 25 sec: 50 % -> it is ok to comunicate
tin cate X = 3 sec per bit
bit 0 - max_loops_per_z
bit 1 - lower_loops_per_z


correcting codes:::::

// cache

