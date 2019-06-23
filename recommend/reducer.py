#!/usr/bin/python
import sys

def reducer():
    prevKey = None
    recdict = {}
    for line in sys.stdin:
        data = line.strip().split("\t")
        key, value = data 
        if prevKey and prevKey!=key:
            print("{0}::{1}".format(prevKey, recdict))
            recdict.clear()
        prevKey = key
        item, power = list(map(float, value.split(",")))
        if item in recdict:
            recdict[item] += power
        else:
            recdict[item] = power
    if prevKey :
        print("{0}::{1}".format(prevKey, recdict))

if __name__ == "__main__":
    reducer()
