# The sqlite3 module 
import sqlite3 as lite
import pandas as pd

#tuples hold table data
cities = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December'),
                     ('Atlanta', 2013, 'July', 'January'))


#Connect to the database. 
con = lite.connect('getting_started.db')

# Drop the tables, create tables and insert rows by passing tuples to `execute()`
with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cities;")
    cur.execute("DROP TABLE IF EXISTS weather;")
    cur.execute("CREATE TABLE cities (name text, state text);")
    cur.execute("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);")
    
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?)", weather)

# join data in table and load into a pandas DataFrame 
with con:

    cur = con.cursor()
    cur.execute("SELECT name, state FROM cities INNER JOIN weather ON name=city WHERE warm_month=?", (month,))

    rows = cur.fetchall()
    df = pd.DataFrame(rows)

    print "The cities that are warmest in July are: "

newlist = []
for i in df.index:
    newlist.append(df.ix[i,0]+','+df.ix[i,1])

print ", ".join(newlist )