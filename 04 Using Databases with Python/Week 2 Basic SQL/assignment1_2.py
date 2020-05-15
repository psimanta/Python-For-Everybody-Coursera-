import sqlite3
from sqlite3 import Error
import urllib.request, urllib.parse, urllib.error

#url = 'https://www.py4e.com/code3/mbox.txt'
#text = urllib.request.urlopen(url)

conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
conn.commit()

fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        pieces = line.split()
        print(pieces)
        #cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
        #row = cur.fetchone()
'''        if row is None:
            cur.execute('INSERT INTO Counts (email, count) VALUES(?,1)',(email,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
            conn.commit()

sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()
'''
