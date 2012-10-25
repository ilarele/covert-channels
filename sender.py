#!/usr/bin/python
IN_FILE = 'in.txt'
BENCHMARK_FILE = 'benchmark.txt'
BZ_BIT_TIME_SEC = 1

import time

def readBenchmark(filename):
    f = open(filename, 'r+')
    bench_info = f.readline().split()
    f.close()
    loops, time_interval = bench_info[0], bench_info[1]

# generate bz 
def generateBz(bit, loops, time_interval):
    assert (bit == True or bit == False)
    if bit:
        end_time = time.time() + 1
        while time.time() < end_time:
            pass
    else:
        time.sleep(1)

def getFileContent(filename):
    f = open(filename, 'r+')
    to_send_txt = f.read()
    f.close()
    return to_send_txt

def getBits(text):
    b_array = []
    for character in text:
       assert len(character) == 1
       bits = ord(character)
       for i in xrange(8):
           bit = bool((bits >> (7-i)) & 1)
           assert (bit == True or bit == False)
           b_array.append(bit)
    return b_array

if __name__ == "__main__":
    # wait some seconds to be sure that the responder waits for me
    time.sleep(2)

    # read benchmark
    loops, time_interval = readBenchmark(BENCHMARK_FILE)

    # read payload from file
    to_send_txt = getFileContent(IN_FILE)
    bits_array = getBits(to_send_txt)

    # convert to covert channel
    for bit in bits_array:
        generateBz(bit, loops, time_interval)
    

