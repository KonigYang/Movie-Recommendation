#!/usr/bin/python
import sys
from pymongo import MongoClient
from decimal import Decimal

def mapper():
    for line in sys.stdin:
        data = line.strip().split("::")
        items, recpower = data
        recpower = Decimal(recpower)
        itemi, itemj = list(map(int,items.split("_")))        
        userlisti = db.items.find({"iid":itemi}, {"userlist":1, "_id":0})
        userlist_i = []
        for userlist in userlisti:
        	userlist_i = userlist["userlist"]        
        userlistj = db.items.find({"iid":itemj}, {"userlist":1, "_id":0})
        userlist_j = []
        for userlist in userlistj:
        	userlist_j = userlist["userlist"]
        Wij = recpower/len(userlist_j)
        Wji = recpower/len(userlist_j)
        for users in userlist_i:
        	print("{0}\t{1},{2}".format(users, itemj, Wji))
		for users in userlist_j:
			print("{0}\t{1},{2}".format(users, itemi, Wij))

if __name__ == "__main__":
	client = MongoClient('localhost',27017)
	db = client['recommend']
	mapper()
