import sqlite3
import sys
from datetime import datetime

conn = sqlite3.connect('logger.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Log
(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    date CHARACTER(10),
    cycle INTEGER,
    romance CHARACTER(1),
    caff INTEGER,
    sunny CHARACTER(1),
    jour CHARACTER(1),
    writePo CHARACTER(1),
    readPo CHARACTER(1),
    willPo CHARACTER(1),
    convo CHARACTER(1),
    willConvo CHARACTER(1),
    employed CHARACTER(1),
    twits INTEGER,
    email INTEGER,
    app INTEGER,
    fb INTEGER,
    insta INTEGER,
    li INTEGER,
    skype INTEGER,
    reddit INTEGER,
    sms INTEGER,
    poms INTEGER
)
''')

print("if your distraction is not listed, please add it to the db.")

### To do: Write if there's already an entry for today, update the entryself.
## If date is undefined, add date. Else ask if they're trying to update. If yes,
## print entry types and ask which entry they're trying to update. Give entries
## a number.

date = str(datetime.today()).split()[0]
print("date is ", date)
# print("here's the date. and type. and the string. adn that type.", date, type(date), date_as_str,type(date_as_str) )
# print("date as list", date

prompt = input("if you want to exit, press e, if testmode press t, otherwise press whatever to continue :) ")

if prompt is 'e': sys.exit()
if prompt is 't' :
    cycle = None
    romance = None
    caff = None
    sunny = None
    jour = None
    writePo = None
    readPo = None
    willPo = None
    convo = None
    willConvo = None
    employed = None
    twits = None
    email = None
    app = None
    fb = None
    insta = None
    li = None
    skype = None
    reddit = None
    sms = None
    poms = None

    answers = [21, 'y', 24, 'n', 'n', 'n','n','n','n','n','n', 4, 45, 4, 10, 30, 1, 1, 1, 1, 4]
    i = 0

    categories = [cycle, romance, caff, sunny , jour , writePo, readPo ,willPo,convo,willConvo,employed,twits,email,app,fb,insta, li,skype,reddit,sms,poms]
    for q in categories :
        q = answers[i]
        i = i+1





else:
    cycle = input('day of cycle is: ')
    romance = input('am i romantically involved? y or n ')
    caff = input('how much coffee did i drink today? in oz: ')
    sunny = input('is it sunny out? y or n ')
    jour = input('did i journal today? y or n ')
    writePo = input('did i write poetry today? y or n ')
    readPo = input('did i read poetry today? y or n ')
    willPo = input('do i plan on engaging with poetry today? y or n ')
    convo = input('did i have a nice conversation with someone today? y or n ')
    willConvo = input('do i anticipate engaging in a nice conversation today? y or n ')
    employed = input('am i employed? y or n ')
    twits = input('# of Twitter distractions? ')
    email = input('# of email distractions? ')
    app = input('# of phone app distractions? (other) ')
    fb = input('# of Facebook distractions? ')
    insta = input('# of Instagram distractions? ')
    li = input('# of LinkedIn distractions? ')
    skype = input('# of Skype distractions? ')
    reddit = input('# of Reddit distractions? ')
    sms = input('number of SMS message distractions? ')
    poms = input('how many poms of work did i do? ')


print("to review: ", id, date, cycle, romance, caff, sunny, jour, writePo, readPo, willPo, convo,
willConvo, employed, twits, email, app, fb, insta, li, skype, reddit, sms, poms )

cur.executemany('''INSERT OR IGNORE INTO Log
    (
    date,
    cycle,
    romance,
    caff,
    sunny,
    jour,
    writePo,
    readPo,
    willPo,
    convo,
    willConvo,
    employed,
    twits,
    email,
    app,
    fb,
    insta,
    li,
    skype,
    reddit,
    sms,
    poms
    )
     VALUES ( ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? )''', ( str(date), cycle, romance, caff, sunny, jour, writePo, readPo, willPo, convo, willConvo, employed, twits, email, app, fb, insta, li, skype, reddit, sms, poms ) )



#
# cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
#     VALUES ( ?, ? )''', ( album, artist_id ) )
# cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
# album_id = cur.fetchone()[0]
#
# cur.execute('''INSERT OR IGNORE INTO Genre (name)
#     VALUES ( ? )''', ( genre, ) )
# cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
# genre_id = cur.fetchone()[0]
#
# cur.execute('''INSERT OR REPLACE INTO Track
#     (title, album_id, genre_id, len, rating, count)
#     VALUES ( ?, ?, ?, ?, ?, ?)''',
#     ( name, album_id, genre_id, length, rating, count ) )
#
conn.commit()




print('cool, bye!')

## if the other is new,
