import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#fname = input('Enter file name: ')
#if (len(fname) < 1): fname = './Data Files/mbox.txt'
fname = r'C:\Users\sachi\Documents\Python for Everybody\Using Databases with Python\mailbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    orglist = pieces[1].split("@")
    org = orglist[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (str(org),))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (str(org),))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (str(org),))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
