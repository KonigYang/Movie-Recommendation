#!/usr/bin/python
import sys
from pymongo import MongoClient

def reducer():
    Values = ""
    prevKey = None
    for line in sys.stdin:
        data = line.strip().split("\t")
        key, value = list(map(str,data)) 
        if prevKey and prevKey!=key:
            if prevKey.startswith("movie"):
                item = prevKey.split("movie")
                userlist = list(map(int, Values.split(";")))
                doc = {"iid":int(item[1]) , "userlist":userlist}
                db.items.insert_one(doc)
            if prevKey.startswith("user"):
                user = prevKey.split("user")
                itemlist = list(map(int, Values.split(";"))) 
                doc = {"uid":int(user[1]) , "itemlist":itemlist}
                db.users.insert_one(doc)
                print("{0}:{1}".format(prevKey, Values))                
            Values = ""
        prevKey = key
        if Values == "" :
            Values = value
        else: 
            Values = Values + ";" + value
    if prevKey :
        if prevKey.startswith("movie"):
            item = prevKey.split("movie")
            userlist = list(map(int, Values.split(";"))) 
            doc = {"iid":int(item[1]), "userlist":userlist}            
            db.items.insert_one(doc)
        if prevKey.startswith("user"):
            user = prevKey.split("user")
            itemlist = list(map(int, Values.split(";"))) 
            doc = {"uid":int(user[1]) , "itemlist":itemlist}
            db.users.insert_one(doc)
            print("{0}:{1}".format(prevKey, Values))

if __name__ == "__main__":
    client = MongoClient('localhost',27017)
    db = client['recommend']
    reducer()
