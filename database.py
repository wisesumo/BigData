# The sqlite3 module 
import sqlite3 as lite
import pandas as pd

#tuples hold table data
cities = (('Las Vegas', 'NV'),
                    ('Atlanta', 'GA'))

weather = (('Las Vegas', 2013, 'July', 'December'),
                     ('Atlanta', 2013, 'July', 'January'))


# connect to the database. 
con = lite.connect('getting_started.db')

# Inserting rows by passing tuples to `execute()`
with con:

    cur = con.cursor()
    cur.executemany("DROP TABLE IF EXISTS cities;")
    cur.executemany("DROP TABLE IF EXISTS weather;")

    cur.executemany("CREATE TABLE cities (name text, state text);")
    cur.executemany("CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);")
    
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?)", weather)


    cur.executemany("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather ON name = city;")
    
    input_dataframe = pd.read_csv('getting_started.db')

   cur.executemany("")
   "The cities that are warmest in July are:"