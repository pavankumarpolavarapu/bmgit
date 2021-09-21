from tinydb import TinyDB, Query, where
import os


def main():
    db = TinyDB('matches20210916.json')
    matches = db.all()
    for match in matches:     
        #pass



if __name__ == '__main__':
    exit(main())
