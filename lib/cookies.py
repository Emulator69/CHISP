import sqlite3 as lite
import re

class Cookies(object):

    def __init__(self, db):
        self.con = lite.connect(db)
        self.con.text_factory = str
        self.db = self.con.cursor()


    def listRows(self, x, y, z):
        """Grab rows from cookies table accordingly"""
        tSet = set()

        q = self.db.execute('SELECT "{0}" FROM `cookies` WHERE "{1}" = ?;'.format(x, y),
                    (z,))
        while True:
            r = q.fetchone()
            if not r:
                break
            else:
                tSet.add(r[0])
        return tSet


    def dotsetPurge(self, tgtSet):
        """Return a sorted and set, list of domains with the leading . removed"""
        tmpList = list(tgtSet - self.mSet)
        tmpSet = set()
        tmpList2 = []
        for i in tmpList:
            if re.match('\.', i):
                
                ## Add to tmpSet for deletion
                tmpSet.add(i)
                
                ## Add to tmpList2 for addition minus the .
                tmpList2.append('.'.join(i.split('.')[1:]))

        ## Iterate through set of deletes and remove from tmpList           
        for i in tmpSet:
            tmpList.remove(i)

        ## Make final set by combining the lists
        return sorted(list(set(tmpList + tmpList2)))


    def setMixer(self, setX, setY):
        """Generate intersections of setY from setX"""
        tmpSet = set()
        for x in setX:
            for y in setY:
    #            print ('Checking %s against %s' % (x, y))
                if x in y:
    #                print('Found %s in %s' % (y, x))
                    tmpSet.add(x)
        return tmpSet
