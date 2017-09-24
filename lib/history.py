import sqlite3 as lite
import re

class History(object):

    def __init__(self, db):
        self.con = lite.connect(db)
        self.con.text_factory = str
        self.db = self.con.cursor()


    def listRows(self):
        """Grab urls from urls table accordingly"""
        urlHTTP = set()
        urlHTTPS = set()
        
        q = self.db.execute('SELECT `url` FROM `urls`;')
        while True:
            r = q.fetchone()
            if not r:
                break
            else:
                if re.match('https://', r[0]):
                    urlHTTPS.add(r[0].split('/')[2])
                else:
                    urlHTTP.add(r[0].split('/')[2])
        return urlHTTP, urlHTTPS