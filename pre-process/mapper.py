#!/usr/bin/python
import sys
def mapper():
    for line in sys.stdin:
        data = line.strip().split("::")
        user, movie, r, t = data
        print("user{0}\t{1}".format(user,movie)) 
        print("movie{0}\t{1}".format(movie,user)) 
if __name__ == "__main__":
    mapper()
